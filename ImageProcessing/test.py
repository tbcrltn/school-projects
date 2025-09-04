import turtle
from PIL import Image
t = turtle.Turtle()
img = Image.open("ImageProcessing/size200.jpg")


pixels = list(img.getdata())

width, height = img.size
image = [pixels[i * width:(i + 1) * width] for i in range(height)]



t.shape("circle")
print(image)
screen = turtle.Screen()
def draw(originx, originy):
    t.penup()
    t.goto(originx, originy)
    t.pendown()
    screen.tracer(0)
    t.speed(0)
    turtle.colormode(255)
    for row in image:
        for num in row:
            color = (num[0], num[1], num[2])
            t.color(color)
            t.forward(1)
        t.penup()
        t.goto(originx, t.ycor()-1)
        t.pendown()
        screen.update()
draw(-600, 400)
draw(-400, 400)
draw(-200, 400)


screen.tracer(1)
t.penup()
t.color("black")
t.right(90)
t.forward(200)
t.left(90)
t.forward(200)
t.pendown()
for x in range(4):
    t.right(90)
    t.forward(100)


def on_close():
    print("Window closed!")
    try:
        screen.bye()  
    except:
        pass

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.protocol("WM_DELETE_WINDOW", on_close)


while True:
    try:
        screen.update()  
    except turtle.Terminator:
        print("Turtle window terminated")
        break
    

