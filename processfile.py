import pandas as pd
import csv
import shutil
import os


def read_file(file):
    f_data = pd.read_excel(file)

    return f_data

def get_file_name(file):
    filename = file.split('.')[0]
    
    return filename

def creat_csv_file(filename, all_list):
    with open(filename + ".csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        
        for i in range(len(all_list)):
            writer.writerow(all_list[i])

def confirm_path(name):
    filepath = ''
    split_name = name.split('/')

    for i in range(len(split_name) - 1):
        creat_file(split_name[i])
        filepath += split_name[i] + '/'

    return filepath 
        
def creat_file(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(file, path):
    shutil.move(file, path + file)

    return path + file
