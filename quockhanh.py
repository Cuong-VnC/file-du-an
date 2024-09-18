import turtle

# Thiết lập cửa sổ vẽ
screen = turtle.Screen()
screen.title("Quốc Khánh Việt Nam ")
screen.setup(width=900, height=600)

# Tạo đối tượng turtle
pen = turtle.Turtle()
pen.speed(10)

# Vẽ nền cờ 
pen.penup()
pen.goto(-450, 300)
pen.pendown()
pen.color("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(900)
    pen.right(90)
    pen.forward(600)
    pen.right(90)
pen.end_fill()

# Hàm vẽ ngôi sao vàng 
def draw_star(center_x, center_y, size):
    pen.penup()
    pen.goto(center_x, center_y)
    pen.setheading(-90)  # Hướng đầu bút xuống dưới
    pen.forward(size / 2)
    pen.setheading(0)  # Hướng đầu bút sang phải
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Vẽ ngôi sao vàng ở giữa lá cờ, lệch sang trái một chút
draw_star(-110,150, 220)

# Thêm dòng chữ "Mừng Quốc Khánh Nước CHXHCN Việt Nam"
pen.penup()
pen.goto(0, -190) 
pen.setheading(0)
pen.color("yellow")
pen.write("Mừng Quốc Khánh Nước CHXHCN Việt Nam\n", align="center", font=("Arial", 20, "bold"))
pen.write("2/9/1945 - 2/9/2024", align="center", font=("Arial", 20, "bold"))

pen.hideturtle()
turtle.done()
