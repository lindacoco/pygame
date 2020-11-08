print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(5*11)
print(3*(3+1))


print('풍선')
print("나비")
print('zzzzzzzzzzzzzzz')
print("Z"*9 + "문자열과 정수를 섞어서 출력 가능")    

# 참 / 거짓 
print(5<10) #True 출력
print(not True) #False 출력됨
print(not False) 

print(not(5>10)) #True출력

#변수
#애완동물을 소개해 주세요

animal ="강아지"
name = "초코"
hobby = "낮잠"
age = 4
is_adult = age >= 3

print("우리집"+animal+"의 이름은" +name+"이에요")

hobby = "공놀이" #변수를 중간에 선언 할 수도 있다. 
# print("연탄이는 "+str(age)+"살이며,"+hobby+"을 아주 좋아해요")
print("연탄이는 ",age,"살이며,",hobby,"을 아주 좋아해요") #콤마로 들어갈 경우 무조건 띄어쓰기가 포함된다.
print(name+"는 어른일까요?" + str(is_adult))

''' 한번에 주석처리 가능 ''' 

# 주석
# 설정
# 하기  ctrl+ 슬래시 

#변수를 이용해서 다음 문장을 출력하시오

station = "신도림"

print(station+ "열차가 들어오고있습니다")

#연산자
print(1+1)
print(3-2)
print(2**3) #2의 3승 2^3 =8 
print(4%3) #나머지 구하기 1 
print(6//4) #몫 구하기  = 1 
print(10//3) #3
print(4>= 7) #False

print(5 <=5) #True

print(3==3) #True

print( 1 !=3 ) #True
print(not(1 != 3)) #False
print((3>0) and (3<5)) #True
print((3>0) or (5>10)) #True

#간단한 수식
print(2 + 3 *4) #14

number = 2 + 3 * 4
print(number)
number = number +2 
print(number)
number += 2 
print(number)
number *=2
print(number)


#절대값
print(abs(-5))
print(pow(4,2)) #4^2
print(max(5,11))
print(min(5,2))
#반올림 
print(round(1.6)) #2

from math import * 

print(floor(4.99)) #4
print(ceil(3.9)) # 4
print(sqrt(16)) # 4

#랜덤함수
from random import *
print(random()) #0.0이상 1.0미만의 임의 값 생성

print(random()*10) #0.0~ 10.0 미만
print(int(random()*10)) #정수로 출력
print(int(random()*10)) #정수로 출력
print(int(random()*10)) #정수로 출력
# 0은 싫다면.. 로또 1부터 출력
print(int(random()*10)+1) #1~10 이하의 임의의 수
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)
# 로또 1~ 45까지
print(int(random()*45)+1) #1부터 45이하의 값
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

print(randrange(1,46)) #1~46미만의 값을 생성
print(randrange(1,46)) #1~46미만의 값을 생성
print(randrange(1,46)) #1~46미만의 값을 생성
print(randrange(1,46)) #1~46미만의 값을 생성
print(randrange(1,46)) #1~46미만의 값을 생성
print(randrange(1,46)) #1~46미만의 값을 생성

print(randint(1,45)) #양 끝을 모두 포함한다 헷갈리면 이걸루

#quiz
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day)+"일로 선정되었습니다.")

#문자열
sentence = "나는 소녀입니다."
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 ="""
나는 소년이고,
파이썬은 쉬워요
"""

print(sentence3)

#슬라이싱
jumin = "990808-2039182"

#필요한 만큼 잘라서 사용
print("성별:" + jumin[7]) # 성별 :1
print("연: " + jumin[0:2]) #한자리 더 해서 적는다 0부터 2직전까지 콜론
print("월: " +jumin[2:4])
print("일:" +jumin[4:6])

print("생년월일:" +jumin[0:6])
print(jumin[:6]) #앞에 0 쓰지 않아도 똑같이 된다

print(jumin[7:])
#뒤에서부터
print(jumin[-7:]) #2039182

#문자열처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper()) #대문자로 

print(python[0].isupper()) #True
print(len(python)) #길이를 반환해준다 17
print(python.replace("Python","Java")) #바꿔서 출력해준다


index = python.index("n")
print(index) #파이썬에서 몇번째에 n이 있는지 알려준다 
index = python.index("n", index+1)
print(index) #두번째 n 15위치에 있다고 한다 

print(python.find("n")) #5라고 나옴 차이가 있으면 Java를 찾으면 
print(python.find("java")) # 없으면-1 반환. 인덱스로 하면 에러가 난다 

print(python.count("n")) # n이 몇 번 나오는지 2번

#문자열 포맷
print("a"+"b")
print("a","b")
#다른 방법 1
print("나는 %d살입니다." %20) #d는 정수값을 의미
print("나는 %s 을 좋아해요" %"python") #앞에 %적어
print("apple은 %c로 시작해요" %"A")

