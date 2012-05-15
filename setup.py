from setuptools import setup
setup(name='djangobp',
      version='1.0',
      packages=['djangobp', 
                'djangobp.management', 
                'djangobp.management.commands', 
                'djangobp.scaffold',
                'djangobp.scaffold.app',
                'djangobp.scaffold.app.controllers',
                'djangobp.scaffold.app.static',
                'djangobp.scaffold.app.templates'],
      )
