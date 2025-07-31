import os
def load_mass_xml(path,path_output, model_avg=False):
    path_output_f = f"{path_output}"
    if not os.path.exists(path_output_f):
        os.makedirs(path_output_f)
    
    with open(f"{path}/energies.xml", 'r') as file:
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