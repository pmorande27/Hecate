import os
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