print("나는 %s살입니다." %20)  #s도 가능

print("나는 %s색과 %s색을 좋아해요" %("파란","보라")) # 순서대로 들어가게된다
#다른 방법 2 중괄호이용
print("나는 {}살 입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("노랑","분홍"))
print("나는 {1}색과 {0}색을 좋아해요".format("노랑","분홍")) #노랑 분홍 순으로 출력됨

#다른 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age =10, color="빨간")) #변수처럼 사용가능
#다른 방법 4 파이썬버전 3.6이상부터 가능
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f로 시작하면 바로 넣을 수 있다. 포맷..의 f인가봄

#탈출문자
print("""백문이 불여일견 
백견이 불여일타""")

# \n
print("백문이 불여일견\n 백견이 불여일타")

print("저는'나도코딩'입니다") #따옴표 안에는 다른 따옴표
print('저는"코코"입니다')
print("저는 \"나도코딩\"입니다") #역슬래시

# \\역슬래시 두번 문장내에서 하나의 \로 바뀌게 됨
#경로를 출력하고 싶음
print("C:\\Users\\YURI\\Desktop\\pythonworkspace>") #하나의 역슬래시만 출력됨
#\r 커서를 맨 앞으로 이동해준다.

print("Red Apple \rPine") #맨 앞으로 커서를 이동... Red 를 Pine으로 대체 
print("장장 미미미\r장초코노") #장초코노 미 출력됨 

#\b 한글자 지우는것
print("Redd\b Apple") #키보드 백스페이스
# \t 탭
print("Red \t Apple") #Red      Apple

#quiz 사이트 별로 비밀번호를 만들어주는 프로그램 작성

url = "http://google.com"
print(url)
pass1 = url.replace("http://","")

pass1 = pass1[:pass1.index(".")]
print(pass1)

password = pass1[:3]+ str(len(pass1))+str(pass1.count("e"))+"!"
print(password)

print("{0}의 비밀번호는 {1}입니다".format(url, password))

#리스트 [] 순서를 가지는 객체의 집합
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20 

subway = [10,20,30] #대괄호를 만들어 순서대로 집어넣는다.
print(subway) #[10,20,30]출력

subway =["유재석","조세호","박명수"]
print(subway)  #['유재석', '조세호', '박명수']

# 조세호가 몇번째 칸
print(subway.index("조세호")) #1 의 위치에 있다고 나옴 
# 하하가 탐
subway.append("하 하")
print(subway) # ['유재석', '조세호', '박명수', '하 하']

#어펜드는 맨 뒤에 붙는데 중간에 넣어보기
subway.insert(1,"정형돈") #1번째의 위치에 넣겠다 
print(subway)

#뒤에서 부터 한명씩 빼기
print(subway.pop()) #하하
print(subway) #['유재석', '정형돈', '조세호', '박명수']
print(subway.pop()) 
print(subway) #['유재석', '정형돈', '조세호']
print(subway.pop()) 
print(subway) #['유재석', '정형돈']

#같은 이름의 사람이 몇 명 있는지 확인하기
subway.append("유재석")
print(subway) #['유재석', '정형돈', '유재석']
print(subway.count("유재석")) #2

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) #[1, 2, 3, 4, 5]
#뒤집기도 가능
num_list.reverse()
print(num_list) #[5, 4, 3, 2, 1]

#모두 지우기
num_list.clear() #리스트 안의 모든 내용 삭제
print(num_list) #[]
#자료형에 구애받지 않고 섞어서 사용 가능
mix_list =["조조", 1,  True]

print(mix_list) #['조조', 1, True]
num_list = [5,2,4,3,1]
#리스트 확장
num_list.extend(mix_list)
print(num_list) #[5, 2, 4, 3, 1, '조조', 1, True]

#사전자료형
#라이브러리 중괄호
cabinet ={3:"유유지", 100:"김현중"} #키는 3 value 유유지
print(cabinet[3]) #키 값을 넣는다 유유지
print(cabinet[100])
#대괄호 외에
print(cabinet.get(3))
# print(cabinet[5]) #없는 값을 넣으면 프로그램이 종료된다.
print(cabinet.get(5)) # None으로 찍히고 다음부분이 실행된다. 없는걸 할때 다른 값을 넣고싶다면
print(cabinet.get(5,"사용가능")) #사용가능이라고 찍힌다. 

print(3 in cabinet) # 사전 자료형 안에 key in 변수 있으면 True없으면 False
# 스트링도 가능
cabinet = {"A-2":"유재석","A-5":"나나"}
print(cabinet["A-2"])
print(cabinet.get("A-5")) #여기서 0, 1 이렇게 넣으면 키를 넣는거라서 None이 뜬다

