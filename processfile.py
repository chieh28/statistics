import pandas as pd
import csv

def read_file(file):
    f_data = pd.read_excel(file)

    return f_data

def get_file_name(file):
    filename = ""
    for s in file:
        if s != ".":
            filename += s
        else:
            break
    
    return filename

def creat_csv_file(filename, all_list):
    with open(filename + ".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        for i in range(len(all_list)):
            writer.writerow(all_list[i])