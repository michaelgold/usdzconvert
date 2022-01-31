import glob
import os
import subprocess
import shutil

source_file_list =  glob.glob("../source/assets/*.glb")

for input_file_name in source_file_list:
    input_file_name = os.path.split(input_file_name)[1]
    output_file_name = "../dist/assets/{}.usdz".format(os.path.splitext(input_file_name)[0])
    print(output_file_name)
    subprocess.call("python run_usd.py usdzconvert/usdzconvert {} {}".format(input_file_name, output_file_name), shell=True, check=True )

for glb_file in source_file_list:
    print(glb_file)
    destination = "../dist/assets/{}".format(os.path.split(glb_file)[1])
    shutil.copyfile(glb_file, destination)
