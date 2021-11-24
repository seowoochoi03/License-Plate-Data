import cv2
import numpy as np

def plus(hpos,vpos):
    img_array2 = np.fromfile('C:\\Users\\pc\\OneDrive\\문서\\인공지능\\이미지 합성\\4-2.png',np.uint8)
    img2 = cv2.imdecode(img_array2, cv2.IMREAD_COLOR)
    img_array1 = np.fromfile('C:\\Users\\pc\\OneDrive\\문서\\인공지능\\이미지 합성\\1-1.png',np.uint8)
    img1 = cv2.imdecode(img_array1, cv2.IMREAD_COLOR)
    h, w, c = img2.shape
    roi = img1[vpos:vpos+h, hpos:hpos+w]#배경이미지 위에 차량을 넣을  영역
    mask = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)#차량을 흑백처리
    #이미지 이진화 : 배경은 검정. 글자는 흰색
    mask[mask[:]==255]=0
    mask[mask[:]>0]=255
    mask_inv = cv2.bitwise_not(mask) #mask반전 => 배경은 흰색. 글자는 검정
    car = cv2.bitwise_and(img2, img2, mask=mask)
    back = cv2.bitwise_and(roi, roi, mask=mask_inv)
    dst = cv2.add(car, back)
    img1[vpos:vpos+h, hpos:hpos+w] = dst
    cv2.imshow('img1', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("img2.png", img1)
    
plus(250,200) #x,y 값으로 차량 위치를 정함

// 참조 : https://cyberpunk.tistory.com/25 
