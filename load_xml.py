import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages    
from numba import jit

def load_plot_xml(path_xml,output_path):
    path_output_f = f"{output_path}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    print(f"Loading plot data from {path_xml} to {path_output_f}")
    with open(f"{path_xml}", 'r') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            if '<plot prin_corr' in line:
                name = line.split("<")[1].split(">")[0].split("plot ")[1]
                
                with open(f"{path_output_f}/{name}", 'w') as f:
                    while True:
                        i += 1
                        if '</plot prin_corr' in content[i]:
                            break
                        f.write(content[i])

def load_prin_corr_xml(path_xml,output_path):
    path_output_f = f"{output_path}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    print(f"Loading plot data from {path_xml} to {path_output_f}")
    with open(f"{path_xml}", 'r') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            if '<pc prin_corr' in line:
                name = line.split("<")[1].split(">")[0].split("pc ")[1]
                
                with open(f"{path_output_f}/{name}", 'w') as f:
                    while True:
                        i += 1
                        if '</pc prin_corr' in content[i]:
                            break
                        f.write(content[i])
def load_mass_xml(path,path_output, model_avg=False):
    path_output_f = f"{path_output}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    
    with open(f"{path}", 'r') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            if '<elem>' in line:
                name_line = content[i + 1]
                value_line = content[i + 2]
                error_line = content[i + 3]
                name = name_line.split('<name>')[1].split('</name>')[0]
                value = float(value_line.split('<value>')[1].split('</value>')[0])
                error = float(error_line.split('<error>')[1].split('</error>')[0])
                if i != len(content)-1:
                    model_avg_value_line = content[i + 4]
                    model_avg_error_line = content[i + 5]
                    if '<model_average_value>' in model_avg_value_line and '<model_average_error>' in model_avg_error_line and model_avg:
                        value = float(model_avg_value_line.split('<model_average_value>')[1].split('</model_average_value>')[0])
                        error = float(model_avg_error_line.split('<model_average_error>')[1].split('</model_average_error>')[0])
                    
                
                with open(f"{path_output_f}/{name}", 'w') as f:
                    f.write(f"{value} {error}")
def load_mass_xml_model_avg_list(path,path_output, model_avg_list):
    path_output_f = f"{path_output}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    
    with open(f"{path}", 'r') as file:
        content = file.readlines()
        for i, line in enumerate(content):
            if '<elem>' in line:
                name_line = content[i + 1]
                value_line = content[i + 2]
                error_line = content[i + 3]
                name = name_line.split('<name>')[1].split('</name>')[0]
                statenum = int(name.split('state')[1].split('.')[0])
                if statenum not in model_avg_list:
                    model_avg = False
                else:
                    print(f"Model averaging for {name}")
                    model_avg = True
                
                value = float(value_line.split('<value>')[1].split('</value>')[0])
                error = float(error_line.split('<error>')[1].split('</error>')[0])
                if model_avg:
                    print(f"Old value: {value}, error: {error}")
                if i != len(content)-1:
                    model_avg_value_line = content[i + 4]
                    model_avg_error_line = content[i + 5]
                    if '<model_average_value>' in model_avg_value_line and '<model_average_error>' in model_avg_error_line and model_avg:
                        value = float(model_avg_value_line.split('<model_average_value>')[1].split('</model_average_value>')[0])
                        error = float(model_avg_error_line.split('<model_average_error>')[1].split('</model_average_error>')[0])
                        print(f"Model average value: {value}, error: {error}")
                    
                
                with open(f"{path_output_f}/{name}", 'w') as f:
                    f.write(f"{value} {error}")
def normalize_Z(path,output_path):
    output_path_f = f"{output_path}"
    if not os.path.exists(output_path_f):
        os.makedirs(output_path_f)
    files = os.listdir(path)
    
    max_op = max([int(file.split('op')[1].split('.')[0]) for file in files if 'op' in file])+1
    for op in range(max_op):
        op_files = [file for file in files if f'op{op}' in file]

        if not op_files:
            continue
        vals,errs = [],[]
        for file in op_files:
            with open(f"{path}/{file}", 'r') as f:
                content = f.readlines()
                for line in content:
                    
                    val, err = line.split()[0], line.split()[1]
                    val = float(val)
                    err = float(err)
                    vals.append(val)
                    errs.append(err)
        maximum = max(vals)
        normalized_vals = [val / maximum for val in vals]
        normalized_errs = [err / maximum for err in errs]
        for i, file in enumerate(op_files):
            with open(f"{output_path_f}/{file}", 'w') as f:
                f.write(f"{normalized_vals[i]} {normalized_errs[i]}\n")
        
        


def load_Z(path,path_output, model_avg=False):
    path_output_f = f"{path_output}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    print(f"Loading Z factors from {path} to {path_output_f}")

    with open(f"{path}", 'r') as file:

        content = file.readlines()
        for i, line in enumerate(content):
            if '<elem>' in line:
                name_line = content[i + 1]
                value_line = content[i + 2]
                error_line = content[i + 3]
                name = name_line.split('<name>')[1].split('</name>')[0]
                value = float(value_line.split('<value>')[1].split('</value>')[0])
                error = float(error_line.split('<error>')[1].split('</error>')[0])
                if i != len(content)-1:
                    model_avg_value_line = content[i + 4]
                    model_avg_error_line = content[i + 5]
                    if '<model_average_value>' in model_avg_value_line and '<model_average_error>' in model_avg_error_line and model_avg:
                        value = float(model_avg_value_line.split('<model_average_value>')[1].split('</model_average_value>')[0])
                        error = float(model_avg_error_line.split('<model_average_error>')[1].split('</model_average_error>')[0])
                
                with open(f"{path_output_f}/{name}", 'w') as f:
                    
                    f.write(f"{value} {error}")
