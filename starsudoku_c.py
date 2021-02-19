from graphics import *

class Game():
    def __init__ (self):
        self.win = GraphWin("Sudoku", 370, 370)
        self.win.setBackground("black")

        self.welcome = Text(Point(185,100),"Welcome to Star Sudoku!")
        self.welcome.setFace("helvetica")
        self.welcome.setStyle("bold")
        self.welcome.setSize(20)
        self.welcome.setTextColor("purple")
        self.welcome.draw(self.win)

        self.instructions = Text(Point(185,185), '''Fill the grid so that each triangle, each horizontal row, 
        and each slanted row contains the digits 1 through 9,
        so the middle rows are expanded over the empty hexagon
        in the middle and the short rows at the edge are 
        completed with the outer cornes of the triangles. 
        \nClick to continue.''')
        self.instructions.setFace("helvetica")
        self.instructions.setSize(10)
        self.instructions.setTextColor("purple")
        self.instructions.draw(self.win)

        if self.win.getMouse():
            self.welcome.undraw()
            self.instructions.undraw()
        
        self.triangle_pink = Polygon(Point(211,51.3), Point(236,7), Point(262,51.3)).draw(self.win)
        self.triangle_pink.getPoints()
        self.triangle_pink.setOutline('pink')
        self.triangle_pink.clone().draw(self.win).move(-25,44) 
        self.triangle_pink.clone().draw(self.win).move(26,44)
        self.triangle_pink.clone().draw(self.win).move(-50,88)
        self.triangle_pink.clone().draw(self.win).move(0,88)
        self.triangle_pink.clone().draw(self.win).move(52,88)
    
        self.triangle_green = Polygon(Point(60,51.3), Point(85,94.6), Point(111,51.3)).draw(self.win)
        self.triangle_green.getPoints()
        self.triangle_green.setOutline('green')
        self.triangle_green.clone().draw(self.win).move(49,0)
        self.triangle_green.clone().draw(self.win).move(99,0)
        self.triangle_green.clone().draw(self.win).move(24,44)
        self.triangle_green.clone().draw(self.win).move(74,44)
        self.triangle_green.clone().draw(self.win).move(49,88)

        self.triangle_orange = Polygon(Point(59,139.3), Point(85,94.6), Point(110,139.3)).draw(self.win)
        self.triangle_orange.getPoints()
        self.triangle_orange.setOutline('orange')
        self.triangle_orange.clone().draw(self.win).move(-26,45)
        self.triangle_orange.clone().draw(self.win).move(24, 45)
        self.triangle_orange.clone().draw(self.win).move(-52, 90)
        self.triangle_orange.clone().draw(self.win).move(-1, 90)
        self.triangle_orange.clone().draw(self.win).move(49, 90)

        self.triangle_purple = Polygon(Point(58,230.3), Point(85,273.6), Point(109,230.3)).draw(self.win)
        self.triangle_purple.getPoints()
        self.triangle_purple.setOutline('purple')
        self.triangle_purple.clone().draw(self.win).move(51,0)
        self.triangle_purple.clone().draw(self.win).move(102,0)
        self.triangle_purple.clone().draw(self.win).move(27,45)
        self.triangle_purple.clone().draw(self.win).move(78,45)
        self.triangle_purple.clone().draw(self.win).move(54,90)

        self.triangle_cyan = Polygon(Point(212,230.3), Point(236,187), Point(263,230.3)).draw(self.win)
        self.triangle_cyan.getPoints()
        self.triangle_cyan.setOutline('cyan')
        self.triangle_cyan.clone().draw(self.win).move(-24,44)
        self.triangle_cyan.clone().draw(self.win).move(27,44)
        self.triangle_cyan.clone().draw(self.win).move(-48,88)
        self.triangle_cyan.clone().draw(self.win).move(3,88)
        self.triangle_cyan.clone().draw(self.win).move(54,88)

        self.triangle_yellow = Polygon(Point(210,140), Point(236,184.6), Point(261,140)).draw(self.win)
        self.triangle_yellow.getPoints()
        self.triangle_yellow.setOutline('yellow')
        self.triangle_yellow.clone().draw(self.win).move(51,0)
        self.triangle_yellow.clone().draw(self.win).move(102,0)
        self.triangle_yellow.clone().draw(self.win).move(27,45)
        self.triangle_yellow.clone().draw(self.win).move(78,45)
        self.triangle_yellow.clone().draw(self.win).move(54,90)

        self.entry_num = [Entry(Point(185,120),1).draw(self.win), 
                          Entry(Point(212,78),1).draw(self.win),
                          Entry(Point(262,110),1).draw(self.win), 
                          Entry(Point(262,78),1).draw(self.win), 
                          Entry(Point(237,120),1).draw(self.win), 
                          Entry(Point(160,110),1).draw(self.win), 
                          Entry(Point(110,78),1).draw(self.win), 
                          Entry(Point(135,157),1).draw(self.win), 
                          Entry(Point(135,70),1).draw(self.win),
                          Entry(Point(160,78),1).draw(self.win),
                          Entry(Point(85,157),1).draw(self.win), 
                          Entry(Point(59,166),1).draw(self.win), 
                          Entry(Point(85,210),1).draw(self.win), 
                          Entry(Point(85,120),1).draw(self.win), 
                          Entry(Point(135,210),1).draw(self.win),   
                          Entry(Point(185,246),1).draw(self.win),
                          Entry(Point(109,256),1).draw(self.win),
                          Entry(Point(110,290),1).draw(self.win),
                          Entry(Point(85,246),1).draw(self.win),
                          Entry(Point(162,290),1).draw(self.win),
                          Entry(Point(315,202),1).draw(self.win),
                          Entry(Point(289,246),1).draw(self.win),
                          Entry(Point(288,210),1).draw(self.win),
                          Entry(Point(236,157),1).draw(self.win),
                          Entry(Point(287,157),1).draw(self.win),
                          Entry(Point(215,290),1).draw(self.win),
                          Entry(Point(236,210),1).draw(self.win),
                          Entry(Point(190,300),1).draw(self.win),
                          Entry(Point(264,256),1).draw(self.win),
                          Entry(Point(240,300),1).draw(self.win)]

        self.numbers = [Text(Point(236,69),"3").draw(self.win).setTextColor("white"),
                        Text(Point(236,33),"4").draw(self.win).setTextColor("white"),
                        Text(Point(288,121),"5").draw(self.win).setTextColor("white"),
                        Text(Point(211,112),"9").draw(self.win).setTextColor("white"),
                        Text(Point(184,70),"1").draw(self.win).setTextColor("white"),
                        Text(Point(109,112),"2").draw(self.win).setTextColor("white"),
                        Text(Point(135,121),"3").draw(self.win).setTextColor("white"),
                        Text(Point(85,70),"6").draw(self.win).setTextColor("white"),
                        Text(Point(33,210),"1").draw(self.win).setTextColor("white"),
                        Text(Point(109,165),"2").draw(self.win).setTextColor("white"),
                        Text(Point(108,202),"5").draw(self.win).setTextColor("white"),
                        Text(Point(58,202),"9").draw(self.win).setTextColor("white"),
                        Text(Point(160,254),"1").draw(self.win).setTextColor("white"),
                        Text(Point(136,300),"2").draw(self.win).setTextColor("white"),
                        Text(Point(136,336),"3").draw(self.win).setTextColor("white"),
                        Text(Point(136,248),"6").draw(self.win).setTextColor("white"),
                        Text(Point(238,248),"2").draw(self.win).setTextColor("white"),
                        Text(Point(291,298),"5").draw(self.win).setTextColor("white"),
                        Text(Point(265,292),"6").draw(self.win).setTextColor("white"),
                        Text(Point(213,254),"9").draw(self.win).setTextColor("white"),
                        Text(Point(337,158),"1").draw(self.win).setTextColor("white"),
                        Text(Point(262,165),"6").draw(self.win).setTextColor("white"),
                        Text(Point(262,202),"7").draw(self.win).setTextColor("white"),
                        Text(Point(312,165),"9").draw(self.win).setTextColor("white")]

        if self.win.getMouse():
            self.triangle_pink
            self.triangle_purple
            self.triangle_orange
            self.triangle_purple
            self.triangle_cyan
            self.triangle_yellow
            self.entry_num
            self.numbers

inter = Game()