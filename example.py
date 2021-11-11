from re import L
import statistics
import random
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
fig=ff.create_distplot([data],["Reading Time"],show_hist=False)

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    showfig(meanlist)
setup()
def standardDeviation():
    meanlist=[]
    for i in range(0,1000):
        setofmeans=randomsetofmean(100)
        meanlist.append(setofmeans)
    standardDeviation=statistics.stdev(meanlist)
    print("Standard Deviation=",standardDeviation)

standardDeviation()
