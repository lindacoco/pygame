#모듈 : 필요한 것들을 부품처럼 만들어진 파일 
#자동차: 타이어만 교체 , 범퍼만 교체 가능 
#영화에서 현금만 받아 ,, 잔돈을 안바꿔쥼

def price(people):
    print("{0}명 가격은 {1}입니다.".format(people, people *10000))

#조조할인 가격
def price_morning(people):
    print("{0}명의 조조할인 가격은 {1}입니다.".format(people, people *6000))

#군인할인 가격
def price_solider(people):
    print("{0}명의 군인할인 가격은 {1}입니다.".format(people, people *4000))

#모듈을 다른 파일에서 써보자.     