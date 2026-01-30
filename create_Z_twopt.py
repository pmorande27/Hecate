import ensemble as ensem
import numpy
import os
def create_overlaps(out_path_t0,t0):
    z_path = f"{out_path_t0}/z"
    prin_corr = f"{out_path_t0}/prin_corrs"
    directories = os.listdir(z_path)
    for directory in directories:
        if "unord" in directory:
            continue
        mass_file = f"{prin_corr}/{directory}/m.jack"
        if not os.path.exists(mass_file):
            continue
        operators = os.listdir(f"{z_path}/{directory}")
        for operator in operators:
            if "op" not in operator:
                continue
            z_file = f"{z_path}/{directory}/{operator}/C.jack"
            if not os.path.exists(z_file):
                continue
            Z_file =  f"{z_path}/{directory}/{operator}/Z.jack"
            if os.path.exists(Z_file):
                pass
            ensem_Z = ensem.Z_ensemble(z_file,mass_file,t0)
            ensem_Z.write(Z_file)
