import xml_reconfit
import os
def hecate_reconfit():
    """
    Function to run the hecate twopt information collection.
    It will read the t0 values from the /. directory and call the
    calculate_masses_and_error_twopt and calculate_ZFactor_and_error_twopt functions
    to obtain all the information needed to create the xml files.
    """
    file_content = os.listdir(".")
    for item in file_content:
        if "t0" in item:

            t0 = item.split("t0")[1]
            path_to_states = f"./{item}"
            output_path = f"./xml"
            output_path_plots = f"./xml_plots"
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            if not os.path.exists(output_path_plots):
                os.mkdir(output_path_plots)
            #path_to_statefactors = f"out/{item}/z"
            name_energies = f"energies_t0_{t0}.xml"
            #name_factors = f"ZFactors_t0_{t0}.xml"
            #name_plots = f"prin_corrs_t0_{t0}.xml"
            #xml_twopt.calculate_ZFactor_and_error_twopt(path_to_statefactors, output_path, t0,name_xml=name_factors)
            xml_reconfit.calculate_masses_and_error_reconfit(path_to_states, output_path, t0,name_xml=name_energies)
            #xml_twopt.create_plot_xml(path_to_states, output_path_plots,t0, name_xml=name_plots)
if __name__ == "__main__":
    hecate_reconfit()  