import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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
def normalize_Z(path,output_path):
    output_path_f = f"{output_path}"
    if not os.path.exists(output_path_f):
        os.makedirs(output_path_f)
    files = os.listdir(path)
    max_op = max([int(file.split('op')[1].split('.')[0]) for file in files if 'op' in file])
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

def create_fit_options_plot(xml_path, output_path, model_avg=False):
    with open(xml_path, 'r') as f:
        content = f.readlines()
        fit_options = []
        figures = []
        with PdfPages(f"{output_path}/fit_options.pdf") as pdf:
            for i, line in enumerate(content):
                if "<elem>" in line:
                    name_line = content[i + 1]
                    value_line = content[i + 2]
                    error_line = content[i + 3]
                    name = name_line.split('<name>')[1].split('</name>')[0]
                    value = float(value_line.split('<value>')[1].split('</value>')[0])
                    error = float(error_line.split('<error>')[1].split('</error>')[0])
                    in_fit_options = False
                    if i != len(content)-1:
                        model_avg_value_line = content[i + 4]
                        model_avg_error_line = content[i + 5]
                        if '<model_average_value>' in model_avg_value_line and '<model_average_error>' in model_avg_error_line and model_avg:
                            value = float(model_avg_value_line.split('<model_average_value>')[1].split('</model_average_value>')[0])
                            error = float(model_avg_error_line.split('<model_average_error>')[1].split('</model_average_error>')[0])
                        
                    
                    l = 2
                    fig,ax = plt.subplots()
                    vals = []
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
                                values = float(content[i + j + 5].split('<value>')[1].split('</value>')[0])
                                errors = float(content[i + j + 6].split('<error>')[1].split('</error>')[0])
                                chisq = (content[i + j + 7].split('<chi_square>')[1].split('</chi_square>')[0])
                                P = content[i + j + 8].split('<P>')[1].split('</P>')[0]
                                color = "black"
                                k = l
                                if P == "N/A":
                                    P = "N/A"
                                    color = 'red'
                                    k= 1
                                    chosen_v = values
                                    chosen_err = errors
                                else:
                                    P = float(P.split("=")[1].strip())
                                
                                chisq = float(chisq.split("=")[1].strip())
                                
                                ax.errorbar(values, k, xerr=errors, fmt='o', label=name,color=color)
                                vals.append(values)


                    ax.errorbar(value, 0, xerr=error, fmt='o', label=name)
                    ax.fill_betweenx([0, l+1], chosen_v - chosen_err, chosen_v + chosen_err, alpha=0.1, color='red')
                    ax.fill_betweenx([0, l+1], value - error, value + error, alpha=0.1, color='blue')
                    ax.set_xlabel("$a_t E$")
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    key = name.split('reorder_state')[1].split('.')[0]
                    figures.append((fig, key))
                    limit = 3
                    while True:
                        if all(abs(val - value) < limit * error for val in vals):
                            break
                        else:
                            limit *= 2
                        
                    ax.set_xlim(value - limit * error, value + limit * error)
                    print(f"Key: {key}")
                    #ax.set_ylabel("Option Index")
                    ax.set_yticks([])
                    ax.set_title(f" ord {key}")
                    #pdf.savefig(fig)
                    #plt.close(fig)
            sorted_figures = sorted(figures, key=lambda x: int(x[1]))
            for fig, key in sorted_figures:
                pdf.savefig(fig)
                plt.close(fig)
                    
            