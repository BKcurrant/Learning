# -*- coding=GBK -*-
import cv2 as cv
import numpy as np


# ���ͼƬ����
def get_image_info(image):  # ����һ�����������ͼƬ��һЩ����
    print(type(image))  # ��ʾͼƬ���� numpy���͵�����
    print(image.shape)
    '''ͼ������shape���Ա�ʾͼ��Ĵ�С��shape�᷵��tupleԪ�飬
          ��һ��Ԫ�ر�ʾ�����������ڶ���Ԫ���ʾ����������
          ������Ԫ����3����ʾ����ֵ�ɹ����ԭɫ���'''
    print(image.size)  # ͼ���С
    print(image.dtype)  # ͼ������
    pixel_data = np.array(image)
    print(pixel_data)  # ͼƬ����


src = cv.imread("C:/bg.jpg")
cv.namedWindow("1", cv.WINDOW_NORMAL)
cv.imshow("1", src)
get_image_info(src)
cv.imwrite("D:/2.jpg", src)  # ͼƬ���Ϊ����Ҫ�浽c�̣�ҪȨ�޵�
cv.waitKey(0)
cv.destroyAllWindows()

