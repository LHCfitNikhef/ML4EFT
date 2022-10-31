"""
Module to compute kinematic variables from a LHE file
"""

import pylhe
import numpy as np


class Kinematics(pylhe.LHEParticle):
    """
    LHE kinematics class
    """

    def __init__(self, particle):
        """
        Loads and combines particles as read from a LHE file

        Parameters
        ----------
        particle: :class:`pylhe.LHEParticle`
            LHE particle object

        Examples
        --------
        We consider :math:`pp\\rightarrow ZH \\rightarrow \ell^+\ell^-b\\bar{b}\;` as a simple example

        >>> import pylhe
        >>> lhe_init = pylhe.read_lhe_init(path_to_lhe)

        Loop over the events in the LHE file and append kinematics

        >>> events = []
        >>> for e in pylhe.read_lhe(path_to_lhe):
        ...     incoming_part = []
        ...     # create particle instances
        ...     for part in e.particles:
        ...         if part.id in [11, 13]: # e^- or \mu^-
        ...            l1 = lhe.Kinematics(part)
        ...         elif part.id in [-11, -13]: # e^+ or \mu^+
        ...            l2 = lhe.Kinematics(part)
        ...         elif part.id == 5: # b
        ...            b = lhe.Kinematics(part)
        ...         elif part.id == -5: #bbar
        ...            bbar = lhe.Kinematics(part)
        ...
        ...     # Particle systems can be created by adding the separate particle instances
        ...     ll = l1 + l2 # dilepton system
        ...     bb = b + bbar # b bbar sytem
        ...     events.append([l1.get_pt(), l2.get_pt(), ll.get_invariant_mass()])

        ``events`` now contains the requested kinematics for all events in the LHE file
        """

        if isinstance(particle, pylhe.LHEParticle):
            particle.__dict__.pop('event')
            super().__init__(**particle.__dict__)
        else:
            super().__init__(**particle)

    def __add__(self, other):
        """
        Returns the system of two :class:`pylhe.LHEParticle` objects

        Parameters
        ----------
        other: :class:`ml4eft.preproc.compute_kinematics.Kinematics`
            Kinematics object to combine

        Returns
        -------
        :class:`ml4eft.preproc.compute_kinematic.Kinematics`
            Kinematics object of the combined system

        """
        dict = self.__dict__.copy()
        dict['e'] = self.e + other.e
        dict['px'] = self.px + other.px
        dict['py'] = self.py + other.py
        dict['pz'] = self.pz + other.pz

        return self.add_system(dict)

    @classmethod
    def add_system(cls, dict):
        """
        Returns a class instance of :class:`pylhe.LHEParticle`

        Parameters
        ----------
        dict: dict
            Combined particle dictionary

        Returns
        -------
        :class:`ml4eft.preproc.lhe_reader.Kinematics`
            Kinematics object of the combined system

        """
        return cls(dict)

    def get_inv_mass(self):
        """
        Returns the invariant mass in GeV

        Returns
        -------
        float
            Invariant mass in GeV

        """
        return np.sqrt(
            sum((1 if mu == 'e' else -1) * getattr(self, mu) ** 2 for mu in ['e', 'px', 'py', 'pz']))

    def get_pt(self):
        """
        Returns the transverse momentum in GeV

        Returns
        -------
        float
            Transverse momentum in GeV
        """
        return np.sqrt(getattr(self, 'px') ** 2 + getattr(self, 'py') ** 2)

    def get_p(self):
        """
        Returns the magnitude of the 3-momentum

        Returns
        -------
        float
            Magnitude of the 3-momentum
        """
        return np.sqrt(getattr(self, 'px') ** 2 + getattr(self, 'py') ** 2 + getattr(self, 'pz') ** 2)

    def get_phi(self):
        """
        Returns the azimuthal angle in radians with respect to the x-axis

        Returns
        -------
        phi: float
            Azimuthal angle with respect to the y-axis in the transverse plane
        """
        p_x = getattr(self, 'px')
        p_y = getattr(self, 'py')

        if p_x > 0 and p_y > 0:
            phi = np.arctan(p_x / p_y)
        elif p_y < 0:
            phi = np.arctan(p_x / p_y) + np.pi
        else:
            phi = 2 * np.pi + np.arctan(p_x / p_y)
        return phi

    def get_theta(self):
        """
        Returns the scattering angle in radians with respect to the beam-axis

        Returns
        -------
        float
            Scattering angle with respect to the beam-axis
        """
        cos_theta = getattr(self, 'pz') / self.get_p()
        return np.arccos(cos_theta)

    def get_pseudorapidity(self):
        """
        Returns the pseudorapidity :math:`\eta`

        Returns
        -------
        eta: float
            Pseudorapidity
        """
        theta = self.get_theta()
        eta = - np.log(np.tan(theta / 2))
        return eta

    def get_rapidity(self):
        """
        Returns the rapidity :math:`Y`

        Returns
        -------
        y: float
            Rapidity
        """
        q0 = getattr(self, 'e')  # energy of the top quark pair in the pp COM frame
        q3 = getattr(self, 'pz')
        y = 0.5 * np.log((q0 + q3) / (q0 - q3))
        return y


def get_deta(eta1, eta2):
    """
    Returns the absolute difference in pseudorapidity

    Parameters
    ----------
    eta1: float
        Pseudorapidity of particle 1
    eta2: float
        Pseudorapidity of particle 2

    Returns
    -------
    float
        Absolute difference in pseudorapidity
    """
    return np.abs(eta1 - eta2)


def get_dphi(phi1, phi2):
    """
    Returns the absolute difference in azimuthal angle

    Parameters
    ----------
    phi1: float
        Azimuthal angle of particle 1
    phi2: float
        Azimuthal angle of particle 2

    Returns
    -------
    float
        Absolute difference in azimuthal angle (shortest)
    """
    dphi = np.abs(phi1 - phi2)
    return dphi if dphi <= np.pi else 2 * np.pi - dphi
