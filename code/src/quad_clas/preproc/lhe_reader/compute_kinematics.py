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


    # def add_p(p1, p2):
    #     temp = copy.deepcopy(p1)
    #     temp.px = p1.px + p2.px
    #     temp.py = p1.py + p2.py
    #     temp.pz = p1.pz + p2.pz
    #     return temp

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
        cos_theta = getattr(self, 'pz') / get_p(p)
        return np.arccos(cos_theta)

    def get_pseudorapidity(self):
        theta = self.get_theta()
        eta = - np.log(np.tan(theta/2))
        return eta

    def get_rapdity(self):
        """
        Computes the rapidity of an event
        """
        q0 = getattr(self, 'e')   # energy of the top quark pair in the pp COM frame
        q3 = getattr(self, 'pz')
        y = 0.5 * np.log((q0 + q3) / (q0 - q3))
        return y


    # def get_d_phi(p1, p2):
    #     phi_1 = get_phi(p1)
    #     phi_2 = get_phi(p2)
    #     d_phi = np.abs(phi_2 - phi_1)
    #     if d_phi > np.pi:
    #         return 2 * np.pi - d_phi
    #     else:
    #         return d_phi
    #
    #
    # def get_d_eta(p1, p2):
    #     eta_1 = get_eta(p1)
    #     eta_2 = get_eta(p2)
    #     d_eta = np.abs(eta_2 - eta_1)
    #     return d_eta
