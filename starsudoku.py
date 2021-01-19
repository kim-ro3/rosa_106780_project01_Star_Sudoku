from graphics import *

win = GraphWin("Sudoku", 370, 370)
win.setBackground("black")

def welcome():
    welcome = Text(Point(185,100),"Welcome to Star Sudoku!")
    welcome.setFace("helvetica")
    welcome.setStyle("bold")
    welcome.setSize(20)
    welcome.setTextColor("purple")
    welcome.draw(win)

    instructions = Text(Point(185,185), "Fill the grid so that each triangle, each horizontal row,\n and each slanted row contains the digits 1 through 9,\nso the middle rows are expanded over the empty hexagon\nin the middle and the short rows at the edge are\n completed with the outer cornes of the triangles.\n\nClick to continue.")
    instructions.setFace("helvetica")
    instructions.setSize(10)
    instructions.setTextColor("purple")
    instructions.draw(win)

    if win.getMouse():
       welcome.undraw()
       instructions.undraw()

def triangle_pink():
    form_1 = Polygon(Point(211,51.3), Point(236,7), Point(262,51.3))
    form_1.getPoints()
    form_1.setOutline('pink')
    form_1.draw(win)

    triangle1 = form_1.clone()
    triangle1.move(-25, 44)
    triangle1.draw(win)

    triangle2 = form_1.clone()
    triangle2.move(26, 44)
    triangle2.draw(win)

    triangle3 = form_1.clone()
    triangle3.move(-50, 88)
    triangle3.draw(win)

    triangle4 = form_1.clone()
    triangle4.move(0, 88)
    triangle4.draw(win)

    triangle5 = form_1.clone()
    triangle5.move(52, 88)
    triangle5.draw(win)

    num_1 = (Entry(Point(185,120),1))
    num_1.draw(win)

    num_2 = (Entry(Point(212,78),1))
    num_2.draw(win)

    num_3 = Text(Point(236,69),"3")
    num_3.setTextColor("white")
    num_3.setStyle("bold")
    num_3.draw(win)

    num_4 = Text(Point(236,33),"4")
    num_4.setTextColor("white")
    num_4.setStyle("bold")
    num_4.draw(win)

    num_5 = Text(Point(288,121),"5")
    num_5.setTextColor("white")
    num_5.setStyle("bold")
    num_5.draw(win)

    num_6 = (Entry(Point(262,110),1))
    num_6.draw(win)

    num_7 = (Entry(Point(262,78),1))
    num_7.draw(win)

    num_8 = (Entry(Point(237,120),1))
    num_8.draw(win)

    num_9 = Text(Point(211,112),"9")
    num_9.setTextColor("white")
    num_9.setStyle("bold")
    num_9.draw(win)

def triangle_green():
    form_2 = Polygon(Point(60,51.3), Point(85,94.6), Point(111,51.3))
    form_2.getPoints()
    form_2.setOutline('green')
    form_2.draw(win)

    triangle1 = form_2.clone()
    triangle1.move(49,0)
    triangle1.draw(win)

    triangle2 = form_2.clone()
    triangle2.move(99,0)
    triangle2.draw(win)

    triangle3 = form_2.clone()
    triangle3.move(24, 44)
    triangle3.draw(win)

    triangle4 = form_2.clone()
    triangle4.move(74, 44)
    triangle4.draw(win)

    triangle5 = form_2.clone()
    triangle5.move(49, 88)
    triangle5.draw(win)

    num_1 = Text(Point(184,70),"1")
    num_1.setTextColor("white")
    num_1.setStyle("bold")
    num_1.draw(win)

    num_2 = Text(Point(109,112),"2")
    num_2.setTextColor("white")
    num_2.setStyle("bold")
    num_2.draw(win)

    num_3 = Text(Point(135,121),"3")
    num_3.setTextColor("white")
    num_3.setStyle("bold")
    num_3.draw(win)

    num_4 = (Entry(Point(160,110),1))
    num_4.draw(win)

    num_5 = (Entry(Point(110,78),1))
    num_5.draw(win)

    num_6 = Text(Point(85,70),"6")
    num_6.setTextColor("white")
    num_6.setStyle("bold")
    num_6.draw(win)

    num_7 = (Entry(Point(135,157),1))
    num_7.draw(win)

    num_8 = (Entry(Point(135,70),1))
    num_8.draw(win)

    num_9 = (Entry(Point(160,78),1))
    num_9.draw(win)

def triangle_orange():
    form_1 = Polygon(Point(59,139.3), Point(85,94.6), Point(110,139.3))
    form_1.getPoints()
    form_1.setOutline('orange')
    form_1.draw(win)

    triangle1  = form_1.clone()
    triangle1.move(-26, 45)
    triangle1.draw(win)

    triangle2 = form_1.clone()
    triangle2.move(24, 45)
    triangle2.draw(win)

    triangle3 = form_1.clone()
    triangle3.move(-52, 90)
    triangle3.draw(win)
 
    triangle4 = form_1.clone()
    triangle4.move(-1, 90)
    triangle4.draw(win)

    triangle5 = form_1.clone()
    triangle5.move(49, 90)
    triangle5.draw(win)

    num_1_green = Text(Point(33,210),"1")
    num_1_green.setTextColor("white")
    num_1_green.setStyle("bold")
    num_1_green.draw(win)

    num_2 = Text(Point(109,165),"2")
    num_2.setTextColor("white")
    num_2.setStyle("bold")
    num_2.draw(win)

    num_3 = (Entry(Point(85,157),1))
    num_3.draw(win)

    num_4 = (Entry(Point(59,166),1))
    num_4.draw(win)

    num_5 = Text(Point(108,202),"5")
    num_5.setTextColor("white")
    num_5.setStyle("bold")
    num_5.draw(win)

    num_6 = (Entry(Point(85,210),1))
    num_6.draw(win)

    num_7 = (Entry(Point(85,120),1))
    num_7.draw(win)

    num_8 = (Entry(Point(135,210),1))
    num_8.draw(win)

    num_9 = Text(Point(58,202),"9")
    num_9.setTextColor("white")
    num_9.setStyle("bold")
    num_9.draw(win)

