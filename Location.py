from Image import Image
import cv2
if __name__=="__main__":
    img=Image(cv2.imread("1.jpeg"))
    cv2.imshow("res",img.pos_img)
    cv2.waitKey(0)
