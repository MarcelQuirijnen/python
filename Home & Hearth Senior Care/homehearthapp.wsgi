
PROJECT_DIR = '/var/www/HomeHearthApp/HomeHearthApp'

import sys
sys.path.insert(0, PROJECT_DIR)

def execfile(filename):
    globals = dict( __file__ = filename )
    exec( open(filename).read(), globals )

import os
activate_this = os.path.join( PROJECT_DIR, 'hhapp/bin', 'activate_this.py' )
execfile(activate_this)

import sys
sys.stdout = sys.stderr

from homehearthapp import app as application
application.debug = True
