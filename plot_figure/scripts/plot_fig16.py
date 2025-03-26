import matplotlib.pyplot as plt
import numpy as np

parameters = {
    'font.family': 'sans-serif',
    'font.sans-serif': 'Arial'
}
plt.rcParams.update(parameters)


functions = ['Function 1', 'Function 2']
labels = ['LS-LSTM', 'LSTH', 'HHP']
cold_start_rate = np.array([[3, 18, 19], [8, 7, 9]]) 
resource_waste = np.array([[26, 16, 16], [32, 75, 69]])

n_groups = len(functions)
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

fig, ax = plt.subplots(1, 2, figsize=(6, 3))
        
"""Cold Start Rate"""
for i in range(3):
    bars=ax[0].bar(index + i*bar_width, cold_start_rate[:, i], bar_width, alpha=opacity, label=f'{labels[i]}', edgecolor='black')

"""Resource Waste"""
for i in range(3):
    bars=ax[1].bar(index + i*bar_width, resource_waste[:, i], bar_width, alpha=opacity, label=f'{labels[i]}',edgecolor='black')

ax[0].set_ylabel('Cold Start Rate')
ax[0].set_xticks(index + bar_width)
ax[0].set_xticklabels(functions)

ax[1].set_ylabel('Resource Waste')
ax[1].set_xticks(index + bar_width)
ax[1].set_xticklabels(functions)
ax[1].legend()

plt.tight_layout()
plt.savefig("imgs/fig16.pdf", bbox_inches='tight')

