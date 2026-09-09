def say_happy_birthday(name:str) -> None:
    print("안녕하세요")
    print(name + "님의 생일을 축하합니다.")
    return None
def test_happy_birthday():
    say_happy_birthday("김윤성")
    say_happy_birthday("이원준")
    say_happy_birthday("유강훈")

def test_happy_birthday2():
    names = ["김윤성","이원준","유강훈"]
    for name in names : 
        say_happy_birthday(neme)
def test_happy_birthday3():
    say_happy_birthday(3,14159)
    say_happy_birthday(10)
    say_happy_birthday([1,2,3])

if __name__ == "__main__":
#    test_happy_birthday2()
    test_happy_birthday3()
