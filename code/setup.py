import setuptools

setuptools.setup(
    name="ml4eft",
    version="0.0.3",
    author="J.J. ter Hoeve, M. Madigan, R.G. Ambrosio, J.Rojo, V.Sanz.",
    author_email="j.j.ter.hoeve@vu.nl",
    description="Machine Learning for Effective Field Theories",
    long_description="ML4EFT is a general open-source framework for the integration of unbinned multivariate observables into global fits of particle physics data. It makes use of machine learning regression and classification techniques to parameterise high-dimensional likelihood ratios, and can be seamlessly integrated into global analyses of, for example, the Standard Model Effective Field Theory and Parton Distribution Functions.",
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    url="https://lhcfitnikhef.github.io/ML4EFT",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "pandas",
        "seaborn",
        "torch",
        "scikit_learn",
        "wget",
        "joblib",
        "pylhe>=0.4.0"
        ],
    python_requires=">=3.7",
)
