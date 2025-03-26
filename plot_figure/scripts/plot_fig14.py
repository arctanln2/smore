import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/fig14/data.csv")
data = data.set_index('name') 

bar_width = 0.2
group_gap = 0.4  
bar_gap = 0       

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  

parameters = {
    'figure.figsize': [6.0, 3.0],
}
plt.rcParams.update(parameters)

fig, ax = plt.subplots()

index = range(len(data.index))
n_bars = len(data.columns)  # 柱子的数量
group_width = bar_width * n_bars + bar_gap * (n_bars - 1)

xticks = [i + group_width / 8 * 3 for i in index]

for i, column in enumerate(data.columns):
    x_positions = [j + i * (bar_width + bar_gap) for j in index]
    bars = ax.bar(x_positions, data[column], bar_width, label=column, edgecolor='black', color=colors[i])

    for bar in bars:
        height = bar.get_height()
        if height < 10:
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, '%.1f' % height,
                    ha='center', va='bottom' if height >= 0 else 'top')
        else:
            ax.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % height,
                    ha='center', va='bottom' if height >= 0 else 'top')
        

ax.set_ylabel('Value')  
ax.set_xticks(xticks)
ax.set_xticklabels(data.index, rotation=0)
ax.legend()
ax.axhline(0, color='gray', linestyle='--')
ax.set_ylim(0, 75) 

plt.tight_layout()
plt.savefig("imgs/fig14.pdf", bbox_inches='tight')


