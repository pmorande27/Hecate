import xml_reconfit
import os
import sys
import shutil
def hecate_reconfit(output,output_pathi,op_listpath):
    """
    Function to run the hecate twopt information collection.
    It will read the t0 values from the /. directory and call the
    calculate_masses_and_error_twopt and calculate_ZFactor_and_error_twopt functions
    to obtain all the information needed to create the xml files.
    """
    path_final = f"{output}/reconfit"
    file_content = os.listdir(output)
    if not os.path.exists(output_pathi):
        os.mkdir(output_pathi)
    shutil.copy(ops_list,f"{output_pathi}/ops.list")

    for item in file_content:
        if "t0" in item and not "multi" in item:

            t0 = item.split("t0")[1]
            path_to_states = f"./{item}"
            output_path = f"{output_pathi}/xml"
            output_path_plots = f"{output_pathi}/xml_plots"
            output_path_pc = f"{output_pathi}/pc_xml"
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            if not os.path.exists(output_path_plots):
                os.mkdir(output_path_plots)
            if not os.path.exists(output_path_pc):
                os.mkdir(output_path_pc)
            name_energies = f"energies_t0_{t0}.xml"
            name_factors = f"ZFactors_t0_{t0}.xml"
            name_plots = f"prin_corrs_t0_{t0}.xml"
            name_pc = f"pc_t0_{t0}.xml"
            print(f"Processing t0: {t0}")
            xml_reconfit.calculate_ZFactor_and_error_reconfit(path_to_states, output_path, t0,name_xml=name_factors)
            xml_reconfit.calculate_masses_and_error_reconfit(path_to_states, output_path, t0,name_xml=name_energies)
            xml_reconfit.create_plot_xml(path_to_states, output_path_plots,t0, name_xml=name_plots)
                        
            xml_reconfit.create_pc_xml(path_to_states, output_path_pc,t0, name_xml=name_pc)
            print(f"moving {item} to {path_final}")
            shutil.move(f"{output}/{item}", path_final)

if __name__ == "__main__":
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

    hecate_reconfit(output=output,output_pathi=output_path,op_listpath=ops_list)  