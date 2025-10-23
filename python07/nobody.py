#!/usr/bin/env python3
import re 
with open("nobody.txt","r") as nobody_file_obj, open("fav_name.txt","w") as name_write:
     for line in nobody_file_obj:
          line=line.rstrip()
          #found=re.search(r"Nobody",line)
          #print(found) 
          name_write=re.sub(r"Nobody",r"Klayton",line)
          print(name_write) 
