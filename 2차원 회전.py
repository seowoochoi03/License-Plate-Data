import os
import cv2
import random
import numpy as np
import imutils

file_list = os.listdir('C:\\Users\\pc\\OneDrive\\문서\\인공지능\\가상 번호판 PNG 파일') #가상 번호판 파일의 이름을 리스트로 옮김

file_name = []
for file in file_list:
    n_word = file[0:-4] #이름만 옮겨지는 것이 아니기에 (.png 와 같은 확장자가 따라옴) 번호판 문자열만 슬라이싱해주기
    file_name.append(n_word)

for i in range(len(file_name)): #가상 번호판을 모두 2차원 회전해줄 것이기 때문에
    img_array = np.fromfile('C:\\Users\\pc\\OneDrive\\문서\\인공지능\\가상 번호판 PNG 파일\\'+file_list[i], np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR) //imread와 같은 역할
    height, width, channel = img.shape #높이, 넓이, 채널(색상 정보)
    a = random.randint(-60,60) #2차원 회전을 위한 각도를 -60에서 60 사이에 수 랜덤 선택
    test_rol = cv2.getRotationMatrix2D((width/2, height/2), a, 1) #이미지 중심, 각도
    test_new = imutils.rotate_bound(img,a) #이미지 회전
    #cv2.imshow("Rotated (Correct)", test_new) 만약 윈도우 창을 통해 미리보고 싶다면 입력하기
    #cv2.waitKey(0)
    file_name[i] = file_name[i] + "_" + str(i)
    cv2.imwrite(file_name[i]+'.png', test_new) #저장
