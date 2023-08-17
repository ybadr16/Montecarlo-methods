from manim import *
import random
import math

class BouncingDots(Scene):
    def construct(self):
        Sig_s = 0.2
        Sig_a = 0.2
        thickness = 2.5
        Sig_t = Sig_a + Sig_s
        iSig_t = 1 / Sig_t
        transmission = 0.0
        N = int(100)
        mu = 0
        l = 0

        rectangle = Rectangle(height=7, width=2.5, color=GRAY)
        rectangle.shift(RIGHT*3)
        rectangle.set_fill(BLUE, opacity=0.2)

        self.play(Create(rectangle))
        text = Variable(transmission,"Transmitted:").scale(0.2)
        self.play(Create(text))
        self.play(text.animate.move_to([-4,3,0]))



        for i in range(N):
            text.add_updater(lambda v: v.tracker.set_value(transmission))
            x = 0
            alive = 1
            dots3 = Dot(point = LEFT)
            self.play(Create(dots3), run_time = 0.2)
            self.play(dots3.animate.next_to(rectangle, LEFT, buff = 0), run_time = 0.2)


            while alive:

                # get distance to collision
                l = -math.log(1 - random.random()) * iSig_t
                # move particle
                x += l * math.cos(mu)
                x_distance = l * math.cos(mu)
                y_distance = l * math.sin(mu)
                self.play(dots3.animate.shift(RIGHT*x_distance, UP*y_distance), run_time = 0.2)
                print(x)

                # still in the slab?
                if x > thickness:
                    transmission += 1
                    print(transmission)
                    self.play(FadeOut(dots3))
                    alive = 0

                elif x < 0:
                    self.play(FadeOut(dots3), run_time = 0.2)
                    alive = 0

                else:
                    # scatter or absorb
                    if random.random() < Sig_s * iSig_t:
                        # scatter, pick new mu
                        mu = random.uniform(-180, 180)
                        print(mu)

                    else:
                        self.play(FadeOut(dots3))
                        # absorbed
                        alive = 0



        self.wait()



