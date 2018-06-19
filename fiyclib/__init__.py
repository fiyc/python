import platform
import sys
import os

print(os.path.abspath(__file__))


if(platform.python_version()[0] == '2'):
    from . import py2 as lib
else:
    from . import py3 as lib

# import sys
# import http_help


# import os
# import platform
# print(platform.python_version())

# py2Path = os.path.abspath('./library/py2')
# py3Path = os.path.abspath('./library/py3')
# commonPath = os.path.abspath('./library/common')

# sys.path.append(commonPath)
# if (platform.python_version()[0] == '2'):
#     sys.path.append(py2Path)
#     sys.path.append(py2Path2)
# else:
#     sys.path.append(py3Path)
#     sys.path.append(py3Path2)

