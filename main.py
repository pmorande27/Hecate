import hecate_load_twopt
import os
def trynew():
    V = 24
    irrep = "Try"
    path_xmls = f"../Analysis/{irrep}/trynew/xml"
    path_irrep_volume = f"../Analysis/{irrep}/Volume_{V}"
    hecate_load_twopt.load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=True)


def prior_analysis():
    V = 24
    irrep = "T1mM-prior-analysis"
    priors = ["noprior"]
    for prior in priors:
        path_xmls = f"../Analysis/{irrep}/Volume_{V}/eigen-prior-{prior}/xml"
        path_irrep_volume = f"../Analysis/{irrep}/Volume_{V}/eigen-prior-{prior}"
        hecate_load_twopt.load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=True)
        path_xmls = f"../Analysis/{irrep}/Volume_{V}/eigen-prior-{prior}/xml_plots"
        hecate_load_twopt.load_plot_ax(path_xmls,path_irrep_volume)
        path_xmls = f"../Analysis/{irrep}/Volume_{V}/eigen-prior-{prior}/pc_xml"

        if not os.path.exists(path_xmls):
            print(f"Path {path_xmls} does not exist, skipping...")
            continue
        hecate_load_twopt.load_pc(path_xmls,path_irrep_volume)
def pc_analysis():
    V = "twopt_eigen_cut_new_matching_generic_sv_cut_tmax_r"
    irrep = "T1mM-pc-analysis"
    path_xmls = f"../Analysis/{irrep}/{V}/xml"
    path_irrep_volume = f"../Analysis/{irrep}/{V}"
    
    hecate_load_twopt.load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=True)
    path_xmls = f"../Analysis/{irrep}/{V}/xml_plots"
    path_xmls = f"../Analysis/{irrep}/{V}/xml_plots"

    hecate_load_twopt.load_plot_ax(path_xmls,path_irrep_volume)
    path_xmls = f"../Analysis/{irrep}/{V}/pc_xml"
    if not os.path.exists(path_xmls):
        print(f"Path {path_xmls} does not exist, skipping...")
    else:
        hecate_load_twopt.load_pc(path_xmls,path_irrep_volume)

    

def main():
    volumes = [48]
    irrep = "../charmonium_865/p000-T1pP-3src"


    for i in volumes:
        V = i

        
        path_xmls = f"{irrep}/Volume_{V}/xml"
        path_irrep_volume = f"{irrep}/Volume_{V}"
        
        path_xmls = f"{irrep}/Volume_{V}/xml"
        hecate_load_twopt.load_twopt_irrep_volume(path_xmls,path_irrep_volume,model_avg=True)
        path_xmls = f"{irrep}/Volume_{V}/xml_plots"
        hecate_load_twopt.load_plot_ax(path_xmls,path_irrep_volume)
        path_xmls = f"{irrep}/Volume_{V}/pc_xml"
        if not os.path.exists(path_xmls):
            print(f"Path {path_xmls} does not exist, skipping...")
        else:
            hecate_load_twopt.load_pc(path_xmls,path_irrep_volume)

if __name__ == "__main__":
    main()