from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP
from random import shuffle

config.video_dir = "./videos"

def piramyd(n):
    return VGroup(*[
        VGroup(*[Square() for _ in range(j)]).arrange(RIGHT,buff=0)
        for j in range(1, n+1)
    ]).arrange(DOWN,buff=0)

class DemoScene(PresentationScene):

    def end_fragment_loop(self):
        self.end_fragment(fragment_type=COMPLETE_LOOP)
        self.end_fragment()

    def construct(self):
        title = Tex("This is a presentation made in \\sc Manim-Slides", color=WHITE)
        title_ul = Underline(title)
        title_ul_bk = Rectangle(width=title.width,height=title.height*1.6)\
            .next_to(title_ul,DOWN,buff=0)\
            .set_style(fill_opacity=1,stroke_width=0,fill_color=BLACK)
        vg_title = VGroup(title_ul_bk,title_ul)
        p = piramyd(7)
        p.set(height=config.frame_height-3)
        down_brace1 = Brace(p,DOWN)
        down_brace1_label = down_brace1.get_tex("n")
        left_brace1 = Brace(p,LEFT)
        left_brace2_label = left_brace1.get_tex("n")
        mobs = [subsubmob for submob in p for subsubmob in submob]
        shuffle(mobs)

        self.play(Write(title))
        self.wait()
        self.play(GrowFromCenter(title_ul))


        self.add(vg_title)
        self.play(vg_title.animate.shift(UP*title_ul_bk.height))
        self.play(ShrinkToCenter(title_ul))
        self.remove(vg_title,title)
        self.wait()


        self.end_fragment() # <- Pause here
        # Start loop here

        self.play(LaggedStart(*list(map(Create,mobs))))

        self.end_fragment_loop() # <- End loop here

        self.play(
                GrowFromCenter(down_brace1),Write(down_brace1_label),
                GrowFromCenter(left_brace1),Write(left_brace2_label),
        )

        self.wait(0.5)
        self.play(p.animate.arrange(DOWN,buff=0,aligned_edge=LEFT))

        self.end_fragment()

        p_ = p.copy()
        self.add(p_)
        self.play(
                p.animate.to_edge(LEFT,buff=2).set_fill(color=RED,opacity=1),
                p_.animate.to_edge(RIGHT,buff=2).set_fill(color=BLUE,opacity=1),
                FadeOut(down_brace1),
                FadeOut(down_brace1_label),
                FadeOut(left_brace1),
                FadeOut(left_brace2_label),
                )

        self.end_fragment()

        del down_brace1, down_brace1_label, left_brace1, left_brace2_label
        self.wait(0.5)
        self.play(
                Rotate(p_,PI,about_point=p_.get_center()),
                run_time=1.7
                # Rotating(p_,PI/2,about_point=p.get_corner(UR))
                )
        self.wait(0.5)
        self.play(
            p.animate.move_to(ORIGIN+LEFT*p[0].width/2),
            p_.animate.move_to(ORIGIN+RIGHT*p[0].width/2),
                )
        down_brace1 = Brace(VGroup(p,p_),DOWN)
        down_brace1_label = down_brace1.get_tex("n+1")
        left_brace1 = Brace(VGroup(p,p_),LEFT)
        left_brace2_label = left_brace1.get_tex("n")
        self.play(
                GrowFromCenter(down_brace1),Write(down_brace1_label),
                GrowFromCenter(left_brace1),Write(left_brace2_label),
        )
        all_mobs = VGroup(*[vmob for vmob in self.mobjects if isinstance(vmob, VMobject)])
        self.wait(0.5)
        self.play(all_mobs.animate.to_edge(LEFT))
        formula = MathTex("\\sum_{i=1}^{n}i={","n","(","n+1",")","\\over 2}")
        formula.scale(1.2)
        formula.to_edge(RIGHT,buff=2)
        self.wait(0.5)
        self.play(
                Write(formula[0]),
                Write(formula[2]),
                Write(formula[4:]),
                TransformFromCopy(left_brace2_label[0], formula[1]),
                TransformFromCopy(down_brace1_label[0], formula[3]),
                run_time=4
                )
        self.wait(2)
        self.end_fragment()

