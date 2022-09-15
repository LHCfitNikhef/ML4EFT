# module to compute kinematics from a lhe file
import pylhe
import numpy as np

class Kinematics(pylhe.LHEParticle):

    def __init__(self, kwargs):
        if isinstance(kwargs, pylhe.LHEParticle):
            kwargs.__dict__.pop('event')
            super().__init__(**kwargs.__dict__)
        else:
            super().__init__(**kwargs)

    def __add__(self, other):
        dict = self.__dict__.copy()
        dict['e'] = self.e + other.e
        dict['px'] = self.px + other.px
        dict['py'] = self.py + other.py
        dict['pz'] = self.pz + other.pz

        return self.add_system(dict)

    @classmethod
    def add_system(cls, dict):
        return cls(dict)

    def get_inv_mass(self):
        return np.sqrt(
            sum((1 if mu == 'e' else -1) * getattr(self,mu) ** 2 for mu in ['e', 'px', 'py', 'pz']))

    def get_pt(self):
        return np.sqrt(getattr(self, 'px') ** 2 + getattr(self, 'py') ** 2)


    def get_p(self):
        return np.sqrt(getattr(self, 'px') ** 2 + getattr(self, 'py') ** 2 + getattr(self, 'pz') ** 2)

    def get_phi(self):
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
        cos_theta = getattr(self, 'pz') / self.get_p()
        return np.arccos(cos_theta)

    def get_pseudorapidity(self):
        theta = self.get_theta()
        eta = - np.log(np.tan(theta/2))
        return eta

    def get_rapidity(self):
        """
        Computes the rapidity of an event
        """
        q0 = getattr(self, 'e')   # energy of the top quark pair in the pp COM frame
        q3 = getattr(self, 'pz')
        y = 0.5 * np.log((q0 + q3) / (q0 - q3))
        return y


def get_dphi(phi1, phi2):
    dphi = np.abs(phi1-phi2)
    return dphi if dphi <= np.pi else 2 * np.pi - dphi

def get_deta(eta1, eta2):
    return np.abs(eta1 - eta2)