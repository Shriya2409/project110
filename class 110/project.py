import statistics
import pandas as pd
import csv
import random
import plotly.figure_factory as ff

df=pd.read_csv("data.csv")
data=df["average"].tolist()

population_mean=statistics.mean(data)
population_deviation=statistics.stdev(data)
print(population_mean)
print(population_deviation)

def random_set(counter):
    data_set=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)    
    return mean

def setup():
    mean_list=[]
    for i in range(0, 100):
        set_of_means=random_set(30)
        mean_list.append(set_of_means)
    df=mean_list
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.show()
    sampling_mean=statistics.mean(mean_list)
    print(sampling_mean)
    std=statistics.stdev(mean_list)
    print(std) 

setup()