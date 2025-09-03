import numpy as np
import imageio.v2 as imageio

# Tasks:
    # 1 (15%) A grayscale image of constant intensity 104
    # 2 (15%) A grayscale image with alternating black and white vertical stripes, each of which is 4 pixels wide 
    # 3 (15%) A grayscale image with a ramp intensity distribution, described by I(x, y) = x/2
    # 5 (15%) A grayscale image with a Gaussian intensity distribution centered at (128, 128), described by [formula]
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
imageio.imwrite("A1_Gray_104.png", Matrix)


    ### 2
#We already created an Image for the 1st task before, and we can still use the data from previous task
#We will use the same MAtrix, but replace numbers in it

for x in range(width): #here we take every column
    if (x // 4) % 2 == 0: #divide column number by 4 without remainder, and check if it is odd or even
        Matrix[:, x] = 0 #Paint column X in Black. 0 Min intensity in 8-bit
    else:
        Matrix[:, x] = 255 #Paint column in White. 255 Max intensity in 8-bit

#After rewriting data in Matrix, We create image:
imageio.imwrite("A2_Stripes_BW.png", Matrix)


    ### 3
#We will reuse the same Matrix again:
for x in range(width):
    intensity = min(x // 2, 255)   # ramp expression
    Matrix[:, x] = intensity       # fill column with that intensity

# Save image
imageio.imwrite("A3_Ramp.png", Matrix)


    ### 4
#coordinate grids:                         
x, y = np.indices((width, height))

#Gaussian Expression:
I = 255 * np.exp( -( (x - 128)**2 + (y - 128)**2 ) / (200**2) ) #I values are float, not integer

Matrix = np.clip(I, 0, 255).astype(np.uint8)    #And wee need a mATRIX WITH INT IN 8BIT RANGE(0, 255)

imageio.imwrite("A4_Gaussian.png", Matrix)


    ### 5
# add one more dimension to our resuable Matrix:
Matrix = np.zeros( (height, width, 3), dtype=np.uint8) # also fill it with Zeros, so ot is empty Black for now.

Matrix[0:height//2, 0:width//2] = [255, 255, 0]    # Upper left Yellow = R + G + 0
Matrix[0:height//2, width//2:width] = [0, 255, 0]     #Upper Right Green = 0 + G + 0
Matrix[height//2:height, 0:width//2] = [255, 0, 0] # Lower Left Red = R + 0 + 0
    # Lower Right is already Black, There is no need to change anything in Matrix

#image
imageio.imwrite("A5_Quadrants.png", Matrix)

