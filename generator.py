import random
import string
import time
import pandas as pd
import os.path as path
from datetime import date


def create_column_name(arg):
    if isinstance(arg, list):
        return '_'.join(arg)
    return arg


def create_field(arg):
    if isinstance(arg, list):
        full_option = ''
        for option in arg:
            with open(f'options/{option}.txt', 'r') as option_file:
                options = option_file.readlines()
                full_option = ' '.join([full_option, random.choice(options).strip()])
        return full_option.strip()
    else:
        if arg == "id":
            return ''.join(random.choices(string.ascii_lowercase, k=10))
        elif arg == "login":
            return ''.join(random.choices(string.ascii_lowercase, k=10))
        elif arg == "date":
            return date.today().replace(year=2021, month=random.randint(1,12), day=random.randint(1, 28))
        elif arg == "price":
            return random.randint(200, 1000)
        else:
            with open(f'options/{arg}.txt', 'r') as option_file:
                options = option_file.readlines()
                return random.choice(options).strip()

def generate_data(copy_from, save_to, pk=None, mode="a+", num=1, *args):
    column_names = [create_column_name(arg) for arg in args]
    if path.exists(copy_from):
        df = pd.read_csv(copy_from)
    else:
        df = pd.DataFrame(columns=column_names)
    data = []
    data_to_append = {c:[] for c in column_names}
    for i in range(num):
        row = []
        for arg in args:
            val = create_field(arg)
            if pk == arg:
                pks = df[create_column_name(arg)]
                while val in list(pks):
                    val = create_field(arg)
            row.append(val)
        df.loc[len(df)] = row
    df.to_csv(save_to, index=False)
    pks = list(df[create_column_name(pk)])
    with open(f"options/{save_to.replace('.csv', '')}.txt", 'w') as f:
        for p in pks:
            f.write(f"{p}\n")
    return data


if __name__ == "__main__":
    # Generowanie T0-T1
    generate_data("employees.csv", "employees.csv", ["first_name", "last_name"], 'a+', 5, ["first_name", "last_name"], 'last_name')
    generate_data("employees2.csv", "employees2.csv", "first_name", 'a+', 2, "first_name", "employees")
    generate_data("players.csv", "players.csv", "id", 'a+', 50, "id", "date")
    generate_data("players2.csv", "players2.csv", "id", 'a+', 2, "id", "date", "quality")
    # Generowanie T1-T2
    generate_data("employees.csv", "employees.csv", ["first_name", "last_name"], 'a+', 3, ["first_name", "last_name"], 'last_name')