import pandas as pd
from processfile import read_csv_file, creat_csv_file


def clean_zero(data, col_name):
    return data[data[col_name] > 0].reset_index()

def classify(data, col_name, standard):
    df = pd.DataFrame(data.to_dict())
    df = df.reindex(columns = [f"new_{col_name}", "Outcome"]).to_dict()
    
    fill_value = data[col_name].tolist()
    for i in range(len(fill_value)):
        if fill_value[i] >= standard:
            fill_value[i] = 1
        else:
            fill_value[i] = 0

    df[f"new_{col_name}"] = pd.Series(fill_value)
    df = pd.DataFrame.from_dict(df)
    return df
    
# def filter_table(orignal_data, col_name: str, filter_value: int = None):
#     if filter_value == None:
#         pass
#     else:
#         return orignal_data[orignal_data[col_name] > filter_value]


def count_corss_number(data, conditions: list):
    column_names = data.columns.values.tolist()

    count = sum((data[column_names[0]] == conditions[0]) & (data[column_names[1]] == conditions[1]))
    return count

def count_total_number(data, col_name, condition):
    
    count = sum(data[col_name] == condition)
    return count

def __main__():
    import_file = "diabetes.csv"
    f_data = read_csv_file(import_file)

    # import json
    # with open('filter.json', newline='') as jsonfile:
    #     filters = json.load(jsonfile)

    # for k, v in filters.items():
    #     converted_f_data = filter_table(converted_f_data, k, v)
    #     print(f"filted data shape: {converted_f_data.values.shape}")

    col_name = "BloodPressure"
    standard = 85

    clean_data = clean_zero(f_data, col_name)
    classify_data = classify(clean_data, col_name, standard)



    cross_tab_list = [["", "NO Diabetes", "Diabetes", "Total"], 
                [col_name + " lower than " + str(standard), count_corss_number(classify_data, [0, 0]), count_corss_number(classify_data, [0, 1]), count_total_number(classify_data, f"new_{col_name}", 0)],
                [col_name + " higher than " + str(standard), count_corss_number(classify_data, [1, 0]), count_corss_number(classify_data, [1, 1]), count_total_number(classify_data, f"new_{col_name}", 1)],
                ["Total", count_total_number(classify_data, "Outcome", 0), count_total_number(classify_data, "Outcome", 1), ""]]
    
    creat_csv_file("Cross Tabulatin", cross_tab_list)

__main__()
