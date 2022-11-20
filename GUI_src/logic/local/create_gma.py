# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:02:02 2022

@author: Aeasala
"""
import sys, os,time
import subprocess
from subprocess import Popen, PIPE, STDOUT
from filelock import FileLock
from threading import Thread, Semaphore

sys.path.append("../")
from paths import paths

_levels_below_bin = 2 + 1


class gmadDaemon(Thread):
    def __init__(self, gmad_path, args = None):
        #Thread.__init__(self,target = self.loop, daemon = True)
        Thread.__init__(self)
        self.gmad_path = gmad_path
        self.gmad_call_string = ['start', self.gmad_path]
        self.stdout = None
        self.stderr = None
        
    def loop(self):
        print("in tha loop")
        time.sleep(5)
        print("leavin tha loop")
        
    def run(self):
        gmad_proc = Popen(self.gmad_call_string,
                          bufsize=1, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
        self.stdout = gmad_proc.communicate()
        while gmad_proc.poll() is None:
            line = gmad_proc.stdout.readline()
            if line.startswith('Press'):
                gmad_proc.communicate('\r\n')
        
class gmaMaker(paths):
    gmad_call_string = 'echo "unable to call gmad.exe.  contact the developer about this"'
    def __init__(self):
        paths.__init__(self, _levels_below_bin, dbg = True)
        self.gmad_path = self.get_rel_path.gmad()
        self.gmad_call_string = ['start', self.gmad_path]
        self.d = gmadDaemon(gmad_path = self.gmad_path)
        self.d.start()
    def gmad_unthreaded(self):
        
        gmad_proc = Popen(self.gmad_call_string,
                          bufsize=1, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
        for line in iter(gmad_proc.stdout.readline,''):
            print(line.rstrip())
            print("asdf")
        while gmad_proc.poll() is None:
            line = gmad_proc.stdout.readline()
            print("asdf")
            if line.startswith('Press'):
                gmad_proc.communicate('\r\n')
        print("out")
# for IDE debugging
if __name__ == "__main__":
    self = gmaMaker()
    
    #self.gmad_unthreaded()
    input()
    pass
