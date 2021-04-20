#Read and Image and Split the Channels
import cv2
import numpy as np
###############################################
# Reading the Image
imageData = cv2.imread("../../Images/lenna-RGB.tif")
cv2.imshow("Beautiful Lena", imageData)
###############################################
print("Image Size = ", imageData.shape) #Know the shape of the Image
#exit(0)
# Channel Splitting

#print(imageData[1,1,1])
#exit(0)
blueData = imageData[:, :, 0]
greenData = imageData[:, :, 1]
redData = imageData[:, :, 2]

print(blueData)
print(greenData)
print(redData)
#exit(0)

# Display all channels individually
cv2.imshow('BlueData', blueData)
cv2.imshow('GreenData', greenData)
cv2.imshow('RedData', redData)
#exit(0)
################################################
cv2.waitKey(0)
cv2.destroyAllWindows()
