import os
def delate_overlap_operator(path_irrep_volume,op):
    for dir in os.listdir(path_irrep_volume):
        if "t0" in dir:
            path = f"{path_irrep_volume}/{dir}/ZvaluesRenormalized"
            if not os.path.exists(path):
                continue
            for file in os.listdir(path):
                if f"op{op}.jack" in file:
                    print(f"Deleting {file} from {path}")
                    os.remove(f"{path}/{file}")
            path = f"{path_irrep_volume}/{dir}/ZValues"
            if not os.path.exists(path):
                continue
            for file in os.listdir(path):
                if f"op{op}.jack" in file:
                    print(f"Deleting {file} from {path}")
                    os.remove(f"{path}/{file}")
delate_overlap_operator("./T1mM-reconfit/Volume_24",43)
delate_overlap_operator("./T1mM-reconfit/Volume_24",44)