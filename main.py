import argparse
from processfile import read_file, get_file_name, creat_csv_file, creat_file, move_file
from statistic import prepare_list, all_title
from visualization import creat_boxplot

def __main__():

    #initialize parser
    parser = argparse.ArgumentParser()

    #add optional argument
    parser.add_argument("-f", type = str, default = "")

    #read argument from command line
    args = parser.parse_args()
    import_file = args.f

    #creat folder for the data
    filename = get_file_name(import_file)
    creat_file(filename + "/")
    
    #creat statistical csv file
    f_data = read_file(import_file)
    all_list = prepare_list(f_data)   
    creat_csv_file(filename, all_list)

    for i in all_title(f_data):
        #creat box plot
        plot = creat_boxplot(f_data, i)

        #move png to the folder
        move_file(plot, filename + "/")

    #move original file to the folder
    move_file(import_file, filename + "/")

    #move csv file to the folder
    move_file(filename + ".csv", filename + "/")


__main__()