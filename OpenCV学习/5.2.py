# -*- coding=GBK -*-
import cv2 as cv


# �߼����㣺���ǵĲ���
def luo_image(src11, src22):
    src = cv.bitwise_and(src11, src22)  # �� ����ͼƬͬһλ�õ�ɫ������ֵ����Ϊ��ĲŻ������
    cv.imshow("��", src)
    src = cv.bitwise_or(src11, src22)  # �� ����ͼƬͬһλ�õ�ɫ������ֵ��ȫΪ��ĲŻ������
    cv.imshow("��", src)
    src = cv.bitwise_not(src11)  # �� ��һ��ͼƬ����  ȡ��
    cv.imshow("��", src)
    src = cv.bitwise_xor(src11, src22)  # ��� ����ͼƬͬһλ�õ�ɫ������ֵ��һ��Ϊ�㣬��һ����Ϊ��Ż����
    cv.imshow("���", src)


src1 = cv.imread("C:/01.jpg")
src2 = cv.imread("C:/02.jpg")
cv.imshow("ԭ��1", src1)
cv.imshow("ԭ��2", src2)
luo_image(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
