import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='MCRcon',
      version='1.0',
      py_modules=['MCRcon'],
      description='MCRcon',
      author='B. Gale',
      author_email='barney.gale@gmail.com',
      url='http://github.com/barneygale/MCRcon',
      )
