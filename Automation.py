import glob 
import os.path 
import re 
import subprocess

in_file = /nfs/site/disks/crt_stdcells_001/stdcells/esd_lib/esd783_r0.8.0_23ww28.5/lef/common/ip78_esd_lib.lef
in_lib = ip78_esd_lib
in_oas_file= /nfs/site/disks/x5e2d_gwa_jovenpey_01/p1278/work/p3/pdk783_r0.8HP/hdk/pds/oasis/
oas_file = glob.glob(in_oas_file) 
file_one = open(in_file, "r") 
for line in file_one:
    if re.search('MACRO', line): 
        
        cell = line.replace('MACRO','') 
        cell = cell.strip() 
       
        cmd_oas_file = "$SMAKE_LINE" + " " + "lib=" + in_lib + " " + "cell=" + cell + " stream stream_add_options=" + "\"-propMap /p/hdk/pu_tu/prd/gen_data/22.07.18_rc/common/streamout_inst_name_prop.map -replaceBusBitChar\" "
        os.system(cmd_oas_file)
       
        cmd_oas_file = "smartlauncher --cores 4 --memory 64 rapidesd -layout" + " " + in_oas_file + cell + '.oas' + " " + "-design" + " " + cell + " " + "-pst_pkg 1 -format oas -savedb -work $PWD"   
        os.system(cmd_oas_file)
       
        print(cmd_oas_file)    
        


