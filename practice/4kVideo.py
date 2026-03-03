import cv2
import numpy as np

# Define parameters
width, height = 3840, 2160  # 4K Resolution
fps = 30
duration = 1800  # 30 minutes in seconds
change_interval = 2  # Change color every 5 seconds

# Define colors (BGR format)
colors = [
    (0, 0, 255),   # Red
    (0, 255, 0),   # Green
    (255, 0, 0),   # Blue
    (0, 255, 255), # Yellow
    (255, 255, 0), # Cyan
    (255, 0, 255), # Magenta
    (128, 0, 128), # Purple
    (255, 165, 0), # Orange
    (0, 128, 128), # Teal
    (128, 128, 0), # Olive
    (75, 0, 130),  # Indigo
    (139, 69, 19), # Brown
    (192, 192, 192), # Silver
    (255, 215, 0), # Gold
]

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('color_test_4k_2.mp4', fourcc, fps, (width, height))

for i in range(duration // change_interval):
    frame = np.full((height, width, 3), colors[i % len(colors)], dtype=np.uint8)
    for _ in range(fps * change_interval):
        out.write(frame)

out.release()
print("4K color-changing video generated successfully!")