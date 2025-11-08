import turtle as t
def number():
    a=int(input('enter a number:'))
    b=int(input('enter the second number'))
    c=a+b
    if c<10 :
        for x in range (4):
            t.fd(100)
            t.rt(90)
    elif 10<=c<15:
        t.circle (100)
    else:
        for n in range (3):
            t.fd(100)
            t.rt(120)
            t.reset()
            t.fd(50)
            t.rt(120)
            t.reset()
            t.fd(25)
            t.rt(120)
number()