#새손님
cabinet : dict
cabinet["A-2"] ="김종국" #업데이트 됨
cabinet["C-20"] = "조세호"
 
print(cabinet) #{'A-2': '김종국', 'A-5': '나나', 'C-20': '조세호'}

# 간 손님
del cabinet["A-5"] #del이용
print(cabinet) #{'A-2': '김종국', 'C-20': '조세호'}

print(cabinet.keys()) #dict_keys(['A-2', 'C-20'])
print(cabinet.values()) #dict_values(['김종국', '조세호'])

#쌍으로 출력
print(cabinet.items()) #dict_items([('A-2', '김종국'), ('C-20', '조세호')])

#목욕탕이 문을 닫아서 모두 퇴장
cabinet.clear() #모든 값을 지울 수 있음 {} 으로 출력

#튜플 - 내용변경이나 추가를 할 수 없지만 속도가 리스트보다 빨라서 변경되지 않는걸 만들 때 사용
# 돈까스 집 메뉴 두가지
menu = ("돈까스","치즈까스") #리스트는 대괄호 [] 튜플은 그냥 괄호()
print(menu[0]) #돈까스
print(menu[1]) #치즈까스

# 값 추가, 변경 불가능! add 못 씀

name = "김종국"
age =20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) =("김종국", 20, "코딩")
#순서대로 넣기 가능
print(name, age, hobby)

#set 집합 : 중복이 안되고, 순서가 없음 
my_set = {1,2,3,3,3} #중괄호는 사전에서 키와 벨류 썼었음 세트에서는 그냥 값만
print(my_set) # {1, 2, 3} 중복 허용안함 

java ={"유재석","양세형","김세호"}
python =set(["유재석","박명수"])

#교집합 출력 자바와 파이썬 모두 할 수 있는 사람
print(java & python) #{'유재석'}
print(java.intersection(python))

#합집합
print(java | python) #{'김세호', '유재석', '양세형', '박명수'}
print(java.union(python))

#차집합 자바는 할 수 있지만 파이썬은 못하는 개발자
print(java - python) #{'양세형', '김세호'}
print(java.difference(python))

#python을 할 수 있는 사람이 늘어남 
python.add("김세호")

print(python) #{'유재석', '김세호', '박명수'} 세트에 값 추가 가능

#자바를 까먹음
java.remove("김세호")
print(java) #{'유재석', '양세형'}

#자료구조의 변경
menu = {"커피","우유","주스"}
print(menu, type(menu)) #{'주스', '우유', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) #['커피', '주스', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) #('커피', '주스', '우유') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #{'주스', '우유', '커피'} <class 'set'>

#quiz 댓글이벤트 한명은 치킨, 3명은 커피 쿠폰 20명이 작성 아이디 1~20, 중복불가 shuffle과 sample활용

from random import *

users = range(1,21) #1부터 20까지 숫자 리스트 생성
print(type(users)) #type은 range <class 'range'>
users = list(users) #list타입으로 저장됨
print(users)

shuffle(users)
print(users)

winners = sample(users,4) #한번에 4명 뽑는다

print("--당첨자 발표--")
print("치킨 당첨자:  {}".format(winners[0]))
print("커피 당첨자:  {}".format(winners[1:])) #중괄호안에 0넣어도 됨 
print("--축하합니다--")

#if 분기


'''if 조건 : 
      실행 명령문 '''
#  weather == "맑음" :
# weather =  input("오늘 날씨는 어때요? ")  #사용자의 명령을 입력하는 부분이 뜨고 입력하는 값이 weather에 들어감 
# if weather == "비" or weather =="눈":
#      print("우산을 챙기세요")
# elif weather =="미세먼지" :
#      print("마스크를 챙기세요")
# else :
#      print("준비물 필요 없습니다 ")

# temp = int(input("기온은 어때요?")) #인풋은 문자로 받으니까
# if temp >= 30 :
#     print("너무 더워요. 나가지 마세요")
# elif temp <30 and temp >=10 :
#     print("괜찮은 날씨에요")
# elif temp <10 and temp >=0 :
#     print("너무 추워요 나가지 마세요")

#for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")


for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {}".format(waiting_no) ) 

for waiting in range(5): #0~4까지 for문
    print("대기번호 : {}".format(waiting) ) 

for waiting in range(1,4): #1~3까지 for문
    print("대기번호 : {}".format(waiting) )


starbucks = ["아이언맨", "토르","로키"]
for customer in starbucks :
     print("{}, 커피 준비되었습니다.".format(customer)) #순서대로 적용됨 

#while 
# customer = "토르"
# index = 5
# while index >=1 :
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer,index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다.")

customer ="아이언맨"
index = 1
# while True:
#       print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer,index))
#       index += 1 #무한루프.. ctrl C로 종료 

