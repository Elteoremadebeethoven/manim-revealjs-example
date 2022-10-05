from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP


config.video_dir= "./videos"

class DemoScene(PresentationScene):
    def construct(self):
        rect = Rectangle(fill_color=RED, fill_opacity=1)
        self.play(Create(rect))
        self.end_fragment()

        self.play(
            Rotate(rect, TAU, run_time=2, rate_func=linear)
        )
        self.end_fragment(fragment_type=COMPLETE_LOOP)
        self.end_fragment()

        self.play(rect.animate.shift(3*LEFT))
        self.end_fragment()

    def end_fragment_loop(self):
        self.end_fragment(fragment_type=COMPLETE_LOOP)
        self.end_fragment()
