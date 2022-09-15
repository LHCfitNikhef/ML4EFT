from ml4eft.core.truth import tt_prod as axs

def plot_mg5_ana_mtt(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """
    axs.plotData(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path)


def plot_xsec_ana(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """
    axs.plot_xsec_ana(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path)