# customer ="토토"
# person ="Unknown"
# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

#continue와 break
# 선생님이 책을 읽으라고 시킬 수 있음

absence = [2,5] #결석
no_book =[7] #책을 깜빡함
for student in range(1,11): #1~10까지
   
    if student in absence :
      continue #아래문장을 실행시키지 않고 바로 다음 조건으로 넘게 만드는 것 
    elif student in no_book:
      print("오늘 수업은 여기까지. {0}번은 교무실로".format(no_book))
      break
    print("{0}번, 책을 읽어봐".format(student))

#한줄로 끝내는 for문
# 출석번호 1,2,3,4,... 앞에 100을 붙이기로 함 101,102
students= [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students) #[101, 102, 103, 104, 105]

#학생이름을 길이로 변환
students=["Iron man","Thor","roki"]
students = [len(i) for i in students]
print(students) #[8, 4, 4]

# 학생이름을 대문자로 바꾸기 
students=["Iron man","Thor","roki"]
students = [i.upper() for i in students]
print(students) #['IRON MAN', 'THOR', 'ROKI']

#quiz
# 택시기사, 50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수를 구하는 프로그램을 작성 
# 승객별 운행 소요시간은 5~50분 사이의 난수 , 나는 5분~15분 손님만 매칭해야한다.

from random import *

my_cust=0
# for customer in range(1,51) :
#     print(customer)
# for time in randint(1,51) :
#     print(time)  
# for customer in range(1,51) :
#     for time in randint(1,51) :
#      if time >=1 and time <=15 :
#         print("a")
    #  torf =  " O "
    #  my_cust +=1 
    # print("[{0}] {1}번째 손님 (소요시간: {2}분".format(torf,customer,time))    
    # elif time >= 16 :
    #     torf =  " "
    # print("[{0}] {1}번째 손님 (소요시간: {2}분".format(torf,customer,time))
#print("총 탑승 승객 :{0} 분".format(count(my_cust))
#다시해보기
for i in range(1,51) : #1~50이라는 승객
    time = randrange(5,51) #5~50분사이의 소요시간
    if 5<= time <=15 :  #5~15분 이내의 손님 탑승 승객 수 증가처리
           print("[O] {0}번째 손님 (소요시간: {1}분".format(i,time))
           my_cust += 1
    else:  #매칭 실패한 경우
           print("[ ] {0}번째 손님 (소요시간: {1}분".format(i,time))
print("총 탑승 승객 :{0} 명".format(my_cust))

#함수
#5를 전달했을때 +20을 해서 25를 받는다
def open_account() : #함수 정의 
    #실제 내용 작성
    print("새로운 계좌가 생성되었습니다.")
#호출
open_account() #새로운 계좌가 생성되었습니다.
balance =0
def deposit(balance, money) : #새로 입금받는 money
  balance += money
  print("잔액은 {}원 입니다".format(balance))
  return balance + money
deposit(balance,10000)

#출금
def withdrwal(balance, money) :
  if balance > money :
      print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
      return balance-money
  else :
      print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
      return balance

withdrwal(10000,1000)

#저녁 출금 커미션 100원
balance =1000
def withdrwal_night(balance,money):
    commission = 100
    return commission, balance- money- commission
commission, balance = withdrwal_night(balance, 500)
print("수수료는 {0}, 잔액은 {1}입니다.".format(commission,balance))


#기본값
def profile(name, age, main_lang):
    print("이름: {0}\t 나이: {1} \t 주 사용언어: {2}".format(name, age, main_lang))

