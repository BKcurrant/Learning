# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# 输出图片属性
def get_image_info(image):  # 定义一个函数来输出图片的一些属性
    print(type(image))  # 显示图片类型 numpy类型的数组
    print(image.shape)
    '''图像矩阵的shape属性表示图像的大小，shape会返回tuple元组，
          第一个元素表示矩阵行数，第二个元组表示矩阵列数，
          第三个元素是3，表示像素值由光的三原色组成'''
    print(image.size)  # 图像大小
    print(image.dtype)  # 图像类型
    pixel_data = np.array(image)
    print(pixel_data)  # 图片矩阵


src = cv.imread("C:/bg.jpg")
cv.namedWindow("1", cv.WINDOW_NORMAL)
cv.imshow("1", src)
get_image_info(src)
cv.imwrite("D:/2.jpg", src)  # 图片另存为，不要存到c盘，要权限的
cv.waitKey(0)
cv.destroyAllWindows()

