import matplotlib.pyplot as plt

time = []
for i in range(1,61):
    time.append(i)

submission_list = [251, 200, 301, 101, 250, 150, 251, 99, 101, 201, 251, 151, 350, 201, 199, 200, 249, 49, 149, 199, 200, 200, 349, 149, 250, 200, 200, 301, 251, 151, 249, 201, 299, 199, 251, 149, 251, 301, 200, 201, 250, 151, 351, 150, 200, 201, 249, 50, 149, 199, 199, 200, 199, 50, 149, 101, 101, 200, 151, 51]
accept_list = [185, 142, 201, 49, 194, 128, 187, 59, 57, 147, 173, 131, 254, 143, 153, 152, 169, 29, 77, 155, 160, 158, 243, 125, 178, 162, 166, 213, 189, 125, 181, 153, 203, 151, 185, 133, 183, 197, 164, 147, 172, 133, 227, 120, 160, 165, 187, 30, 87, 153, 155, 146, 99, 20, 83, 65, 65, 98, 83, 29]

parameters = {
    'figure.figsize': [6.0, 3.0],
}
plt.rcParams.update(parameters)
plt.plot(time,submission_list,label="Job Submission",marker = 'o',markersize = 4,linestyle = '-')
plt.plot(time,accept_list, label="Job Admission",marker = 'o',markersize = 4,linestyle = 'dotted')

plt.axis([0, 60, 0, 400])
plt.ylabel('Number of Jobs')
plt.xlabel('Time (s)')

plt.legend()
plt.savefig(f"imgs/fig12.pdf", bbox_inches='tight')
