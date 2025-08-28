import numpy as np
import imageio.v2 as imageio

# Create a 200x200 green square
data = np.zeros((200, 200, 3), dtype=np.uint8)
data[:] = [0, 255, 0]  # RGB green

imageio.imwrite("green.png", data)
