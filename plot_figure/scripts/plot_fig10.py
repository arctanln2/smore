import matplotlib.pyplot as plt
import pandas as pd

y1 = pd.read_csv("data/fig10/colo_util.csv")['utilization']
y2 = pd.read_csv("data/fig10/solo_util.csv")['utilization']
t = pd.read_csv("data/fig10/colo_util.csv")['time']

parameters = {
    'figure.figsize': [3.0, 3.0],
}
plt.rcParams.update(parameters)

plt.plot(t,y1,label = "Co-location")
plt.plot(t,y2,label = "Solo-run")

plt.axis([0, 20, 0, 100])
plt.ylabel('GPU Util (%)')
plt.xlabel('Time (s)')

plt.legend()
plt.savefig(f"imgs/fig10.pdf", bbox_inches='tight')