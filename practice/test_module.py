# 호출방법
# 1. import theater_module
# theater_module.price(3) #3명이서 영화보러 갔을 때 가격 
# #조조할인 가격
# theater_module.price_morning(4)

# theater_module.price_solider(3)

# 2.import theater_module as mv #별명을 써서 줄일 수 있다 
# mv.price_solider(4)

# 3.
# from theater_module import *
# price(3)

# 4.필요한 함수만
# from theater_module import price, price_morning
# price(5)

# 5. 한개의 모듈만 별명을 붙여서 사용
# from theater_module import price_solider as price
# price(4) #4명의 군인할인 가격은 16000입니다.  이때 price는 별명 price 

# import travel.thailand #임포트 뒤에는 모듈이나 함수만 가능, 클래스(ThailandPackage)는 불가능 from에서는 사용가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() #[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# from travel.thailand import ThailandPackage #이렇게는 가능 
# trip_to1 = ThailandPackage()
# trip_to1.detail() 

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail() #[베트남 패키지 3박 5일] 다낭 효도 여행 60만원

from travel import *
trip_to = vietnam.VietnamPackage() #왜 오류가 날까?? 공개범위가 달서서
trip_to.detail() #__init__파일을 수정했더니 됨 

trip_to = thailand.ThailandPackage() #왜 오류가 날까?? 공개범위가 달서서
trip_to.detail()

#위치확인
import inspect
import random
print(inspect.getfile(random)) #C:\Python39\lib\random.py

print(inspect.getfile(thailand)) #c:\Users\YURI\Desktop\pythonworkspace\travel\thailand.py

#pip패키지 설치 
#랜덤수를 만드는 프로그램 누군가 만든 것을 활용하는등
#터미널에 붙여넣기 pip install beautifulsoup4

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장함수
# input : 사용자 입력을 받는 함수 
# dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시 
# print(dir())
# import pickle #외장 함수
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# https://docs.python.org/ko/3/library/functions.html#input

#외장함수 
# https://docs.python.org/3/py-modindex.html

#glob : 경로 내의 폴더/ 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob(".py")) #확장자가 py인 모든 파일 

import os
print(os.getcwd()) #현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder,"폴더를 삭제하였습니다.")
else :
    os.makedirs(folder)
    print(folder,"폴더를 생성하였습니다.")

print(os.listdir())

#시간관련된 외장함수 
import time
print(time.localtime())
print(time.strftime("%Y-%m-%D %H:%M:%S")) # %d 2020-10-$10/30/20 07:55:31

import datetime
print("오늘 날짜는",datetime.date.today()) #오늘 날짜는 2020-10-30
#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days =100)
print("우리가 만난지 100일은", today + td)
#오늘 날짜는 2020-10-30
#우리가 만난지 100일은 2021-02-07


#프로젝트 내에 나만의 시그니처를 남기는 모듈을 만들어라 byme.py

import byme
byme.sign()


