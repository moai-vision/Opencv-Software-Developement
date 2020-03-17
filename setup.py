from cx_Freeze import setup,Executable
import sys
#import all your used library
import cv2
import numpy as np



base=None #platoform base
program="test.py" #.py file
logo="logo.ico" #application logo

if sys.platform=="win32": #platoform search 
   base="Win32GUI"
   

fetch=[Executable(program,base=base,icon=logo)] #executable setups


#setup used packages and module and extra useful resources
build_exe_options = {"packages": ["cv2","numpy"]}

#applications setup
setup(name="test",
      version="1.0",
      description="software development testing",
      options={"build_exe": build_exe_options},
      executables=fetch
	  )