profile("나나",str(20),"파이썬")
#같은학교 같은 학년 같은반 같은수업
def profile1(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t 나이: {1} \t 주 사용언어: {2}".format(name, age, main_lang))
profile1("자냥")  #이름: 자냥       나이: 17        주 사용언어: 파이썬
profile1("초롱")  #age, 메인언어 적지 않아도 설정한 대로 출력됨 

#키워드값을 이용한 함수호출 순서 관계없이 값 입력 가능
def profile2(name, age, main_lang):
    print("이름: {0}\t 나이: {1} \t 주 사용언어: {2}".format(name, age, main_lang))
profile2(name="또또", main_lang="자바",age="20") #이름: 또또       나이: 20        주 사용언어: 자바

#가변인자
def profile4(name, age, lang1, lang2, lang3, lang4):
    print("이름: {0}\t 나이: {1}\t".format(name,age),end=" ") #end큰따옴표 띄우기면 문장 출력 후 줄바꿈이 없음 빈칸이 엔드 
    print(lang1, lang2, lang3, lang4)

profile4("유재석",20,"파이썬","자바","html","")
#빈칸을 매번 넣거나 lang6을 추가하거나 하기가 귀찮아짐 이 때 쓰는 것이 가변함수
def profile4(name, age, *language):
    print("이름: {0}\t 나이: {1}\t".format(name,age),end=" ") #end큰따옴표 띄우기면 문장 출력 후 줄바꿈이 없음 빈칸이 엔드 
    for lang in language :
        print(lang, end=" ")
profile4("유재석",20,"파이썬","자바","html","")
profile4("재호",20,"파이썬","자바")

#지역변수와-함수에만사용 전역변수 -프로그램 내 어디서든 사용 가능
# 군대
gun =10  #UnboundLocalError: local variable 'gun' referenced before assignment
def checkpoint(soliders): #경계근무 서는 군인들 수 
    gun =20
    gun -= soliders
    print("[]남은 총:{0}".format(gun))

print()
print("전체 총: {0}".format(gun))
checkpoint(2)
#전체 총: 10
#[]남은 총:18 순서로 출력됨 
 
def checkpoint(soliders): #경계근무 서는 군인들 수 
    global gun #전역변수로 선언된 gun값을 쓰겠다
    gun -= soliders
    print("[]남은 총:{0}".format(gun))

print()
print("전체 총: {0}".format(gun))
checkpoint(2)
#전체 총: 10
#[]남은 총:8 로 출력됨

def checkpoint_return(gun,soliders):
    gun = gun - soliders
    print("[]남은 총:{0}".format(gun))
    return gun #밖에서 받을 수 있음 
print()
print("전체 총: {0}".format(gun))
checkpoint_return(gun,4)
#전체 총: 8
#[]남은 총:4


#quiz 표준체중을 구하는 프로그램을 작성하시오
# 표준체중은 각 개인의 키에 적당한 체중 남자: 키(m)*키(m) * 22
# 
from math import *
def std_weight(height,gender):
    hei_num = height/100
    if gender == "여자" :
        print("키 {0} 여자의 표준 체중은 {1}입니다.".format(height,round((hei_num*hei_num)*21,2)) )
        
    else:
        print("키 {0} 남자의 표준 체중은 {1}입니다.".format(height,round((hei_num*hei_num)*22,2)) )
       
std_weight(175,"남자")

# def std_weight(height, gender) :
#   if gender =="남자 " :
        # return height * height * 22 
    #else:
        # return height * height * 21 
# height = 175
# gender ="남자"
# weight = round(std_weight(height /100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}입니다".format(height, gender, weight))

# 표준입출력
print("Pyth","jav","jas", sep=" vs ") #Pyth vs jav vs jas 사이사이에 vs가 들어간다 
print("Pyth","jav","jas", sep=",",end ="?") #프린트 문장을 한줄에 넣게해주는 end
print("무엇이 더 재미있을까요?")

import sys
print("Pyth","jav","jas", file=sys.stdout) #표준출력 Pyth jav jas
print("Pyth","jav","jas", file=sys.stderr) #표준에러 로그처리를 한다고 할 때 필요하면 따로 에러처리를 할 수 있다

#출력포맷
scores ={"수학": 0, "영어" :50, "코딩" :100}
for subject, score in scores.items(): #딕셔너리에서는 items로 하면 키와 밸류로 가져옴
    #print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #8개의 공간을 만들고 왼쪽으로 정렬 , 오른쪽으로 4개공간확보

#은행에 갔을 때 대기 순번표 001,003, ...
for number in range(1,21): #1~20까지
    print("대기번호:" + str(number).zfill(3)) #값이 없는 부분은 0으로 채운다 대기번호:020

#answer = input("아무값이나 입력하세요: ") #값을 입력하면 answer에 들어감
#print("입력하신값은"+answer+"입니다.") #문자를 입력하지 않고 숫자로 입력해도 잘 들어간다 
#print(type(answer)) #타입을 찍어보면 10도 str로 찍힘  사용자 입력값은 항상 문자열 형태로 들어간다는 것

#다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(-500))  #       500
# 양수일땐 +로 표시, 음수일땐 -로 표시
print("{0: >+10}".format(500))  #      +500
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))  #+500______
print("{0:_<10}".format(500))   #500_______
#세자리마다 콤마찍기
print("{0:,}".format(1000000000))  #1,000,000,000
#세자리마다 콤마 찍고 부호도 붙여주기 
print("{0:+,}".format(1000000000)) #+1,000,000,000
#세자리마다 콤마찍고, 부호, 자릿수확보, 빈자리는 ^표시로 채우기
print("{0:^<+30,}".format(1000000000)) #+1,000,000,000^^^^^^^^^^^^^^^^
#소수점출력
print("{0:f}".format(5/3))  #1.666667
print("{0:.2f}".format(5/3)) #1.67

