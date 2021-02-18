from graphics import *

win = GraphWin("Sudoku", 370, 370)
win.setBackground("black")

def welcome():
    welcome = Text(Point(185,100),"Welcome to Star Sudoku!").draw(win)
    welcome.setFace("helvetica")
    welcome.setStyle("bold")
    welcome.setSize(20)
    welcome.setTextColor("purple")

    instructions = Text(Point(185,185), '''Fill the grid so that each triangle, each horizontal row, 
    and each slanted row contains the digits 1 through 9,
    so the middle rows are expanded over the empty hexagon
    in the middle and the short rows at the edge are 
    completed with the outer cornes of the triangles. 
    \nClick to continue.''')
    instructions.setFace("helvetica")
    instructions.setSize(10)
    instructions.setTextColor("purple")
    instructions.draw(win)

    if win.getMouse():
       welcome.undraw()
       instructions.undraw()

def triangle_pink():
    form_1 = Polygon(Point(211,51.3), Point(236,7), Point(262,51.3)).draw(win)
    form_1.getPoints()
    form_1.setOutline('pink')
    form_1.clone().draw(win).move(-25,44) 
    form_1.clone().draw(win).move(26,44)
    form_1.clone().draw(win).move(-50,88)
    form_1.clone().draw(win).move(0,88)
    form_1.clone().draw(win).move(52,88)

def entries_pink():
    Entry(Point(185,120),1).draw(win) # Entry for number 1
    Entry(Point(212,78),1).draw(win) # Entry for number 2
    Entry(Point(262,110),1).draw(win) # Entry for number 6
    Entry(Point(262,78),1).draw(win) # Entry for number 7
    Entry(Point(237,120),1).draw(win) # Entry for number 8

def num_pink():
    num_3 = Text(Point(236,69),"3").draw(win)
    num_3.setTextColor("white")
    num_3.setStyle("bold")

    num_4 = Text(Point(236,33),"4").draw(win)
    num_4.setTextColor("white")
    num_4.setStyle("bold")

    num_5 = Text(Point(288,121),"5").draw(win)
    num_5.setTextColor("white")
    num_5.setStyle("bold")

    num_9 = Text(Point(211,112),"9").draw(win)
    num_9.setTextColor("white")
    num_9.setStyle("bold")

def triangle_green():
    form_2 = Polygon(Point(60,51.3), Point(85,94.6), Point(111,51.3)).draw(win)
    form_2.getPoints()
    form_2.setOutline('green')
    form_2.clone().draw(win).move(49,0)
    form_2.clone().draw(win).move(99,0)
    form_2.clone().draw(win).move(24,44)
    form_2.clone().draw(win).move(74,44)
    form_2.clone().draw(win).move(49,88)

def entries_green():
    Entry(Point(160,110),1).draw(win) # Entry for number 4
    Entry(Point(110,78),1).draw(win) # Entry for number 5
    Entry(Point(135,157),1).draw(win) # Entry for number 7
    Entry(Point(135,70),1).draw(win) # Entry for number 8
    Entry(Point(160,78),1).draw(win) # Entry for number 9

def num_green():
    num_1 = Text(Point(184,70),"1").draw(win)
    num_1.setTextColor("white")
    num_1.setStyle("bold")

    num_2 = Text(Point(109,112),"2").draw(win)
    num_2.setTextColor("white")
    num_2.setStyle("bold")

    num_3 = Text(Point(135,121),"3").draw(win)
    num_3.setTextColor("white")
    num_3.setStyle("bold")

    num_6 = Text(Point(85,70),"6").draw(win)
    num_6.setTextColor("white")
    num_6.setStyle("bold")

def triangle_orange():
    form_1 = Polygon(Point(59,139.3), Point(85,94.6), Point(110,139.3)).draw(win)
    form_1.getPoints()
    form_1.setOutline('orange')
    form_1.clone().draw(win).move(-26,45)
    form_1.clone().draw(win).move(24, 45)
    form_1.clone().draw(win).move(-52, 90)
    form_1.clone().draw(win).move(-1, 90)
    form_1.clone().draw(win).move(49, 90)

def entries_orange():
    Entry(Point(85,157),1).draw(win) # Entry for number 3
    Entry(Point(59,166),1).draw(win) # Entry for number 4
    Entry(Point(85,210),1).draw(win) # Entry for number 6
    Entry(Point(85,120),1).draw(win) # Entry for number 7
    Entry(Point(135,210),1).draw(win) # Entry for number 8

