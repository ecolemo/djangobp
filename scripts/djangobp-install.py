#!/usr/bin/env python
from djangobp.editsettings import install_app
import sys
import os
import importlib

if __name__ == "__main__":
    settings = os.getcwd().split('/')[-1] + '.settings'
    sys.path.append('.')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
    install_app('djangobp')