#파일입출력
score_file= open("score.txt","w", encoding="utf8") #스코어라는 파일이 생성됨 w로 열어본다 덮어쓰기
print("수학 : 0", file=score_file)
print("영어: 50",file=score_file)
score_file.close()

score_file2 = open("score.txt","a",encoding="utf8") #연달아 쓰는 append를 의미
score_file2.write("과학: 80")
score_file2.write("\n코딩: 100")
score_file2.close()

score_file3 = open("score.txt","r",encoding="utf8") #읽다
print(score_file3.read()) # 터미널 창에 텍스트가 열린다. 
score_file3.close() 
#한줄한줄 열기
score_file4 = open("score.txt","r",encoding="utf8") #읽다
print(score_file4.readline()) # 한줄을 열고 커서를 다음 줄로 이동한다 
print(score_file4.readline())
print(score_file4.readline())
print(score_file4.readline())
print(score_file4.readline())
score_file4.close() 

#몇줄인지 모를 때
score_file5 = open("score.txt","r",encoding="utf8") #읽다
while True:
    line = score_file5.readline()
    if not line :
        break
    print(line, end="")
score_file5.close() 

print("")

score_file6 = open("score.txt","r",encoding="utf8") #읽다
lines = score_file6.readlines() #list형태로 저장
for line in lines:
    print(line, end="")
score_file6.close()

#pickle 프로그램상에서 사용하는 프로그램을 파일 형태로 저장
import pickle
profile_file = open("profile.pickle","wb") #binary의 b 피클에서는 따로 인코딩을 저장하지 않아도됨
profile = {"이름":"조조","나이":30,"취미":["축구","골프","농구"]}
print(profile) #{'이름': '조조', '나이': 30, '취미': ['축구', '골프', '농구']}
#피클을 이용해 이 데이터를 쓰는 것
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

#읽기
profile_file2 = open("profile.pickle","rb")
profile = pickle.load(profile_file2) #데이터를 가지고 와서 바이너리 형태로 불러와준다
print(profile)   #{'이름': '조조', '나이': 30, '취미': ['축구', '골프', '농구']}
profile_file2.close()

#with  파일을 열고 처리를 하고 파일을 닫았는데 with를 쓰면 조금 더 편하게 쓸 수 있다.
import pickle

with open("profile.pickle","rb") as profile_f :
    print(pickle.load(profile_f)) #{'이름': '조조', '나이': 30, '취미': ['축구', '골프', '농구']}

#따로 닫을 필요없이 with를 벗어나면서 닫아준다
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열공하는중 ")

with open("study.txt","r", encoding="utf8") as study_file:
    print(study_file.read())  #파이썬을 열공하는중

#quiz 매주1회 작성하는 보고서 
# -x주차 주간보고 - 
# 부서:
# 이름:
# 업무요약:  
#1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램을 작성하시오. 파일명은 1주차.txt 2주차.txt.. 이런식으로 만든다

import pickle
# for numm in range(1,6) :
#     with open("{0}주차.txt".format(numm),"w") as workingfile:
#         workingfile.write("-"+str(numm)+"주차 주간보고-")
#         workingfile.write("부서: ")
#         workingfile.write("이름: ")
#         workingfile.write("업무요약: ")

for i in range(1,6) :
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:
        report_file.write("-{0}주차 주간보고 -".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무요약: ")

#클래스 스타크래프트
 # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
 
name = "마린"
hp =40 #유닛의 체력
damage = 5 #유닛의 공격력

print("{0}유닛이 생성되었습니다.".format(name))
print("체력{0}, 공격력 {1}".format(hp,damage))

tank_name= "탱크"
tank_hp = 150
tank_damage = 35
print("{0}유닛이 생성되었습니다.".format(tank_name))
print("체력{0}, 공격력 {1}".format(tank_hp,tank_damage))

def attack(name,location, damage):
    print("{0}유닛이 {1}방향으로 적군을 공격합니다 [공격력 {2}]".format(name,location,damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)

class Unit: 
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp =hp
        self.damage =damage
        print("{0}유닛이 생성되었습니다".format(self.name))
        print("체력{0}, 공격력 {1}".format(self.hp,self.damage))


marine1 = Unit("마린",40,5)
marine1 = Unit("마린",40,5)
marine1 = Unit("탱크",150,35)

#init __init__ 생성자 클래스 안의 변수들 다 써야함 3개면 3가지 값을 다 넣어야함

#멤버변수 클래스안의 self.name 이런것들
#레이스
wraith1 = Unit("레이스",80,5)
print("유닛이름:{0}, 공격력:{1}".format(wraith1.name,wraith1.damage)) #점을 사용해서 멤버변수를 외부에서 사용가능
#마인드 컨트롤
wraith2 = Unit("빼앗은 레이스",80,5) #빼앗은 레이스유닛이 생성되었습니다
wraith2.cloking = True #외부에서 클로킹이라는 변수를 할당해서 넣음 파이썬은 객체 외부에서 추가로 변수를 만들어 넣을 수 있음
if wraith2.cloking == True:
    print("{0}은 현재 클로킹 상태입니다".format(wraith2.name)) #빼앗은 레이스은 현제 클로킹 상태입니다
#wraith1에는 클로킹이 없기때문에 wraith1.cloking이라고 치면 오류가 뜬다.

class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp =hp
        self.damage =damage 
   
    def attack(self, location):
       print("{0}유닛이 {1}방향으로 적군을 공격합니다 [공격력 {2}]"\
       .format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))
        

# 파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

#공격 두번 받음
firebat1.damaged(25)
firebat1.damaged(25)




#상속
class Unit1 :
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp =hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1}방향으로 이동합니다. [속도{2}]".format(self.name, location, self.speed))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -=damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

