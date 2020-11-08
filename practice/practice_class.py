class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
       # super().__init__()
       Unit.__init__(self)
       Flyable.__init__(self)

#드랍쉽을 만든다
dropship = FlyableUnit() #Unit 생성자 만 생성됨 위치를 바꾸면 FlyableUnit 생성자만 출력.. 슈퍼를 쓰면 맨 첨에 받는 것만되기 때문에
#FlyableUnit클래스 밑에 슈퍼가 아닌 Unit.__init__(self) Flyable.__init__(self)를 쓴다.
#Unit 생성자
#Flyable 생성자 둘 다 뜸

