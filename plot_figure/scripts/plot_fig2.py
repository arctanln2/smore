import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

df = pd.read_csv("./data/fig2/deg_data.csv")

x_labels = ["resnet", 'vgg', 'mobilenet', "bert", "deepfm", 'segnet','roberta','deepvit']
y_labels = ["deepfm", "vgg", "roberta"]

train_deg_dict = {}
infer_deg_dict = {}

for index, row in df.iterrows():
    train_model = row['train_model']
    infer_model = row['infer_model']
    train_deg = row['train_deg']
    infer_deg = row['infer_deg']
    k = f"{train_model}_{infer_model}"
    train_deg_dict[k] = train_deg
    infer_deg_dict[k] = infer_deg


data1 = np.random.rand(len(y_labels), len(x_labels))
data2 = np.random.rand(len(y_labels), len(x_labels))

for i, train_model in enumerate(y_labels):
    for j, infer_model in enumerate(x_labels):
        k = f"{train_model}_{infer_model}"
        data1[i][j]=train_deg_dict[k]
        data2[i][j]=infer_deg_dict[k]


fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6, 4.5))

x_labels = ["ResNet", 'VGG', 'MobileNet', "Bert", "Deepfm", 'SegNet','RoBERTa','DeepViT']
y_labels = ["DeepFM", "VGG", "RoBERTa"]

sns.heatmap(data1, ax=axes[0], annot=True, fmt=".1f", cmap="YlGnBu",
            xticklabels=[], yticklabels=y_labels)
axes[0].set_title('Training Workload Degradation')

sns.heatmap(data2, ax=axes[1], annot=True, fmt=".1f", cmap="YlGnBu",
            xticklabels=x_labels, yticklabels=y_labels)
axes[1].set_title('Inference Workload Degradation')
axes[1].set_xticklabels(x_labels, rotation=30, ha='right') 

plt.tight_layout()  
plt.savefig("imgs/fig2.pdf")