#이걸 상속받는 클래스 생성
class AttackUnit1(Unit1): #상속받을 유닛1을 괄호안에 넣어주고
    def __init__(self,name,hp,damage,speed): #이닛을 불러 부모 값을 불러줌 
        Unit1.__init__(self,name,hp,speed)
        self.damage = damage
    def attack(self, location):
       print("{0}유닛이 {1}방향으로 적군을 공격합니다 [공격력 {2}]"\
       .format(self.name,location,self.damage))

#마린 유닛
class Marine(AttackUnit1):
    def __init__(self):
        AttackUnit1.__init__(self,"마린",40,5,1)
      
    #스팀팩: 일정 시간동안 이동 및 공격 속도를 증가 시킴 체력 10감소 해서 빠르게 이동 가능
    def stimpack(self):
        if self.hp > 10 :
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다. (HP10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스탬팩을 사용하지 않습니다.".format(self.name))


firebat1 = AttackUnit1("파이어뱃",50,16,0)
firebat1.attack("5시")

#탱크
class Tank(AttackUnit1):
    #시즈모드  더 높은 파워로 공격 가능하다 . 이동 불가.  
    seiz_developed = False 
    def __init__(self):
        AttackUnit1.__init__(self,"탱크",150,35,1)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seiz_developed == False :
             return 
        
        if self.set_seize_mode == False:
            print("{0} : 시즈 모드로 전환합니다.".format(self.name))
            self.damage *=2 
            self.set_seize_mode = True
        else :
            print("{0} : 시즈 모드를 해제합니다.".format(self.name))
            self.damage /=2 
            self.set_seize_mode = False 



#공격 두번 받음
# firebat1.damaged(25)
# firebat1.damaged(25)

#다중상속 부모 클래스를 두개 받는다

#드랍쉽 : 공중유닛, 수송기, 마린/파이어뱃/탱크 등을 수송  -공격은 불가능

class Flyable: 
    def __init__(self,speed):
        self.speed = speed

    def fly(self,name,location):
        print("{0}: {1}방향으로 날아갑니다. [속도 {2}]".format(self.name,location,self.speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit1, Flyable): #부모클래스 콤마로 구분 
    def __init__(self, name, hp, damage, speed):
        AttackUnit1.__init__(self,name,hp,damage,speed)
        Flyable.__init__(self,speed)
    
    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)

#레이스 생성
class Wraith(FlyableAttackUnit):
    #클로킹 모드 
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5) 
        self.clocked = False #클로킹모드가 아닌 상태로 만들어짐
    def cloking(self): #외부에서 클로킹할거야 하면
        if self.clocked == True :
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다".format(self.name))
            self.cloked = True



#발키리 생성 : 공중공격 유닛, 한번에 14발 미사일 발사 가능
valkyrie = FlyableAttackUnit("발키리",200,6, 5)
valkyrie.fly(valkyrie.name,"3시")

#연산자 오버로딩, 부모 클래스에서 정의 되지 않은 함수를 자식클래스에서 정의해서 사용할 수 있다.

# 벌쳐: 지상유닛, 기동성 좋음
vulture = AttackUnit1("벌쳐",80,10,20)

#배틀 크루저: 공중유닛, 체력 좋고 공격력좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500 , 25, 3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name,"9시")

#매번 지상유닛인지 공중유닛인지 확인해야하는 번거로움이 있다. 똑같이 move함수를 써도 공중은 날아가도록 하기 위해서는

battlecruiser.move("9시") #배틀크루저: 9시방향으로 날아갑니다. [속도 3] 똑같이 쓰게된다 

#패스
#어떤 건물을 만든다
# class BuildingUnit(Unit1):
#     def __init__(self,name,hp, location) :
#         pass  #아무것도 안하고 일단 넘어가 아무것도 안찍힘

