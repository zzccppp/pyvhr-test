from pyVHR.analysis.pipeline import Pipeline
import matplotlib.pyplot as plt

import matplotlib
from my_pipeline import MyPipeline
import numpy as np

matplotlib.use("WebAgg")

video_path = ["cpi/cpi_resting/cv_camera_sensor_stream_handler.avi",
				"cpi/cpi_gym/cv_camera_sensor_stream_handler.avi",
              "my_video/VID_20220121_192203.mp4",
              "my_video/VID_20220121_192236.mp4",
              "my_video/VID_20220122_100738.mp4",]

pipe = MyPipeline()
time, BPM, uncertainty, bvps = pipe.run_on_video(video_path[3], cuda=True, roi_approach="patches", roi_method="faceparsing")

# np.save("my_video_.mat", bvps)

plt.figure()
plt.plot(time, BPM)
plt.fill_between(time, BPM-uncertainty, BPM+uncertainty, alpha=0.2)
plt.show()