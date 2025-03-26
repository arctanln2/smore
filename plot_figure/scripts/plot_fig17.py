import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/fig17/data.csv")

bar_width = 0.4  

parameters = {
    'figure.figsize': [6.0, 3.0],
}
plt.rcParams.update(parameters)

index = range(len(data['name']))
bar1 = plt.bar([i for i in index], data['low load mode'], bar_width, label='Low load mode', edgecolor='black')
bar2 = plt.bar([i + bar_width for i in index], data['high load mode'], bar_width, label='High load mode', edgecolor='black')

plt.axhline(0, color='gray', linestyle='--')
plt.ylabel('Scheduling time per 1000 requests (ms)')
plt.xticks(rotation=0) 

plt.xticks([i + bar_width / 2 for i in index], data['name']) 

plt.legend()
plt.ylim(0, 900)

for rect in bar1 + bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.0f' % height, ha='center', va='bottom' if height > 0 else 'top')

plt.savefig("imgs/fig17.pdf", bbox_inches='tight')