#서플라이 디폿: 건물, 1개건물 = 8 유닛
#supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") 

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player: GG")
    print("[Plyer] 님이 게임에서 퇴장 하셨습니다.")
    pass

game_start()
game_over() #아무것도 안찍히고 패스

#슈퍼
class BuildingUnit(Unit1):
    def __init__(self,name,hp, location) :
    # Unit.__init__(self,name,hp,0)
     super().__init__(name,hp, 0) #슈퍼를 쓰면 이닛을 쓰고 self값을 보내지 않는다. 
     self.location = location


#스타크래프트 전반전 
game_start()
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동
for unit in attack_units:
    unit.move("1시")
#탱크 시즈모드로 개발 
Tank.seiz_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

#공격 모드 준비( 탱크 : 시즈모드, 레이스: 클로킹모드 , 마린: 스탬팩)
for unit in attack_units :
    if isinstance(unit, Marine):  #지금 객체가 어떤 클래스의 인스턴스인지 확인 
       unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21)) #공격은 랜덤으로 받음 (5~20사이)

# 게임 종료
game_over()


#quiz 부동산프로그램

class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type \
        ,self.price, self.completion_year)

house = [] #리스트
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

house.append(house1)
house.append(house2)
house.append(house3)

print("총 {0}개의 매물이 있습니다.".format(format(len(house))))
for houses in house:
    houses.show_detail()

# 예외처리 에러가발생했을 때 그 에러를 처리하는 것 
#택배 주소 오류, 잔액 부족 
# print("나누기 전용 계산기입니다.")
# num1 = int(input("첫번째 숫자를 입력하세요 : "))
# num2 = int(input("첫번째 숫자를 입력하세요 : "))
# print("{0}/{1} = {2}".format(num1,num2, int(num1/num26)))
# 여기서 삼 넣으면 오류가 나서 프로그램이 종료되어버림

# try: 
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("첫번째 숫자를 입력하세요 : "))
#     print("{0}/{1} = {2}".format(num1,num2, int(num1/num2))) 
# except ValueError:
#     print("잘못된 값을 입력했습니다.")
# #0 으로 나눴을 때 오류가 나는것
# except ZeroDivisionError as err:
#    print(err)

try: 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    # 3nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0],nums[1], nums[2])) 
except ValueError:
    print("잘못된 값을 입력했습니다.")
#0 으로 나눴을 때 오류가 나는것
except ZeroDivisionError as err:
   print(err)
#nums[2]를 실수로 안넣었을 경우 리스트에 없는경우
# except :
#     print("알 수 없는 에러가 발생하였습니다.")
except Exception as err:
  print("알 수 없는 에러가 발생하였습니다.")
  print(err) #list index out of range 정확한 에러 메세지도 같이 뜬다 

#의도적으로 에러 발생시키기
# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1= int(input("첫번째 숫자를 입력하세요 : "))
#     num2= int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise ValueError #특정 에러를 지정해서 exception에 지정  ValueError
#     print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("한자리 숫자만 입력하세요 ")

#사용자 정의 에러
class BigNumError(Exception):
    #pass
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

         
# try:
#     print("한자리 숫자 나누기 전용 계산기입니다.")
#     num1= int(input("첫번째 숫자를 입력하세요 : "))
#     num2= int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >=10 or num2 >=10:
#         raise BigNumError #특정 에러를 지정해서 exception에 지정  ValueError
#     print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
# except ValueError:
#     print("한자리 숫자만 입력하세요 ")    
# except BigNumError:
#     print("너무 큰 숫자입니다. 한자리 숫자만 입력하세요 ")

try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1= int(input("첫번째 숫자를 입력하세요 : "))
    num2= int(input("두번째 숫자를 입력하세요 : "))
    if num1 >=10 or num2 >=10:
        raise BigNumError("입력값 : {0} , {1}".format(num1, num2)) #함수 수정했으니 이 안에 직접 출력
    print("{0}/{1}={2}".format(num1,num2,int(num1/num2)))
except ValueError:
    print("한자리 숫자만 입력하세요 ")    
except BigNumError as err:
    print("너무 큰 숫자입니다. 한자리 숫자만 입력하세요 ")
    print(err)
finally :
    print("계산기를 이용해 주셔서 감사합니다.")
#finally 예외처리 구문에서 오류가 생기건 말건 무조건 처리되는 부분 

#자동주문시스템, 적절한 예외처리구문

chicken = 10
waiting = 1 #홀 안은 현재 만석, 대기번호 1부터 시작

class SoldOutError(Exception):
    pass
    # def __init__(self,msg):
    #     self.msg = msg
    # def __str__(self):
    #     return self.msg


while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order <=0 :
            raise ValueError   
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order
        if chicken == 0 :
            raise SoldOutError
            # raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.") 
            # break
    except ValueError :
          print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break




















