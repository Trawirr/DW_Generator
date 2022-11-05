import random
import time

def generate_data(save_to, mode="w", num=1, *args):
    data = []
    with open(save_to, mode) as f:
        for i in range(num):
            row = []
            for arg in args:
                if isinstance(arg, list):
                    full_option = ''
                    for option in arg:
                        with open(f'options/{option}.txt', 'r') as option_file:
                            options = option_file.readlines()
                            full_option = ' '.join([full_option, random.choice(options).strip()])
                    row.append(full_option.strip())
                else:
                    with open(f'options/{arg}.txt', 'r') as option_file:
                        options = option_file.readlines()
                        row.append(random.choice(options).strip())
            data.append(', '.join(row) + "\n")
        f.writelines(data)
    return data

# Generowanie T0-T1
generate_data("employees.txt", 'w', 3, ["first_name", "last_name"])

# Generowanie T1-T2
generate_data("employees.txt", 'a', 1, ["first_name", "last_name"])
