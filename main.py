import pandas as pd
import csv

filename = "number-of-deaths-by-risk-factor"
boston_data = pd.read_excel(f"{filename}.xlsx")

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
    
#function to calculate quartiles
def calculate_quartiles(input, p):
    input.sort()
    if p == 25:
        if len(input) % 4 != 0:
            return round(input[len(input) // 4 + 1], 2)
        else:
            return round((input[len(input) // 4] + input[len(input) // 4 + 1]) / 2, 2)
    elif p == 50:
        return round(calculate_median(input), 2)
    else:
        if 3 * (len(input)) % 4 != 0:
            return round(input[3 * (len(input)) // 4 + 1], 2)
        else:
            return round((input[3 * (len(input)) // 4] + input[3 * (len(input)) // 4 + 1]) / 2, 2)
        
#function to calculate IQR
def calculate_IQR(input):
    Q1 = calculate_quartiles(input, 25)
    Q3 = calculate_quartiles(input, 75)
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

title = [" "] + list(boston_data.head(0))
mean = ["mean"]
var = ["variance"]
std = ["standard deviation"]
skewness = ["skewness"]
kurtosis = ["kurtosis"]
Q1 = ["Q1"]
median = ["median(Q2)"]
Q3 = ["Q3"]
IQR = ["IQR"]
CV = ["CV"]

for s in title:
    if s == " ":
        continue
    mean.append(str(calculate_mean(list(boston_data[s]))))
    var.append(str(calculate_var(list(boston_data[s]))))
    std.append(str(calculate_std(list(boston_data[s]))))
    skewness.append(str(calculate_skewness(list(boston_data[s]))))
    kurtosis.append(str(calculate_kurtosis(list(boston_data[s]))))
    Q1.append(str(calculate_quartiles(list(boston_data[s]), 25)))
    median.append(str(calculate_median(list(boston_data[s]))))
    Q3.append(str(calculate_quartiles(list(boston_data[s]), 75)))
    IQR.append(str(calculate_IQR(list(boston_data[s]))))
    CV.append(str(calculate_CV(list(boston_data[s]))))

with open(f"{filename}.csv", "w", newline="") as csvfile :
    writer = csv.writer(csvfile)
    writer.writerow(title)
    writer.writerow(mean)
    writer.writerow(var)
    writer.writerow(std)
    writer.writerow(skewness)
    writer.writerow(kurtosis)
    writer.writerow(Q1)
    writer.writerow(median)
    writer.writerow(Q3)
    writer.writerow(IQR)
    writer.writerow(CV)