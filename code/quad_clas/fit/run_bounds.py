import os, sys
from ..core import bounds as bounds


class ScanBounds:
    """
    This python class object scans through EFT parameter space and computes the z-score.
    """

    def __init__(self, root_path, dict_int, mc_run, luminosity, truth=True, nn=True, fit=True):
        """

        Parameters
        ----------
        root_path: str
            location to root directory
        dict_int: dict
            dictionary with eft points as keys and location of the corresponding lhe-file as values
        mc_run: int
            labels the run. Each run gives an independent replica.
        luminosity: float
            luminosity of the experiment in pb^-1
        truth: bool
            Includes the truth scanning
        nn: bool
            Includes the nn scanning
        fit: bool
            Should be set to true for every new scan. After one run, it can be set to False.
        """

        self.root_path = root_path
        self.output_path = os.path.join(self.root_path, 'output/z_scores')
        self.plots_path = os.path.join(self.output_path, 'plots')
        self.paths = {'root': self.root_path, 'output': self.output_path, 'plots': self.plots_path}
        self.dict_int = dict_int
        self.luminosity = luminosity
        self.fit = fit

        self.mc_run = mc_run
        self.truth = truth
        self.nn = nn

        # start the scanning
        self.run_scan()

    def run_scan(self):
        #TODO: only load the data once for the truth and the nn
        if self.truth:
            self.paths['output'] = os.path.join(self.output_path, 'truth')
            bounds.StatAnalysis(self.paths, dict_int=self.dict_int, nn=False, mc_run=self.mc_run, fit=self.fit, luminosity=self.luminosity)
        if self.nn:
            self.paths['output'] = os.path.join(self.output_path, 'nn')
            bounds.StatAnalysis(self.paths, dict_int=self.dict_int, nn=True, mc_run=self.mc_run, fit=self.fit, luminosity=self.luminosity)
