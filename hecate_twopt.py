import os
import xml_twopt
def hecate_twopt():
    """
    Function to run the hecate twopt information collection.
    It will read the t0 values from the /out directory and call the
    calculate_masses_and_error_twopt and calculate_ZFactor_and_error_twopt functions
    to obtain all the information needed to create the xml files.
    """
    file_content = os.listdir("out")
    for item in file_content:
        if "t0" in item:
            t0 = t0.split("t0_")[1]
            path_to_states = f"out/{item}/prin_corrs"
            output_path = f"out/xml"
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            path_to_statefactors = f"out/{item}/z"
            name_energies = f"energies_t0_{t0}.xml"
            name_factors = f"ZFactors_t0_{t0}.xml"
            xml_twopt.calculate_ZFactor_and_error_twopt(path_to_statefactors, output_path, t0,name_xml=name_factors)
            xml_twopt.calculate_masses_and_error_twopt(path_to_states, output_path, t0,name_xml=name_energies)
