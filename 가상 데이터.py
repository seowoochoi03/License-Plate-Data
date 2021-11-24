차량 번호판에 대한 규정을 모두 참고한 것이 아님.

import numpy as np
import random
from PIL import Image,ImageDraw,ImageFont

list_A = []
number = '0123456789' 
for num in number:
    list_A.append(num) #번호판의 숫자를 담은 리스트
list_B = []
korean = '가나다라마바사아자하거너더러머버서어저허구누도로부수우주호고노더소오지두'
for kor in korean:
    list_B.append(kor) #번호판의 문자를 담은 리스트

for i in range(20): #전체 데이터셋을 50개 만들 계획(그 중 20개는 2019년에 개정된 번호판)
    list_1 = [random.choice(number) for i in range(3)] 
    list_2 = [random.choice(korean) for i in range(1)]
    list_3 = [random.choice(number) for i in range(4)]
    list_1 = ["".join(list_1)]
    list_3 = ["".join(list_3)]
    list_last = list_1 + list_2 + list_3
    str = " ".join(list_last) #문자와 숫자 사이 공백
    draw_text = str
    font = ImageFont.truetype("NotoSansKR-Medium.otf",37, encoding="unic") #파라미터 순대로 폰트,폰트 크기
    path = "license_plate.png" #기존의 번호판 배경 이미지
    image_pil = Image.open(path)
    draw = ImageDraw.Draw(image_pil)
    w, h = font.getsize(draw_text)
    draw.text((16,-3),draw_text,'black', font) #(x,y), 번호판 문자열, 폰트 색, 위에서 설정한 폰트  

    image_pil.save(draw_text+'.png',"PNG")
	#image_pil.show() 만약 이미지를 보고 싶다면 입력(저장하는 기능은 아님)
    
for i in range(30): #전체 데이터셋을 50개 만들 계획(그 중 30개는 2019년 전에 만들어진 번호판)
    list_1 = [random.choice(number) for i in range(2)]
    list_2 = [random.choice(korean) for i in range(1)]
    list_3 = [random.choice(number) for i in range(4)]
    list_1 = ["".join(list_1)]
    list_3 = ["".join(list_3)]
    list_last = list_1 + list_2 + list_3
    str = " ".join(list_last)
    draw_text = str
    font = ImageFont.truetype("NotoSansKR-Medium.otf",37, encoding="unic")
    path = "license_plate.png"
    image_pil = Image.open(path)
    draw = ImageDraw.Draw(image_pil)
    w, h = font.getsize(draw_text)
    draw.text((27,-3),draw_text,'black', font)

    image_pil.save(draw_text+'.png',"PNG")