def triangle_purple():
    form_2 = Polygon(Point(58,230.3), Point(85,273.6), Point(109,230.3))
    form_2.getPoints()
    form_2.setOutline('purple')
    form_2.draw(win)

    triangle1 = form_2.clone()
    triangle1.move(51, 0)
    triangle1.draw(win)
    
    triangle2 = form_2.clone()
    triangle2.move(102,0)
    triangle2.draw(win)

    triangle3 = form_2.clone()
    triangle3.move(27,45)
    triangle3.draw(win)

    triangle4 = form_2.clone()
    triangle4.move(78,45)
    triangle4.draw(win)
 
    triangle5 = form_2.clone()
    triangle5.move(54,90)
    triangle5.draw(win)

    num_1 = Text(Point(160,254),"1")
    num_1.setTextColor("white")
    num_1.setStyle("bold")
    num_1.draw(win)

    num_2 = Text(Point(136,300),"2")
    num_2.setTextColor("white")
    num_2.setStyle("bold")
    num_2.draw(win)

    num_3 = Text(Point(136,336),"3")
    num_3.setTextColor("white")
    num_3.setStyle("bold")
    num_3.draw(win)

    num_4 = (Entry(Point(185,246),1))
    num_4.draw(win)

    num_5 = (Entry(Point(109,256),1))
    num_5.draw(win)

    num_6 = Text(Point(136,248),"6")
    num_6.setTextColor("white")
    num_6.setStyle("bold")
    num_6.draw(win)

    num_7 = (Entry(Point(110,290),1))
    num_7.draw(win)

    num_8 = (Entry(Point(85,246),1))
    num_8.draw(win)

    num_9 = (Entry(Point(162,290),1))
    num_9.draw(win)

    

def triangle_cyan():
    form_1 = Polygon(Point(212,230.3), Point(236,187), Point(263,230.3))
    form_1.getPoints()
    form_1.setOutline('cyan')
    form_1.draw(win)

    triangle1 = form_1.clone()
    triangle1.move(-24, 44)
    triangle1.draw(win)

    triangle2 = form_1.clone()
    triangle2.move(27, 44)
    triangle2.draw(win)

    triangle3 = form_1.clone()
    triangle3.move(-48, 88)
    triangle3.draw(win)

    triangle4 = form_1.clone()
    triangle4.move(3, 88)
    triangle4.draw(win)

    triangle4 = form_1.clone()
    triangle4.move(54, 88)
    triangle4.draw(win)

    num_1 = (Entry(Point(215,290),1))
    num_1.draw(win)

    num_2 = Text(Point(238,248),"2")
    num_2.setTextColor("white")
    num_2.setStyle("bold")
    num_2.draw(win)

    num_3 = (Entry(Point(236,210),1))
    num_3.draw(win)

    num_4 = (Entry(Point(190,300),1))
    num_4.draw(win)

    num_5 = Text(Point(291,298),"5")
    num_5.setTextColor("white")
    num_5.setStyle("bold")
    num_5.draw(win)

    num_6 = Text(Point(265,292),"6")
    num_6.setTextColor("white")
    num_6.setStyle("bold")
    num_6.draw(win)

    num_7 = (Entry(Point(264,256),1))
    num_7.draw(win)

    num_8 = (Entry(Point(240,300),1))
    num_8.draw(win)

    num_9 = Text(Point(213,254),"9")
    num_9.setTextColor("white")
    num_9.setStyle("bold")
    num_9.draw(win)

def triangle_yellow():  
    form_2 = Polygon(Point(210,140), Point(236,184.6), Point(261,140))
    form_2.getPoints()
    form_2.setOutline('yellow')
    form_2.draw(win)

    triangle1 = form_2.clone()
    triangle1.move(51, 0)
    triangle1.draw(win)
    
    triangle2 = form_2.clone()
    triangle2.move(102,0)
    triangle2.draw(win)

    triangle3 = form_2.clone()
    triangle3.move(27,45)
    triangle3.draw(win)

    triangle4 = form_2.clone()
    triangle4.move(78,45)
    triangle4.draw(win)
 
    triangle5 = form_2.clone()
    triangle5.move(54,90)
    triangle5.draw(win)

    num_1 = Text(Point(337,158),"1")
    num_1.setTextColor("white")
    num_1.setStyle("bold")
    num_1.draw(win)

    num_2 = (Entry(Point(315,202),1))
    num_2.draw(win)

    num_3 = (Entry(Point(289,246),1))
    num_3.draw(win)

    num_4 = (Entry(Point(288,210),1))
    num_4.draw(win)

    num_5 = (Entry(Point(236,157),1))
    num_5.draw(win)

    num_6 = Text(Point(262,165),"6")
    num_6.setTextColor("white")
    num_6.setStyle("bold")
    num_6.draw(win)

    num_7 = Text(Point(262,202),"7")
    num_7.setTextColor("white")
    num_7.setStyle("bold")
    num_7.draw(win)

    num_8 = (Entry(Point(287,157),1))
    num_8.draw(win)

    num_9 = Text(Point(312,165),"9")
    num_9.setTextColor("white")
    num_9.setStyle("bold")
    num_9.draw(win)

def game():
    triangle_pink()
    triangle_green()
    triangle_orange()
    triangle_purple()
    triangle_cyan()
    triangle_yellow()

    win.getMouse()

if __name__ == '__main__':
    welcome()
    game()
