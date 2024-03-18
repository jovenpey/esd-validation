import glob 
import os.path 
import re 
import subprocess

from text import in_file, in_lib, in_oas_file

print(in_file)
print(in_lib)
print(in_oas_file)

# oas_file = glob.glob(in_oas_file) 
# file_one = open(in_file, "r") 
# for line in file_one:
#     if re.search('MACRO', line): 
        
#         cell = line.replace('MACRO','') 
#         cell = cell.strip() 
       
#         cmd_oas_file = "$SMAKE_LINE" + " " + "lib=" + in_lib + " " + "cell=" + cell + " stream stream_add_options=" + "\"-propMap /p/hdk/pu_tu/prd/gen_data/22.07.18_rc/common/streamout_inst_name_prop.map -replaceBusBitChar\" "
#         os.system(cmd_oas_file)
       
#         cmd_oas_file = "smartlauncher --cores 4 --memory 64 rapidesd -layout" + " " + in_oas_file + cell + '.oas' + " " + "-design" + " " + cell + " " + "-pst_pkg 1 -format oas -savedb -work $PWD"   
#         os.system(cmd_oas_file)
       
#         print(cmd_oas_file)    
        
