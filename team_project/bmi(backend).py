
def file_read(path) :
    f = open(path, 'r', encoding='utf-8')
    user_list = []

    file = f.readlines()
    for i in file :
        user_list.append(i.split())

    print("데이터 저장완료")
    return user_list

def cal_bmi(height, weight) :
    
    """
    Args :
        height (float) : 키 (cm 단위)
        weigth (float) : 몸무게 (kg 단위)
    
    Returns :
        tuple[str, float] : (비만도 판정 문자열, bmi 계산값)
    """

    result = weight / ((height)*0.01)**2
    state = ""

    if 20 > result : state = "저체중"
    elif 20<=result<25 : state = "표준"
    elif 25<=result<30 : state = "과체중"
    elif result>= 30 : state = "비만"

    return state, result

def data_store(user_list) :
    clean_data = []
    for user in user_list :
        tel, name = user[0], user[1]

        height, weight = float(user[2]), float(user[3])
        state, result = cal_bmi(height, weight)

        clean_data.append([tel, name, height, weight, round(result, 3), state])

    return clean_data

def main() :
    path = "lab\\Team_project\\health.txt"
    user_list = file_read(path)
    clean_data = data_store(user_list)

    print(["전화번호", "이름", "키(cm)", "몸무게(kg)", "bmi", "소견"])
    
    for data in clean_data :
        print(data)

if __name__ == "__main__" :
    main()