def load_fit_options(path_xml, output_path, model_avg=False):
    with open(path_xml, 'r') as f:
        content = f.readlines()
        fit_options = {}
        for i, line in enumerate(content):
            if "<elem>" in line:
                
                name_line = content[i + 1]
                value_line = content[i + 2]
                error_line = content[i + 3]
                name = name_line.split('<name>')[1].split('</name>')[0]
                value = float(value_line.split('<value>')[1].split('</value>')[0])
                error = float(error_line.split('<error>')[1].split('</error>')[0])
                if i != len(content)-1:
                    model_avg_value_line = content[i + 4]
                    model_avg_error_line = content[i + 5]
                    model_avg_value_A_line = content[i + 6]
                    model_avg_error_A_line = content[i + 7]
                    model_avg_value_dm_line = content[i + 8]
                    model_avg_error_dm_line = content[i + 9]
                    if '<model_average_value>' in model_avg_value_line and '<model_average_error>' in model_avg_error_line and model_avg:
                        value = float(model_avg_value_line.split('<model_average_value>')[1].split('</model_average_value>')[0])
                        error = float(model_avg_error_line.split('<model_average_error>')[1].split('</model_average_error>')[0])
                        if '<model_average_value_A>' in model_avg_value_A_line and '<model_average_error_A>' in model_avg_error_A_line:
                            A_value = float(model_avg_value_A_line.split('<model_average_value_A>')[1].split('</model_average_value_A>')[0])
                            A_error = float(model_avg_error_A_line.split('<model_average_error_A>')[1].split('</model_average_error_A>')[0])
                            dm_value = float(model_avg_value_dm_line.split('<model_average_value_dm>')[1].split('</model_average_value_dm>')[0])
                            dm_error = float(model_avg_error_dm_line.split('<model_average_error_dm>')[1].split('</model_average_error_dm>')[0])
                            fit_options[name] = [("model_average", value, error, "N/A", "N/A", "blue", 0,[A_value, A_error, dm_value, dm_error,"N/A", "N/A"])]
                        else:
                            fit_options[name] = [("model_average", value, error, "N/A", "N/A", "blue", 0,[])]
                in_fit_options = False
 
                l = 2
                for j, line_w in enumerate(content[i + 3:]):
                        if "<fit options>" in line_w:
                            in_fit_options = True
                            continue

                        if "</fit options>" in line_w:

                            break
                        if in_fit_options:
                            if "<option>" in line_w:
                                l += 1
                                names = content[i + j +4].split('<name>')[1].split('</name>')[0]
                                if names.strip() == "Chosen fit":
                                    names = "Chosen_fit"
                                names = names.replace(" ", "_")
                                names = names.replace("=", "")
                                values = float(content[i + j + 5].split('<value>')[1].split('</value>')[0])
                                errors = float(content[i + j + 6].split('<error>')[1].split('</error>')[0])
                                chisq = (content[i + j + 7].split('<chi_square>')[1].split('</chi_square>')[0])
                                P = content[i + j + 8].split('<P>')[1].split('</P>')[0]
                                if "m' value" in  content[i + j + 9]:
                                    mp = float(content[i + j + 9].split("<m' value>")[1].split("</m' value>")[0])
                                    mp_err = float(content[i + j + 10].split("<m' error>")[1].split("</m' error>")[0])
                                    A = float(content[i + j + 11].split("<A value>")[1].split("</A value>")[0])
                                    A_err = float(content[i + j + 12].split("<A error>")[1].split("</A error>")[0])
                                    extra_p = [mp, mp_err, A, A_err]
                                else:
                                    extra_p = []
                                if "<A>" in content[i + j + 9]:
                                    A = content[i + j + 9].split("<A>")[1].split("</A>")[0]
                                    A_err = content[i + j + 10].split("<A_err>")[1].split("</A_err>")[0]
                                    P_A = content[i + j + 11].split("<P_A>")[1].split("</P_A>")[0]
                                    dm = content[i + j + 12].split("<dm>")[1].split("</dm>")[0]
                                    dm_err = content[i + j + 13].split("<dm_err>")[1].split("</dm_err>")[0]
                                    P_dm = content[i + j + 14].split("<P_dm>")[1].split("</P_dm>")[0]
                                    extra_p = [A,A_err, dm, dm_err,P_A, P_dm]
                                    
                                color = "black"
                                k = l
                                if P == "N/A":
                                    P = "N/A"
                                    color = 'red'
                                    k= 1
                                    chosen_v = values
                                    chosen_err = errors
                                elif P == "-":
                                    P = "N/A"
                                
                                else:
                                    try:
                                        P = float(P)
                                    except ValueError:
                                        P = float(P.split("=")[1].strip())
                                
                                try :
                                    chisq = float(chisq.split("=")[1].strip())
                                except IndexError:
                                    chisq = float(chisq)
                                if name not in fit_options.keys():
                                    fit_options[name] = [(names, values, errors, chisq, P, color, k, extra_p)]
                                else:
                                    fit_options[name].append((names, values, errors, chisq, P, color, k, extra_p))
                with open(f"{output_path}/{name}", 'w') as f:
                    if name not in fit_options.keys():
                        return
                    for option in fit_options[name]:
                        f.write(f"{option[0]} {option[1]} {option[2]} {option[3]} {option[4]} {option[5]} {option[6]} {option[7]}\n")
                       