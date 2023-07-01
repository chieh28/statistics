import argparse
from processfile import read_file, get_file_name, creat_csv_file
from statistic import prepare_list

def __main__():

    #initialize parser
    parser = argparse.ArgumentParser()

    #add optional argument
    parser.add_argument("-f", type = str, default = "")

    #read argument from command line
    args = parser.parse_args()
    import_file = args.f
    
    f_data = read_file(import_file)
    filename = get_file_name(import_file)
    all_list = prepare_list(f_data)   
    creat_csv_file(filename, all_list)

__main__()