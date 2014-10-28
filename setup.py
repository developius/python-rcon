import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='rcon',
      version='1.0',
      py_modules=['rcon'],
      description='MCRcon',
      author='F. Anderson',
      author_email='finnian@fxapi.co.uk',
      url='https://github.com/xavbabe/python-rcon',
      long_description=read('README.md'),
      )
