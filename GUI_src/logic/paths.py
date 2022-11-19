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
    _levels_below_bin = 2
    
    def __init__(self):
                    
        self._wd = os.getcwd()
        
        self.GMAD_PATH = os.path.join('bin', 'gmad.exe')
        self.GMPUBLISH_PATH = os.path.join('bin', 'gmpublish.exe')
        self.STEAM_API_DLL_PATH = os.path.join('bin', 'steam_api.dll')
        


    def validate_bin(self):
        os.chdir(self._wd)
        to_find = 'bin'

        self.get_wd()
        for i in range(self._levels_below_bin):
            print(i)
            
            os.chdir('../')
            self.get_wd()
            
        print(os.getcwd() + self.GMAD_PATH)
        if os.path.exists(
                os.path.join(os.getcwd() + to_find)):
            
            self.found(to_find, type_folder)
        else:
            self.no_find(to_find, type_folder)
        os.chdir(self._wd)


    def found(self, name, item_type):
        print("Found", item_type, name)

    def no_found(self, name, item_type):
        print("Could not find", item_type, "'" + name + "'" + ".  Check your installation.")
        
    def refresh_paths(self):
        pass
    
    def get_wd(self):
        print(os.getcwd())
        
    def _find(self, to_find, find_type, relative = False):
        os.chdir(self._wd)
        up_dir = '..' + os.sep
        
        rel_path_str = ''
        
        for directory_step in range(self._levels_below_bin):              
            os.chdir(up_dir)
            rel_path_str = os.path.join('..', rel_path_str)
            continue
        print(os.path.join(rel_path_str, to_find))
        print(os.getcwd())
        
        print(os.path.exists(os.path.join(rel_path_str, binfolder, to_find)))
        hit_try = os.path.join(os.getcwd(), binfolder, to_find)
        if os.path.exists(hit_try):
            self.found(to_find, type_file)
            if relative:
                hit = ''

                pass
            else:
                hit = hit_try
        else:
            self.no_found(to_find, type_file)
            hit = None
        
        os.chdir(self._wd)
        return hit
        
    class get_full_path():
        
        def gmad():
            to_find = 'gmad.exe'
            find_type = type_file
            
            hit = self._find(to_find, find_type)
            
            return hit

        def gmpublish():
            to_find = 'gmpublish.exe'
            find_type = type_file
            
            hit = self._find(to_find, find_type)
            
            return hit

        def steam_api():
            to_find = 'steam_api.dll'
            find_type = type_file
            
            hit = self._find(to_find, find_type)
            
            return hit
            pass
        
    def get_rel_path():
        def gmad():
            pass
        def gmpublish():
            pass
        def steam_api():
            pass

# for IDE debugging
if __name__ == "__main__":
    self = paths()
    self.get_full_path.gmad()
    self.get_full_path.gmpublish()
    self.get_full_path.steam_api()