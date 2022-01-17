import sys
from cx_Freeze import setup, Executable
setup(name= "PhotovolaticGA",
	version= "3.1",
	executables = [Executable("D:\PhotovolaticGA\mainpage.py", base= "Win32GUI")])