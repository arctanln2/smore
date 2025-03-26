
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/fig15/data.csv")

x_values = data['x_values']
pred_y = data['pred_y']
real_y = data['real_y']
train_split = 735

plt.figure(figsize=(6, 3))

plt.plot(x_values, pred_y,  label="prediction")

plt.plot(x_values, real_y,  label="real",alpha = 0.5)

plt.axvline(x=train_split, color="g", linestyle="--", label="Train/Test Split")

plt.xlabel("Time (minutes)")  
plt.ylabel("Requests")  
plt.legend(loc="best")
plt.tight_layout()

plt.savefig(f"imgs/fig15.pdf")