from setuptools import setup
setup(name='djangobp',
      version='1.0',
      packages=['djangobp', 
                'djangobp.management', 
                'djangobp.management.commands', 
                'djangobp.scaffold',
                'djangobp.scaffold.controllers',
                'djangobp.scaffold.templates'],
      )
