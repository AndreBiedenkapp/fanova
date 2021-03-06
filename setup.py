from setuptools import setup, find_packages

setup(
    name = "fanova",
    version = "2.0.1",
    packages = find_packages(),
    install_requires = [
                        'numpy',
                        'docutils>=0.3',
                        'setuptools',
                        'matplotlib>=1.4.2',
                        'ConfigSpace'],

    author = "Stefan Falkner and Christina Hernandez Wunsch. Legacy branch: Tobias Domhan, Aaron Klein and Frank Hutter (FANOVA)",
    author_email = "sfalkner@cs.uni-freiburg.de",
    description = "Functional ANOVA: an implementation of the ICML 2014 paper 'An Efficient Approach for Assessing Hyperparameter Importance' by Frank Hutter, Holger Hoos and Kevin Leyton-Brown.",
    include_package_data = True,
    keywords = "hyperparameter parameter optimization bayesian smac global variance analysis",
    license = "FANOVA is free for academic & non-commercial usage. Please contact Frank Hutter(fh@informatik.uni-freiburg.de) to discuss obtaining a license for commercial purposes.",
    url = "http://automl.org/fanova"
)
