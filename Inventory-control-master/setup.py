import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter', 'mysql', 'reportlab'],'include_msvcr' : True}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Inventory Control',
    version='1.0',
    description='Programa para controle de laboratório de montagem óptica!',
    options={'build_exe': build_exe_options},
    executables=[Executable('Versão_Beta1.0.py', base=base)]
)
