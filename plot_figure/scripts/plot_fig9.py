#coding=gbk
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/fig9/data.csv")

bar_width = 0.3

parameters = {
    'xtick.labelsize': 7,
    'figure.figsize': [3.0, 3.0],
}
plt.rcParams.update(parameters)

bar = plt.bar(data['name'], data['degree'], bar_width, edgecolor='black')

plt.axis([None, None , 0, 1.05])
plt.ylabel('Percentage of Requests Admitted (%)')

index = range(len(data['name']))
plt.xticks([i for i in index], data['name'],rotation=30, ha='right') 

plt.ylim(0,1.1)
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.2f' % height, ha='center', va='bottom' if height > 0 else 'top')

plt.savefig("imgs/fig9.pdf", bbox_inches='tight')

