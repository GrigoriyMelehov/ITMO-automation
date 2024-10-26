class Pr_ug:

    def __init__(self, h, w):
        self.h = h
        self.w = w

    def ploshad(self):
        s = self.w * self.h
        print('площадь равна = ',s)

    def perim(self):
        p = self.w * 2 + self.h * 2
        print('периметр равен = ', p)

A_1 = Pr_ug(4,5)
A_2 = Pr_ug(2,4)
A_3 = Pr_ug(5,2)

A_1.perim()
A_2.perim()
A_3.perim()
A_1.ploshad()
A_2.ploshad()
A_3.ploshad()

class Math:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def addition(self):
        print('a+b= ', self.a + self.b)

    def multiplication(self):
        print('a*b= ', self.a * self.b)

    def division(self):
        print('a/b= ', self.a / self.b)

    def substraction(self):
        print('a-b= ', self.a - self.b)

B_1 = Math(3,5)
B_1.addition()
B_1.multiplication()
B_1.division()
B_1.substraction()

class Button:

    def __init__(self, text, type_button = 'Кнопка', loc = ''):
        self.text = text
        self.type_button = type_button
        self.loc = loc

    def click(self):
        return "Клик по кнопке {}".format(self.text)

But_1 = Button('Text Box')
But_2 = Button('Check Box')
But_3 = Button('Radio Button')
But_4 = Button('Web Tables')
But_5 = Button('Buttons')
But_6 = Button('Links')
But_7 = Button('Broken Links -Images')
But_8 = Button('Upload and Downloads')
But_9 = Button('Dynamic Properties')

print(But_1.text,But_2.text,But_3.text,But_4.text,But_5.text,But_6.text,But_7.text,But_8.text,But_9.text)
print(But_1.click(),But_2.click(),But_3.click(),But_4.click(),But_5.click(),But_6.click(),But_7.click(),But_8.click(),But_9.click())