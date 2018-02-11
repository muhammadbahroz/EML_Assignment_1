class MyNameInitial(object):
    def __init__(self):
        """This CLASS only works with Print function"""
        import turtle
        self.seurat = turtle.Turtle()
        self.seurat.color('red')
        self.seurat.hideturtle()
        self.seurat.speed(200)
        self.seurat.screen.title("My Initials 'M.BAHROZ' :)")

    def _set_starting_pos(self):
        self.seurat.penup()
        self.seurat.goto(-100, 0)
        self.seurat.pendown()

    def _next_alphabet_pos(self, z, y=0):
        """ 'z' is the addition element and 'y' is the y-coordinate """
        x, u = self.seurat.pos()
        x = x + z
        self.seurat.penup()
        self.seurat.goto(x, y)
        self.seurat.left(90)
        self.seurat.pendown()

    def __str__(self):
        self._set_starting_pos()
        self.seurat.left(90)

        # Alphabet 'M'
        self.seurat.forward(100)
        self.seurat.right(170)
        self.seurat.forward(100)
        self.seurat.left(160)
        self.seurat.forward(100)
        self.seurat.right(170)
        self.seurat.forward(100)
        self.seurat.left(90)

        # next alphabet position
        self._next_alphabet_pos(z=15, y=50)

        # next alphabet '.'
        self.seurat.dot()
        self.seurat.left(-90)

        # next alphabet position
        self._next_alphabet_pos(z=15)

        # next alphabet 'B'
        self.seurat.forward(100)
        self.seurat.right(90)
        for i in range(19):
            self.seurat.forward(5)
            self.seurat.right(10)
        for i in range(14):
            self.seurat.backward(5)
            self.seurat.right(13)

        # next alphabet position
        self._next_alphabet_pos(z=40)

        # next alphabet 'A'
        self.seurat.forward(100)
        self.seurat.right(152)
        self.seurat.forward(50)
        self.seurat.right(107)
        self.seurat.forward(25)
        self.seurat.backward(25)
        self.seurat.right(-107)
        self.seurat.forward(50)
        self.seurat.left(74)

        # next alphabet position
        self._next_alphabet_pos(z=15)

        # next alphabet 'H'
        self.seurat.forward(100)
        self.seurat.backward(50)
        self.seurat.right(90)
        self.seurat.forward(25)
        self.seurat.left(90)
        self.seurat.forward(50)
        self.seurat.backward(100)
        self.seurat.right(90)

        # next alphabet position
        self._next_alphabet_pos(z=15)

        # next alphabet 'R'
        self.seurat.forward(100)
        self.seurat.right(90)
        for i in range(19):
            self.seurat.forward(5)
            self.seurat.right(10)
        self.seurat.right(45)
        self.seurat.backward(50)
        self.seurat.right(35)
        self.seurat.right(90)

        # next alphabet position
        self._next_alphabet_pos(z=15)

        # next alphabet 'O'
        self.seurat.penup()
        x, y = self.seurat.pos()
        x = x + 95
        # y = y + 50
        self.seurat.goto(x, 50)
        self.seurat.pendown()
        self.seurat.circle(50)
        # next alphabet position
        self._next_alphabet_pos(z=3)
        self.seurat.right(90)
        # next alphabet 'Z'
        self.seurat.penup()
        self.seurat.forward(100)
        self.seurat.pendown()
        self.seurat.right(90)
        self.seurat.forward(50)
        self.seurat.right(120)
        self.seurat.forward(120)
        self.seurat.right(-120)
        self.seurat.forward(65)
        from time import sleep
        sleep(1)
        return 'Printing Done'


a = MyNameInitial()
print(a)
