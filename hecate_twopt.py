import os
import xml_twopt
import create_Z_twopt
import numpy as np
import sys
import shutil 
def hecate_twopt(output,output_p,ops_list):
    """
    Function to run the hecate twopt information collection.
    It will read the t0 values from the /out directory and call the
    calculate_masses_and_error_twopt and calculate_ZFactor_and_error_twopt functions
    to obtain all the information needed to create the xml files.
    """
    file_content = os.listdir(output)
    if not os.path.exists(output_p):
        os.mkdir(output_p)
    shutil.copy(ops_list,f"{output_p}/ops.list")
    for item in file_content:
        if "t0" in item:
            t0 = item.split("t0_")[1]
            path_tot0 = f"{output}/{item}"
            path_to_states = f"{output}/{item}/prin_corrs"
            output_path = f"{output_p}/xml"
            output_path_plots = f"{output_p}/xml_plots"
            output_path_pc = f"{output_p}/pc_xml"
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            if not os.path.exists(output_path_plots):
                os.mkdir(output_path_plots)
            if not os.path.exists(output_path_pc):
                os.mkdir(output_path_pc)
            path_to_statefactors = f"{output}/{item}/z"
            name_energies = f"energies_t0_{t0}.xml"
            name_factors = f"ZFactors_t0_{t0}.xml"
            name_plots = f"prin_corrs_t0_{t0}.xml"
            name_pc = f"pc_t0_{t0}.xml"
            create_Z_twopt.create_overlaps(path_tot0,int(t0))
            xml_twopt.calculate_masses_and_error_twopt(path_to_states, output_path, t0,name_xml=name_energies)
            xml_twopt.calculate_ZFactor_and_error_twopt(path_to_statefactors, output_path, t0,name_xml=name_factors)

            xml_twopt.create_plot_xml(path_to_states, output_path_plots,t0, name_xml=name_plots)
            xml_twopt.create_pc_xml(path_to_states, output_path_pc,t0, name_xml=name_pc)
if __name__ == "__main__":
    ## if there is one argument take it as the out file, if not take the directroy to be out
    if len(sys.argv)== 4:
        output = sys.argv[2]
        output_path = sys.argv[3]
        ops_list = sys.argv[1]
    elif len(sys.argv)== 3:
        ops_list = sys.argv[1]
        output = sys.argv[2]
        output_path = output
    elif len(sys.argv) == 2:
        ops_list = sys.argv[1]

        output = "out"
        output_path = "out"
    else:
        ops_list = "ops.list"
        output = "out"
        output_path = "out"
    hecate_twopt(output,output_path,ops_list)  
