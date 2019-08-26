import cv2 as cv

src = cv.imread("C:/bg.jpg")
cv.namedWindow("1", 0)
cv.imshow("1", src)
cv.waitKey(0)
cv.destroyAllWindows()

