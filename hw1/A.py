import numpy as np
import imageio.v2 as imageio

# Tasks:
    # 1 (15%) A grayscale image of constant intensity 104
    # 2 (15%) A grayscale image with alternating black and white vertical stripes, each of which is 4 pixels wide 
    # 3 (15%) A grayscale image with a ramp intensity distribution, described by I(x, y) = x/2
    # 4 (15%) A grayscale image with a Gaussian intensity distribution centered at (128, 128), described by [formula]
    # 5 (15%) A color image where the upper left quadrant is yellow, the lower left quadrant is red, the upper right quadrant is green, and the lower right quadrant is black
    # 6 (15%) For questions 1-5, create a document consisting of your inputs, outputs, your observations, problems you have faced, solutions indicating how you have overcome the problems, and other points that you think are necessary.
    # 7 (10%) For questions 1-5, create a video describing your solutions


# Solutions:

    ### 1
#let`s create variables that will indicate the dimensions of our figure(matrix)
height, width = 1000, 1000 # so, it could be mtable in future if needed(good code)

#Then we will use those dimnesions in Matrix:
Matrix = np.full(   (height, width), #matrix dimensions
                 104, #every number in Matrix is equal to 104
                 dtype=np.uint8) #We use uint 8, since it is 8-bit data, range is 0, 255

#And finally we a special library to create an imgae from a Matrix data
imageio.imwrite("1_Gray_104.png", Matrix)
