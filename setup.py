from setuptools import setup, find_packages

def parse_requirements(filename:str) -> list:
    """Reads the requirements.txt file and returns a list of packages."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

setup(
    name='TaskMorph',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='unlincense',
    description='Methods that will help you in coding RPAs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Nando2003/ezScraping',
    install_requires=parse_requirements('requirements.txt'),
    author='Fernando Fontes',
    author_email='nandofontes30@gmail.com',
)