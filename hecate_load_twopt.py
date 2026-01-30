import os
import load_xml
from alive_progress import alive_bar

def reload_twopt_irrep_volume_mass(path_xmls,path_irrep_volume,model_avg_list,t0):
    content = os.listdir(path_xmls)
    for file in content:
        
        if "energies" in file and f"t0_{t0}" in file:
            print(f"Processing file: {file}")
            path_output = f"{path_irrep_volume}/t0{t0}/MassValues"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_mass_xml_model_avg_list(f"{path_xmls}/{file}",path_output, model_avg_list=model_avg_list)
            
        
      
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
            if not os.path.exists(f"{path_irrep_volume}/t0{t0}/FitOptions"):
                os.makedirs(f"{path_irrep_volume}/t0{t0}/FitOptions")
            load_xml.load_fit_options(f"{path_xmls}/{file}", f"{path_irrep_volume}/t0{t0}/FitOptions", model_avg=model_avg)
        
        elif "ZFactors" in file:
            t0 = file.split('t0_')[1].split('.')[0]
            path_output = f"{path_irrep_volume}/t0{t0}/ZValues"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_Z(f"{path_xmls}/{file}",path_output, model_avg=True)
            if not os.path.exists(f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized"):
                os.makedirs(f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized")
            load_xml.normalize_Z(path_output,f"{path_irrep_volume}/t0{t0}/ZvaluesRenormalized")
def load_pc(path_xmls,path_irrep_volume):
    content = os.listdir(path_xmls)
    for file in content:
        if "pc_" in file:
            t0 = file.split('t0_')[1].split('.')[0]
            print(f"Processing file: {file}")
            path_output = f"{path_irrep_volume}/t0{t0}/PrinCorrValues"
            if not os.path.exists(path_output):
                os.makedirs(path_output)
            load_xml.load_prin_corr_xml(f"{path_xmls}/{file}",path_output)
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
    path_xmls = "./D2A1M-reconfit/Volume_24/xml"
    path_irrep_volume = "./D2A1M-reconfit/Volume_24"
    load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=False)
    #reload_twopt_irrep_volume_mass(path_xmls,path_irrep_volume,model_avg_list=[3,5,4],t0=12)
    path_xmls = "./D2A1M-reconfit/Volume_24/xml_plots"
    load_plot_ax(path_xmls,path_irrep_volume)
