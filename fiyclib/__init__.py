import platform
import sys
import os

if(platform.python_version()[0] == '2'):
    from . import py2 as lib
else:
    from . import py3 as lib

