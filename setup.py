from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

with open('test_requirements.txt','r') as f:
    test_requirements = f.read().splitlines()

setup(
    name = 'aibs_dipde',
    version = '0.2.1',
    description = """DiPDE (dipde) is a simulation platform for numerically solving the time evolution of coupled networks of neuronal populations. Instead of solving the subthreshold dynamics of individual model leaky-integrate-and-fire (LIF) neurons, dipde models the voltage distribution of a population of neurons with a single population density equation.""",
    author = "Nicholas Cain",
    author_email = "nicholasc@alleninstitute.org",
    url = 'http://stash.corp.alleninstitute.org/scm/~nicholasc/aibs.dipde',
    packages = find_packages(),
    include_package_data=True,
    install_requires = requirements,
    entry_points={
          'console_scripts': [
              'aibs.dipde = aibs.dipde.__main__:main'
        ]
    },
    license="Allen Institute Software License",
    setup_requires=['pytest-runner'],
    tests_require = test_requirements
)
