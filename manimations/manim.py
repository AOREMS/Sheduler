from manim import *
import EDF_finished as EDF
import string



class CreateGrid(Scene):
    def construct(self):
        ax = Axes(x_range=[0,14,1],
                  y_range=[0,4,1],
                  x_axis_config={"include_numbers": True},
                  tips=False,
                  x_length=10)
        #punkte an den richtigen stellen hinmachen für deadlines
        point = ax.coords_to_point(2  , 2  )
        dot = Dot(point)
        self.add(ax , dot)
        letters = list(string.ascii_uppercase)
        ypos = []
        for  char in EDF.edf_1.shedule:
            if(char == '_'):
                ypos.append(-1) 
            else:
                ypos.append(letters.index(char))

        self.wait(2)
        rects  = VGroup()
        tasks = EDF.edf_1.id.keys()
        for i, letter in enumerate(tasks):
            l = Text(letter)
            ar = Arrow(start=DOWN, end= UP,color=GREEN)
            ar.scale(0.5)
            dr = Arrow(start=UP, end= DOWN,color=RED , buff=0.45)
            dr.to_corner([-1,-1,0])
            dr.shift( (i * UP + 0.25 * UP) , (EDF.t2.ts[i][2] * RIGHT) + RIGHT, 0 )
            ar.to_corner([-1,-1,0])
            ar.shift( (i * UP + 0.25 * UP) , (EDF.t2.ts[i][0] * RIGHT) + RIGHT, 0 )
            self.add(ar, dr)
            self.play(Write(l))
            l.to_corner([-1,-1,0])
            l.shift( (i * UP + 0.25 * UP) , 0 , 0 )
            self.add(l)

        for i,task in enumerate(EDF.edf_1.shedule):
            if task != '_':
                rec = Rectangle(height=1,width=1)
                rects.add(rec)
                rec.to_corner([-1,-1,0])
                rec.shift((ypos[i] * UP))
                self.play(rec.animate.shift( RIGHT * i + RIGHT))

        self.wait(5)




            

class TaskRectangle(Animation):
    def construct(self):
        self.play(Create(Rectangle(height=len(EDF.edf_1.id),width=1,grid_ystep=1)  ,run_time=2, func=smooth))

    def get_ypos(self):
        pass
    

