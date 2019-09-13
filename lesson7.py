import turtle as t

t.bgcolor(0, 0, 0)
t.colormode(255)
t.speed(0)
t.hideturtle()
t.setposition(0.0, 0.0)
t.penup()
t.delay(5)

def drawRomb(a, b): # a - величина одной из вершин.

    t.pendown()
    t.right((180 - a) / 2)
    t.forward(b)
    t.right(a)
    t.forward(b)
    t.right(180 - a)
    t.forward(b)
    t.right(a)
    t.forward(b)
    t.right(((180 - a) / 2))
    t.penup()

cols = [x * 16  for x in range(0, 16)]
colsr = list(range(255, 0, -16))
zeros = [x * 0 for x in range(0, 16)]
z255s = [x * 0 + 255 for x in range(0, 16)]

numsr = z255s + colsr + zeros + zeros + cols + z255s
numsg = cols + z255s + z255s + colsr + zeros + zeros
numsb = zeros + zeros + cols + z255s + z255s + colsr

nums = list(zip(numsr, numsg, numsb))

print(len(nums))
i = 0
while i <= len(nums):
    # t.setx()
    t.pendown()
    t.pencolor(nums[i])
    t.color(nums[i])
    i += 1
    t.begin_fill()
    drawRomb(10, 200)
    t.end_fill()
    t.penup()
    if i == (len(nums) - 1):
        i = 0
    t.right(360/len(nums))
    #t.clear()

