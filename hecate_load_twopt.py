import os
import load_xml
def load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=False):
    content = os.listdir(path_xmls)
    for file in content:
        print(f"Processing file: {file}")
        if "energies" in file:
            t0 = file.split('t0_')[1].split('.')[0]
            path_output = f"{path_irrep_volume}/t0{t0}/MassValues"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_mass_xml(f"{path_xmls}/{file}",path_output, model_avg=model_avg)
        elif "ZFactors" in file:
            t0 = file.split('t0_')[1].split('.')[0]
            path_output = f"{path_irrep_volume}/t0{t0}/ZValues"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_Z(f"{path_xmls}/{file}",path_output, model_avg=True)
            if not os.path.exists(f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized"):
                os.makedirs(f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized")
            load_xml.normalize_Z(path_output,f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized")
def load_plot_ax(path_xmls,path_irrep_volume):
    content = os.listdir(path_xmls)
    for file in content:
        if "prin_corrs" in file:
            t0 = file.split('t0_')[1].split('.')[0]
            print(f"Processing file: {file}")
            path_output = f"{path_irrep_volume}/t0{t0}/PrinCorrPlots"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_plot_xml(f"{path_xmls}/{file}",path_output)
if __name__ == "__main__":
    path_xmls = "./T1mM-testing/Volume_24/xml plots"
    path_irrep_volume = "./T1mM-testing/Volume_24"
    #load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=True)
    #load_xml.create_fit_options_plot(f"{path_xmls}/energies_t0_11.xml", f"{path_irrep_volume}/t011/FitOptions",True)  
    load_plot_ax(path_xmls,path_irrep_volume)     
            