def num_orange():
    num_1 = Text(Point(33,210),"1").draw(win)
    num_1.setTextColor("white")
    num_1.setStyle("bold")

    num_2 = Text(Point(109,165),"2").draw(win)
    num_2.setTextColor("white")
    num_2.setStyle("bold")
    
    num_5 = Text(Point(108,202),"5").draw(win)
    num_5.setTextColor("white")
    num_5.setStyle("bold")
  
    num_9 = Text(Point(58,202),"9").draw(win)
    num_9.setTextColor("white")
    num_9.setStyle("bold")

def triangle_purple():
    form_2 = Polygon(Point(58,230.3), Point(85,273.6), Point(109,230.3)).draw(win)
    form_2.getPoints()
    form_2.setOutline('purple')
    form_2.clone().draw(win).move(51,0)
    form_2.clone().draw(win).move(102,0)
    form_2.clone().draw(win).move(27,45)
    form_2.clone().draw(win).move(78,45)
    form_2.clone().draw(win).move(54,90)

def entries_purple():
    Entry(Point(185,246),1).draw(win)
    Entry(Point(109,256),1).draw(win)
    Entry(Point(110,290),1).draw(win)
    Entry(Point(85,246),1).draw(win)
    Entry(Point(162,290),1).draw(win)

def num_purple():
    num_1 = Text(Point(160,254),"1").draw(win)
    num_1.setTextColor("white")
    num_1.setStyle("bold")

    num_2 = Text(Point(136,300),"2").draw(win)
    num_2.setTextColor("white")
    num_2.setStyle("bold")

    num_3 = Text(Point(136,336),"3").draw(win)
    num_3.setTextColor("white")
    num_3.setStyle("bold")

    num_6 = Text(Point(136,248),"6").draw(win)
    num_6.setTextColor("white")
    num_6.setStyle("bold")

def triangle_cyan():
    form_1 = Polygon(Point(212,230.3), Point(236,187), Point(263,230.3)).draw(win)
    form_1.getPoints()
    form_1.setOutline('cyan')
    form_1.clone().draw(win).move(-24,44)
    form_1.clone().draw(win).move(27,44)
    form_1.clone().draw(win).move(-48,88)
    form_1.clone().draw(win).move(3,88)
    form_1.clone().draw(win).move(54,88)

def entries_cyan():
    Entry(Point(215,290),1).draw(win)
    Entry(Point(236,210),1).draw(win)
    Entry(Point(190,300),1).draw(win)
    Entry(Point(264,256),1).draw(win)
    Entry(Point(240,300),1).draw(win)

def num_cyan():
    num_2 = Text(Point(238,248),"2").draw(win)
    num_2.setTextColor("white")
    num_2.setStyle("bold")

    num_5 = Text(Point(291,298),"5").draw(win)
    num_5.setTextColor("white")
    num_5.setStyle("bold")
   
    num_6 = Text(Point(265,292),"6").draw(win)
    num_6.setTextColor("white")
    num_6.setStyle("bold")
   
    num_9 = Text(Point(213,254),"9").draw(win)
    num_9.setTextColor("white")
    num_9.setStyle("bold")

def triangle_yellow():  
    form_2 = Polygon(Point(210,140), Point(236,184.6), Point(261,140)).draw(win)
    form_2.getPoints()
    form_2.setOutline('yellow')
    form_2.clone().draw(win).move(51,0)
    form_2.clone().draw(win).move(102,0)
    form_2.clone().draw(win).move(27,45)
    form_2.clone().draw(win).move(78,45)
    form_2.clone().draw(win).move(54,90)

def entries_yellow():
    Entry(Point(315,202),1).draw(win)
    Entry(Point(289,246),1).draw(win)
    Entry(Point(288,210),1).draw(win)
    Entry(Point(236,157),1).draw(win)
    Entry(Point(287,157),1).draw(win)

def num_yellow():
    num_1 = Text(Point(337,158),"1").draw(win)
    num_1.setTextColor("white")
    num_1.setStyle("bold")

    num_6 = Text(Point(262,165),"6").draw(win)
    num_6.setTextColor("white")
    num_6.setStyle("bold")

    num_7 = Text(Point(262,202),"7").draw(win)
    num_7.setTextColor("white")
    num_7.setStyle("bold")

    num_9 = Text(Point(312,165),"9").draw(win)
    num_9.setTextColor("white")
    num_9.setStyle("bold")

def game():
    triangle_pink()
    entries_pink()
    num_pink()
    triangle_green()
    entries_green()
    num_green()
    triangle_orange()
    entries_orange()
    num_orange()
    triangle_purple()
    entries_purple()
    num_purple()
    triangle_cyan()
    entries_cyan()
    num_cyan()
    triangle_yellow()
    entries_yellow()
    num_yellow()

    win.getMouse()

if __name__ == '__main__':
    welcome()
    game()