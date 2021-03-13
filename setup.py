import setuptools

PACKAGE_NAME='ppline'
PACKAGE_AUTHOR='5x12'
PACKAGE_AUTHOR_EMAIL='contact@awolf.io'
PACKAGE_DESCR='Pipeline framework.'

try:
   from ppline.version import __version__ as version
except ImportError:
   exec(f'from {PACKAGE_NAME}.version import __version__ as version')

def parse_requirements(filename):
    lines = (line.strip() for line in open(filename))
    return [line for line in lines if line and not line.startswith("#")]

with open('README.md', 'r') as f: long_description=f.read()

setuptools.setup(
   name=PACKAGE_NAME,
   version=version,
   author=PACKAGE_AUTHOR,
   description=PACKAGE_DESCR,
   long_description=long_description,
   license='MIT',
   long_description_content_type='text/markdown',
   packages=setuptools.find_packages(),
   install_requires=parse_requirements('requirements.txt'),
   python_requires='>=3.6',
   include_package_data=True,
)
