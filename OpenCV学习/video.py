# -*- coding=GBK -*-
import cv2 as cv


# ������ͷ��ȡͼƬ
def video_demo():
    capture = cv.VideoCapture(0)  # ������ͷ��0��������豸id������ж������ͷ����������������ֵ
    while True:
        ret, frame = capture.read()
        '''��ȡ����ͷ,���ܷ���������������һ��������bool�͵�ret����ֵΪTrue��False��
        ������û�ж���ͼƬ���ڶ���������frame���ǵ�ǰ��ȡһ֡��ͼƬ'''
        frame = cv.flip(frame, 1)  # ��ת 0:���µߵ� ����0ˮƽ�ߵ�   С��180��ת
        cv.imshow("video", frame)
        c = cv.waitKey(40)
        if c == 27:
            break


video_demo()
cv.destroyAllWindows()


