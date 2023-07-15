from processfile import read_csv_file

def __main__():
    import_file = "diabetes.csv"
    f_data = read_csv_file(import_file)

    column = "BloodPressure"
    print(sum(f_data[column] >= 85))
__main__()


def classify(input, standard):
    pass

def clean_zero(data):
    pass