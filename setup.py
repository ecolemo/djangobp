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
      package_data={'djangobp.scaffold.app.static': ['css/*', 'js/*', 'images/*', 'fancybox/*'],
                    'djangobp.scaffold.app.templates': ['*'],
                    },
      scripts=['scripts/djangobp-install.py']
      )
