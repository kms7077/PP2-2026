import turtle

# 파일 열기
file = open("team_project/health.txt", "r", encoding="utf-8")

# 파일의 모든 줄 읽기
data = file.readlines()

# 파일 닫기
file.close()


# 터틀 생성
t = turtle.Turtle()
t.speed(0)
t.penup()


# 표의 시작 위치
start_x = -300
start_y = 300

# 한 칸의 크기
cell_width = 120
cell_height = 35

# 열과 행의 개수
columns = 4
rows = len(data) + 1


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

t.hideturtle()

turtle.done()