import setuptools

PACKAGE_NAME='ppline'
PACKAGE_AUTHOR='5x12'
PACKAGE_AUTHOR_EMAIL='contact@awolf.io'
PACKAGE_DESCR='Pipeline framework.'

try:
   from ppline.version import __version__ as version
except ImportError:
   exec(f'from {PACKAGE_NAME}.version import __version__ as version')


with open('README.md', 'r') as f: long_description=f.read()

setuptools.setup(
   name=PACKAGE_NAME,
   version=version,
   author=PACKAGE_AUTHOR,
   url = 'https://github.com/5x12/ppline',
   download_url = 'https://github.com/5x12/ppline/archive/0.1.9.tar.gz',
   description=PACKAGE_DESCR,
   long_description=long_description,
   license='MIT',
   long_description_content_type='text/markdown',
   packages=setuptools.find_packages(),
   install_requires=['schema', 'PyYAML'],
   keywords = ['PIPELINE', 'PIPE'],
   python_requires='>=3.6',
   include_package_data=True,
   classifiers=[
    'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
  ],
)
