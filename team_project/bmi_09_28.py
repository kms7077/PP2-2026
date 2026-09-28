import turtle

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

def draw_table(clean_data) :

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    start_x, start_y = -300, 300
    cell_width, cell_height = 120, 35

    # 열과 행의 개수
    columns, rows = 6, len(clean_data)+1

    # 표 그리기
    for row in range(rows):
        for col in range(columns):

            # 현재 칸의 위치
            x = start_x + col * cell_width 
            y = start_y - row * cell_height

            # 현재 칸으로 이동
            t.goto(x, y)

            # 펜 내리기
            t.pendown()

            # 사각형 그리기
            for i in range(2):
                t.forward(cell_width)
                t.right(90)
                t.forward(cell_height)
                t.right(90)

            # 펜 올리기
            t.penup()
        

def draw_text(clean_data):
    headers = ["전화번호", "이름", "키(cm)", "몸무게(kg)", "bmi", "소견"]
    
    t = turtle.Turtle()
    t.hideturtle()  
    t.penup()      

    start_x = -238
    start_y = 275
    col_width = 120 
    row_height = 35  

    for col_idx, header in enumerate(headers):
        x = start_x + (col_idx * col_width)
        t.goto(x, start_y)
        t.write(header, align="center", font=("맑은 고딕", 11, "bold"))

    for row_idx, row in enumerate(clean_data):
        y = start_y - ((row_idx + 1) * row_height)  
        
        for col_idx, item in enumerate(row):
            x = start_x + (col_idx * col_width)
            t.goto(x, y)
            t.write(str(item), align="center", font=("맑은 고딕", 10, "normal"))

    turtle.done()
    #draw_text

if __name__ == "__main__" :
    path = r"C:\202611818김민석\PP2-2026\team_project\health.txt"
    user_list = file_read(path)
    clean_data = data_store(user_list)
    draw_table(clean_data)
    draw_text(clean_data)