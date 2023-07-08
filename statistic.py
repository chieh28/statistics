import pandas as pd
import csv

#function to calculate mean
def calculate_mean(input):
    sum = 0
    for i in input:
        sum += i
    mean = sum / len(input)
    return round(mean, 2)

#function to calculate variance
def calculate_var(input):
    mean = calculate_mean(input)
    sum = 0
    for i in input:
        sum += (i - mean) ** 2
    var = sum / (len(input) - 1)
    return round(var, 2)

#function to calculate standard deviation
def calculate_std(input):
    var = calculate_var(input)
    std = var ** (1/2)
    return round(std, 2)

#function to calculat skewness
def calculate_skewness(input):
    mean = calculate_mean(input)
    std = calculate_std(input)

    sum = 0
    for i in input:
        sum += (i - mean) ** 3
    m = sum / (len(input) - 1)
    skewness = m / (std ** 3)
    return round(skewness, 2)

#function to calculate kurtosis
def calculate_kurtosis(input):
    mean = calculate_mean(input)
    std = calculate_std(input)

    sum = 0
    for i in input:
        sum += (i - mean) ** 4
    m = sum / (len(input) - 1)
    kurtosis = m / (std ** 4)
    return round(kurtosis - 3, 2)

#function to calculate median
def calculate_median(input):
    input.sort()
    if len(input) % 2 != 0:
        return round(input[len(input) // 2 + 1], 2)
    else:
        return round((input[len(input) // 2] + input[len(input) // 2 + 1]) / 2, 2)
    
#function to calculate Q1
def calculate_Q1(input):
    input.sort()

    if len(input) % 4 != 0:
        return round(input[len(input) // 4 + 1], 2)
    else:
        return round((input[len(input) // 4] + input[len(input) // 4 + 1]) / 2, 2)

#function to calculate Q3
def calculate_Q3(input):
    input.sort()

    if 3 * (len(input)) % 4 != 0:
        return round(input[3 * (len(input)) // 4 + 1], 2)
    else:
        return round((input[3 * (len(input)) // 4] + input[3 * (len(input)) // 4 + 1]) / 2, 2)

#function to calculate IQR
def calculate_IQR(input):
    Q1 = calculate_Q1(input)
    Q3 = calculate_Q3(input)
    return round(Q3 - Q1, 2)

#function to calculate MAD
# def calculate_MAD(input):
#     Q2 = calculate_quartiles(input, 50)
#     sum = 0
#     for i in input:
#         sum += abs(i - Q2)
#     MAD = sum / len(input)
#     return MAD

#function to calculate CV
def calculate_CV(input):
    std = calculate_std(input)
    mean = calculate_mean(input)
    return round(std / mean, 2)

def prepare_list(f_data):
    title = [" "] + list(f_data.head(0))

    sta_val_dic = {
        "mean" : [calculate_mean, ["mean"]],
        "var" : [calculate_var, ["variance"]],
        "std" : [calculate_std, ["standard deviation"]],
        "skewness" : [calculate_skewness, ["skewness"]],
        "kurtosis" : [calculate_kurtosis, ["kurtosis"]],
        "Q1" : [calculate_Q1, ["Q1"]],
        "median" : [calculate_median, ["median(Q2)"]],
        "Q3" : [calculate_Q3, ["Q3"]],
        "IQR" : [calculate_IQR, ["IQR"]],
        "CV" : [calculate_CV, ["CV"]]
    }

    def creat_lists(title, sta_val, function_name):
        sta_val_dic[sta_val][1].append(str(function_name(list(f_data[s]))))


    for s in title:
        if s == " ":
            continue

        for sta_val in sta_val_dic.keys():
            creat_lists(s, sta_val, sta_val_dic[sta_val][0])
        
    all_list = [title]
    for sta_val in sta_val_dic.keys():
        all_list.append(sta_val_dic[sta_val][1])

    return all_list

def all_title(f_data):
    return list(f_data.head(0))