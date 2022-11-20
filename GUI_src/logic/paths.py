# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:02:02 2022

@author: Aeasala
"""
import os
type_folder = 'folder'
type_file = 'file'

binfolder = 'bin'

class paths():
        
    rel_wd = "GUI_src/logic/"
    
    _wd = None
    _levels_below_bin = 2 + 0
    
    
    def __init__(self, levels_below_bin = 2, dbg = False):
        self.dbg = dbg
        self._levels_below_bin = levels_below_bin
        self._wd = os.getcwd()
        
        self.get_full_path = self.__get_full_path(self)
        self.get_rel_path = self.__get_rel_path(self)
        
        if self.dbg:
            print("╔══════════════════════════════════════════╗\n"
                  "║ :: Looking for binaries and libraries :: ║\n"
                  "╠══════════════════════════════════════════╣\n")
        self.validate()
        if self.dbg:
            print("\n"
                  "╚══════════════════════════════════════════╝")
        
    def validate(self):
        self.validate_bin()
        print()
        self.gmad_path = self.get_full_path.gmad()
        self.gmpublish_path = self.get_full_path.gmpublish()
        self.steam_api_path = self.get_full_path.steam_api()
    
    def validate_bin(self):
        os.chdir(self._wd)
        to_find = 'bin'

        hit = self._find(to_find, type_folder, is_folder = 'bin')
        
        
        
        return hit
    
    def get_wd(self):
        print(os.getcwd())
        return os.getcwd()
    
    def reset_wd(self):
        os.chdir(self._wd)
        
        
    def _find(self, to_find, find_type, relative = False, inside_folder = None, is_folder = None):
        
        os.chdir(self._wd)
        up_dir = '..' + os.sep
        
        rel_path_str = ''
        for directory_step in range(self._levels_below_bin):              
            os.chdir(up_dir)
            rel_path_str = os.path.join('..', rel_path_str)
            continue
        
        if inside_folder is not None and is_folder is not None:
            print("inside_folder and is_folder args cannot both be set.\n"
                  "clearing is_folder, looking inside_folder = 'bin'")
            is_folder = None
            inside_folder = 'bin'
        elif inside_folder is None and is_folder is None:
            inside_folder = 'bin'
            
        
        if inside_folder is not None:
            hit_try = os.path.join(os.getcwd(), inside_folder, to_find)
        else:
            hit_try = os.path.join(os.getcwd(), to_find)
            
        if os.path.exists(hit_try):

            if relative:
                hit = os.path.join(rel_path_str, binfolder, to_find)
            else:
                hit = hit_try
                
            if self.dbg:
                print(" > Found", find_type, "'" + to_find + "'")
        else:
            if self.dbg:
                print(" > Could not find", find_type, "'" + to_find + "'" + ".  Check your installation.")
            hit = None
        
        os.chdir(self._wd)
        return hit
        
    class __get_full_path():

        def __init__(self, object):
            self.wrapper = object
            
        def gmad(self):
            to_find = 'gmad.exe'
            find_type = type_file
            
            hit = self.wrapper._find(to_find, find_type, inside_folder = binfolder)
            
            return hit

        def gmpublish(self):
            to_find = 'gmpublish.exe'
            find_type = type_file
            
            hit = self.wrapper._find(to_find, find_type, inside_folder = binfolder)
            
            return hit

        def steam_api(self):
            to_find = 'steam_api.dll'
            find_type = type_file
            
            hit = self.wrapper._find(to_find, find_type, inside_folder = binfolder)
            
            return hit
            pass
        
    class __get_rel_path(): #unimplemented
        def __init__(self, object):
            self.wrapper = object    
            
        def gmad(self):
            to_find = 'gmad.exe'
            find_type = type_file
            
            hit = self.wrapper._find(to_find, find_type, inside_folder = binfolder, relative = True)
            
            return hit
            pass
        def gmpublish(self):
            pass
        def steam_api(self):
            pass

# for IDE debugging
if __name__ == "__main__":
    self = paths()
