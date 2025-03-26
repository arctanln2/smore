import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_line_from_csv(filename, ax, label='vgg', data_dir = 'data/fig1/training', point_start=0, point_end=600, interval=10):
    file_path = os.path.join(data_dir, filename + '.log')
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip()
        data = data.iloc[:point_end, :]
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data['timestamp'] = (data['timestamp'] - data['timestamp'].iloc[point_start]).dt.total_seconds()

        ax.plot(data['timestamp'][point_start:point_end:interval],
                 data["utilization.gpu [%]"][point_start:point_end:interval],
                 label=label)
    except Exception as e:
        print(f"Error processing file {filename}: {e}")

parameters = {
    'figure.figsize': [6, 3],
}
plt.rcParams.update(parameters)

fig, axes = plt.subplots(1, 2) 

infer_dict = {}
train_dict = {}
model_list = ["VGG", "MobileNet","DeepViT","ResNet","BERT","RoBERTa","DeepFM","SegNet"]

"""Training Part"""
data_dir = 'data/fig1/training'
filelist = os.listdir(data_dir)
filelist.sort()
for file in filelist:
    if not file.endswith('.log'):
        continue
    
    split_ans = file[:-4].split('_')
    label = f"{split_ans[-2]}"
    train_dict[label]=file

"""Inference Part"""
data_dir = 'data/fig1/inference'
filelist = os.listdir(data_dir)
filelist.sort()

for file in filelist:
    if not file.endswith('.log'):
        continue
    
    split_ans = file[:-4].split('_')
    label = f"{split_ans[-2]}"
    infer_dict[label]=file

for label in model_list:
    plot_line_from_csv(train_dict[label][:-4], axes[0], label, 'data/fig1/training')
    plot_line_from_csv(infer_dict[label][:-4], axes[1], label, 'data/fig1/inference')

axes[0].axis([0, 60, 0, 100])
axes[0].set_ylabel('GPU Util (%)')
axes[0].set_xlabel('Time (s)')
axes[0].set_title('Training')

axes[1].axis([0, 60, 0, 100])
axes[1].set_xlabel('Time (s)')
axes[1].set_title('Inference')
axes[1].legend(bbox_to_anchor=(1, 1), loc='upper left')
axes[1].set_yticks([])  

plt.tight_layout()  
plt.savefig("imgs/fig1.pdf", bbox_inches='tight')
