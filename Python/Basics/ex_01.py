#An introduction to Open CV
import cv2

imageData = cv2.imread("../../Images/lenna-gray.tif")
cv2.imshow("Lenna, a benchmark Image", imageData)

cv2.waitKey(0)
cv2.destroyAllWindows()
