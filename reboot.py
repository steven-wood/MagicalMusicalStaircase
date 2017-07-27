import sys, os, time
def restartProgram():
    python = sys.executable
    os.execl(python, python, *sys.argv)