from setuptools import setup, find_packages

setup( 
  name='mypackage',
  version='0.1',
  packages=find_packages(exclude=['tests*']),
  license='MIT',
  description='Learning to build packages in python!',
  long_description=open('README.md').read(),
  install_requires=['numpy'],
  url='https://github.com/RimanaSifiso/mypackage',
  author="Sifiso",
  author_email='rimanasifiso@gmail.com',
)