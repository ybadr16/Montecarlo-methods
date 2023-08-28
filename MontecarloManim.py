import numpy as np
#I am using manimgl, but you can definitely do this with manim ce, just remove "lib" and switch all ShowCreation to Create
from manimlib import *
#use manimgl -w -o -c BLACK --show_animation_progress MontecarloManim.py  to run.


'''
This animation is created to animate the montecarlo algorithm i explain in my serious "Monte carlo methods",
if you are not an arabic speaker the series probably is not relevant to you, but this code is pretty self contained.
'''

class Pi(Scene):
    def construct(self):
        r = 3
        N = int(1e5) #More points = more accurate results = more computational time

        #Crafting randomly generated dots coordinates
        x = np.random.uniform(-r, r, N)
        y = np.random.uniform(-r, r, N)
        is_inside = x**2 + y**2 <= r**2  #True for every randomly generated point that is inside the circle

        #Creating circle and square to set the scene for the dots
        square = Rectangle(height =2*r, width= 2*r, color = GREY)
        self.play(ShowCreation(square))
        circle = Circle(radius = r)
        self.play(ShowCreation(circle))
        #Initializing groups to add multiple randomly generated points at once
        inside_dots = VGroup()
        outside_dots = VGroup()
        is_circle = []
        pi = 0 #unnecessary, really, I use it for testing
        #initializing the value of pi as 0, as well as creating the text and the decimal number
        pi_anim = DecimalNumber(0, num_decimal_places=7).scale(0.5)
        pi_anim.move_to([1.6, 3.7, 0])
        text = Text("Current Value of pi:").scale(0.5)
        text.move_to([-1.3, 3.7, 0])
        self.play(ShowCreation(text))
        self.play(ShowCreation(pi_anim))
        step = 500
        '''
        The big loop is used for two things: Adding a chunk of points at once, and calculating pi after that chunk is added
        The nested loop adds dots by iterating through the previously created x & y arrays, and using them as coordinates
        for the created dots
        '''
        for i in range(0, N, step):
            for j in range(step):
                dot = Dot().scale(0.2)
                dot.move_to([x[i+j], y[i+j], 0])
                if is_inside[i+j]:
                    inside_dots.add(dot)   # Add inside dots to one group
                    is_circle.append(True) #This is to update the value of pi
                else:
                    outside_dots.add(dot)  # Add outside dots to another group

            pi2 = pi + 4* np.sum(is_circle)/(i+step)
            '''
            Like i said before, pi is useless, The other part just represensts "Area of circle" / "Area of square" multiplied by 4
            This is because pi * r^2 / 4 * r^2 is the ratio, so to calculate pi you would multiply by 4 the other side
            '''
            inside_dots.set_color(RED_E)
            outside_dots.set_color(BLUE_B)
            self.add(inside_dots, outside_dots)  # Add both groups in each iteration
            self.add(pi_anim.set_value(pi2))
            self.wait(0.35) #Sets the speed of the animation. Without it, the points would all be added at once


        self.wait()


