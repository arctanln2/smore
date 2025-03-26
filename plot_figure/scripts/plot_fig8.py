import matplotlib.pyplot as plt
import numpy as np

accept_list = [17, 15, 21, 4, 22, 13, 14, 8, 6, 15, 17, 12, 22, 17, 18, 15, 14, 3, 7, 15]
submission_list =    [25, 20, 30, 10, 25, 15, 25, 10, 10, 20, 25, 15, 35, 20, 20, 20, 25, 5, 15, 20]

time = np.arange(len(submission_list))

parameters = {
    'legend.fontsize': 9,
    'figure.figsize': [3.0, 3.0],
}
plt.rcParams.update(parameters)

plt.plot(time,submission_list,label="Job Submission",marker = 'o',markersize = 4,linestyle = '-')
plt.plot(time,accept_list, label="Job Admission",marker = 'o',markersize = 4,linestyle = 'dotted')

plt.axis([-1, 20, 0, 40])
plt.ylabel('Number of Jobs')
plt.xlabel('Time (s)')
plt.legend()

plt.savefig(f"imgs/fig8.pdf", bbox_inches='tight')
