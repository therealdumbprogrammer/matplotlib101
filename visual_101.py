import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

#Line plot with matplotlib
def lineplot():
    plt.plot(df['PassengerId'], df['Fare'])
    plt.title("Fare vs Passenger")
    plt.xlabel('Passenger ID')
    plt.ylabel('Fare')
    plt.show() 


#Histogram with Seaborn
def hisogram():
    sns.histplot(data=df, x='Age', bins=20)
    plt.title("Age histogram")
    plt.show()

#Scatter Plot with Matplotlib
def scatterPlot():
    plt.scatter(df['Age'], df['Fare'])
    plt.title("Age vs Fare")
    plt.xlabel('Age')
    plt.ylabel('Fare')
    plt.show()

#Box Plot with Seaborn
def boxplot():
    sns.boxplot(data=df, x='Pclass', y='Age')
    sns.set_style('whitegrid')
    plt.title('Age Distribution by Passenger Class')
    plt.show()

lineplot()
hisogram()
scatterPlot()
boxplot()