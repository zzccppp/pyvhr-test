import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("WebAgg")

# bvps = np.load("bvps.mat.npy")
# bvps = np.load("bvps_gym.mat.npy")
bvps = np.load("my_video_1.mat.npy")
# bvps = np.load("my_video_.mat.npy")

line = bvps[0]

plt.scatter([0] * line.shape[0], line[:,0], s=1)
plt.figure()

stds = []
avgs = []
time = []

time_range = 6
stride = 1
fps = 25

start_frame = int((time_range - stride) / 2 * fps)
end_frame = int((time_range + stride) / 2 * fps)
now_time = (time_range - stride) / 2

for i in range(bvps.shape[0]):
    for j in range(start_frame,end_frame):
        stds.append(np.std(bvps[i][:,j]))
        avgs.append(np.average(bvps[i][:,j]))

plt.plot(np.linspace(now_time, now_time + bvps.shape[0] * stride, len(stds)),stds)
plt.figure()
plt.plot(np.linspace(now_time, now_time + bvps.shape[0] * stride, len(stds)),avgs)
plt.show()