# Import libraries
import matplotlib.pyplot as plt
import numpy as np

def creat_boxplot(data, title):
    fig = plt.figure(figsize =(10, 7))

    # Adding title
    plt.title(f"{title} box plot")
    plt.xlabel(title)

    # Creating plot
    plt.boxplot(data[title])

    # show plot
    plt.savefig(f"{title} box plot.png")

    return f"{title} box plot.png"