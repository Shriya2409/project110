import statistics
import pandas as pd
import csv
import random
import plotly.figure_factory as ff

df=pd.read_csv("temperature.csv")
data=df["temp"].tolist()

mean=statistics.mean(data)
std=statistics.stdev(data)
print(mean)
print(std)
fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

data_set=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(value)
mean2=statistics.mean(data_set)
std2=statistics.stdev(data_set)
print(mean2)
print(std2)

def setup():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means=random_set(100)
        mean_list.append(set_of_means)
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
    sampling_mean=statistics.mean(mean_list)
    print(sampling_mean)
    std=statistics.stdev(mean_list)
    print(std)

def random_set(counter):
    dataSet=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data))
        value=data[random_index] 
        dataSet.append(value)
    mean=statistics.mean(dataSet)    
    return mean
      
setup()      