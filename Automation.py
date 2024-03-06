import glob 
import os.path 
import re 
import subprocess

in_file = input("Enter the file name : ") # grep macro lef file
in_lib = input("Enter the Library name : ") # lib name eg: ip783...
in_oas_file= input("Enter the Oasis file directory: ") # /nfs/pdx/disks/x5e2d_gwa_aelumala_01/p1278/work/p3/pdk783_r0.5HP/hdk/pds/oasis/*.oas
oas_file = glob.glob(in_oas_file) # read all .oas in oas path
file_one = open(in_file, "r") # read .lef
for line in file_one:
    if re.search('MACRO', line): # grep macro
        
        cell = line.replace('MACRO','') #replace MACRO with empty line
        cell = cell.strip() # get the cell name only, removed space
        # CALL the command line for oasis file
        cmd_oas_file = "$SMAKE_LINE" + " " + "lib=" + in_lib + " " + "cell=" + cell + " stream stream_add_options=" + "\"-propMap /p/hdk/pu_tu/prd/gen_data/22.07.18_rc/common/streamout_inst_name_prop.map -replaceBusBitChar\" "
        os.system(cmd_oas_file)
        # rapid esd command
        cmd_oas_file = "smartlauncher --cores 4 --memory 64 rapidesd -layout" + " " + in_oas_file + cell + '.oas' + " " + "-design" + " " + cell + " " + "-pst_pkg 1 -format oas -savedb -work $PWD"   
        os.system(cmd_oas_file)
        # display the command to cross-cehck
        print(cmd_oas_file)    
        
  
#at terminal "python Automation.py"
