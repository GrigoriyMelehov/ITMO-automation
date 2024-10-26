from task_9_checks import *

class Input(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Tittle(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

A_1 = Input('add1', '/add2')
A_2 = Button('add3', '/add4')
A_3 = Tittle('add5', '/Add6')
A_4 = Link('add7', '/add8')

print(A_1.text, A_1.loc, A_3.loc, A_4.text)
print()
print(A_1.check_text(),A_2.check_text(),A_3.check_text(),A_4.check_text()) #выполнение условия доп.задания