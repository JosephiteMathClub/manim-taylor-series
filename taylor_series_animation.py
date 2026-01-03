from manim import *
import numpy as np

class TaylorSeriesIntro(Scene):
    """Introduction to Taylor Series"""
    def construct(self):
        # Title
        title = Text("Taylor Series", font_size=60, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Taylor series formula
        formula = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n",
            font_size=50
        )
        formula.next_to(title, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(2)
        
        # Expanded form
        expanded = MathTex(
            r"f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots",
            font_size=36
        )
        expanded.next_to(formula, DOWN, buff=0.6)
        self.play(Write(expanded))
        self.wait(2)
        
        # Description
        description = Text(
            "Approximates any smooth function\nusing an infinite sum of polynomial terms",
            font_size=30,
            line_spacing=1.2
        )
        description.next_to(expanded, DOWN, buff=0.8)
        self.play(FadeIn(description))
        self.wait(3)
        
        # Fade out
        self.play(
            FadeOut(title),
            FadeOut(formula),
            FadeOut(expanded),
            FadeOut(description)
        )


class TaylorSeriesVisualization(Scene):
    """Visualize how Taylor series approximates a function"""
    def construct(self):
        # Setup axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE, "include_numbers": True}
        )
        axes.to_edge(DOWN, buff=0.5)
        
        # Labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)", edge=LEFT, direction=LEFT, buff=0.3)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait()
        
        # Title
        title = Text("Building a Taylor Series Approximation", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Example function: sin(x) around x=0
        func = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-4, 4])
        func_label = MathTex(r"f(x) = \sin(x)", color=YELLOW, font_size=35)
        func_label.next_to(axes, UP, buff=0.2).shift(LEFT * 3)
        
        self.play(Create(func), Write(func_label))
        self.wait()
        
        # Center point
        center_dot = Dot(axes.c2p(0, 0), color=RED)
        center_label = MathTex("a=0", color=RED, font_size=30)
        center_label.next_to(center_dot, DOWN + RIGHT, buff=0.1)
        self.play(Create(center_dot), Write(center_label))
        self.wait()
        
        # Taylor approximations
        colors = [RED, GREEN, BLUE, PURPLE, ORANGE]
        approximations = []
        
        # n=0: constant
        taylor_0 = axes.plot(lambda x: 0, color=colors[0], x_range=[-4, 4])
        label_0 = MathTex(r"P_0(x) = 0", color=colors[0], font_size=30)
        label_0.next_to(func_label, DOWN, aligned_edge=LEFT, buff=0.3)
        
        self.play(Create(taylor_0), Write(label_0))
        self.wait(2)
        approximations.append((taylor_0, label_0))
        
        # n=1: linear
        taylor_1 = axes.plot(lambda x: x, color=colors[1], x_range=[-2, 2])
        label_1 = MathTex(r"P_1(x) = x", color=colors[1], font_size=30)
        label_1.next_to(label_0, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.play(
            FadeOut(taylor_0),
            Create(taylor_1),
            FadeOut(label_0),
            Write(label_1)
        )
        self.wait(2)
        approximations.append((taylor_1, label_1))
        
        # n=3: cubic
        taylor_3 = axes.plot(
            lambda x: x - x**3/6, 
            color=colors[2], 
            x_range=[-3, 3]
        )
        label_3 = MathTex(r"P_3(x) = x - \frac{x^3}{6}", color=colors[2], font_size=30)
        label_3.next_to(label_1, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.play(
            FadeOut(taylor_1),
            Create(taylor_3),
            FadeOut(label_1),
            Write(label_3)
        )
        self.wait(2)
        
        # n=5
        taylor_5 = axes.plot(
            lambda x: x - x**3/6 + x**5/120,
            color=colors[3],
            x_range=[-3.5, 3.5]
        )
        label_5 = MathTex(r"P_5(x) = x - \frac{x^3}{6} + \frac{x^5}{120}", 
                         color=colors[3], font_size=30)
        label_5.next_to(label_3, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.play(
            FadeOut(taylor_3),
            Create(taylor_5),
            FadeOut(label_3),
            Write(label_5)
        )
        self.wait(2)
        
        # n=7
        taylor_7 = axes.plot(
            lambda x: x - x**3/6 + x**5/120 - x**7/5040,
            color=colors[4],
            x_range=[-4, 4]
        )
        label_7 = MathTex(
            r"P_7(x) = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040}",
            color=colors[4],
            font_size=26
        )
        label_7.next_to(label_5, DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.play(
            FadeOut(taylor_5),
            Create(taylor_7),
            FadeOut(label_5),
            Write(label_7)
        )
        self.wait(2)
        
        # Highlight convergence
        converge_text = Text("Getting closer to sin(x)!", font_size=35, color=GREEN)
        converge_text.next_to(axes, RIGHT, buff=0.5)
        self.play(Write(converge_text))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class SineExample(Scene):
    """Detailed example: sin(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: sin(x)", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula
        sine_formula = MathTex(
            r"\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1}",
            font_size=45
        )
        sine_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(sine_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \cdots",
            font_size=40
        )
        expanded.next_to(sine_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-2, 2, 1],
            x_length=11,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        # Custom x-axis labels
        x_labels = VGroup()
        for x_val in [-2*PI, -PI, 0, PI, 2*PI]:
            if x_val == -2*PI:
                label = MathTex(r"-2\pi", font_size=25)
            elif x_val == -PI:
                label = MathTex(r"-\pi", font_size=25)
            elif x_val == 0:
                label = MathTex(r"0", font_size=25)
            elif x_val == PI:
                label = MathTex(r"\pi", font_size=25)
            else:
                label = MathTex(r"2\pi", font_size=25)
            label.next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        self.play(Create(axes), Write(x_labels))
        
        # Actual sin(x)
        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-2*PI, 2*PI])
        sin_label = MathTex(r"\sin(x)", color=YELLOW, font_size=30)
        sin_label.move_to(axes.c2p(PI*1.3, 1.3))
        
        self.play(Create(sin_graph), Write(sin_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (1, lambda x: x, r"P_1", RED),
            (3, lambda x: x - x**3/6, r"P_3", GREEN),
            (5, lambda x: x - x**3/6 + x**5/120, r"P_5", BLUE),
            (7, lambda x: x - x**3/6 + x**5/120 - x**7/5040, r"P_7", PURPLE),
            (9, lambda x: x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880, r"P_9", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            # Determine range to avoid numerical issues
            x_range = [-min(2*PI, 3), min(2*PI, 3)] if n <= 5 else [-2*PI, 2*PI]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-PI*1.5, -1.3))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Final note
        note = Text("More terms = Better approximation!", font_size=30, color=GREEN)
        note.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class CosineExample(Scene):
    """Detailed example: cos(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: cos(x)", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula
        cosine_formula = MathTex(
            r"\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n}",
            font_size=45
        )
        cosine_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(cosine_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - \cdots",
            font_size=40
        )
        expanded.next_to(cosine_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-2, 2, 1],
            x_length=11,
            y_length=5,
            axis_config={"color": BLUE},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        # Custom x-axis labels
        x_labels = VGroup()
        for x_val in [-2*PI, -PI, 0, PI, 2*PI]:
            if x_val == -2*PI:
                label = MathTex(r"-2\pi", font_size=25)
            elif x_val == -PI:
                label = MathTex(r"-\pi", font_size=25)
            elif x_val == 0:
                label = MathTex(r"0", font_size=25)
            elif x_val == PI:
                label = MathTex(r"\pi", font_size=25)
            else:
                label = MathTex(r"2\pi", font_size=25)
            label.next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        self.play(Create(axes), Write(x_labels))
        
        # Actual cos(x)
        cos_graph = axes.plot(lambda x: np.cos(x), color=YELLOW, x_range=[-2*PI, 2*PI])
        cos_label = MathTex(r"\cos(x)", color=YELLOW, font_size=30)
        cos_label.move_to(axes.c2p(0, 1.3))
        
        self.play(Create(cos_graph), Write(cos_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (0, lambda x: 1, r"P_0", RED),
            (2, lambda x: 1 - x**2/2, r"P_2", GREEN),
            (4, lambda x: 1 - x**2/2 + x**4/24, r"P_4", BLUE),
            (6, lambda x: 1 - x**2/2 + x**4/24 - x**6/720, r"P_6", PURPLE),
            (8, lambda x: 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320, r"P_8", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-min(2*PI, 3), min(2*PI, 3)] if n <= 4 else [-2*PI, 2*PI]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-PI*1.5, -1.3))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Comparison note
        note = Text("Notice: Only even powers of x!", font_size=30, color=GREEN)
        note.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class LnExample(Scene):
    """Detailed example: ln(1+x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: ln(1+x)", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula
        ln_formula = MathTex(
            r"\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} x^{n}",
            font_size=45
        )
        ln_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(ln_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - \cdots",
            font_size=40
        )
        expanded.next_to(ln_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait()
        
        # Important note
        note = Text("Converges for -1 < x ≤ 1", font_size=30, color=RED)
        note.next_to(expanded, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-1, 1.5, 0.5],
            y_range=[-2, 1, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        self.play(Create(axes))
        
        # Actual ln(1+x)
        ln_graph = axes.plot(
            lambda x: np.log(1 + x),
            color=YELLOW,
            x_range=[-0.99, 1.5],
            use_smoothing=True
        )
        ln_label = MathTex(r"\ln(1+x)", color=YELLOW, font_size=30)
        ln_label.move_to(axes.c2p(1.2, 0.7))
        
        self.play(Create(ln_graph), Write(ln_label))
        self.wait()
        
        # Convergence point
        convergence_line = DashedLine(
            axes.c2p(1, -2),
            axes.c2p(1, 1),
            color=RED,
            dash_length=0.1
        )
        conv_label = Text("x = 1", font_size=25, color=RED)
        conv_label.next_to(axes.c2p(1, -2), DOWN, buff=0.2)
        
        self.play(Create(convergence_line), Write(conv_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (1, lambda x: x, r"P_1", RED),
            (2, lambda x: x - x**2/2, r"P_2", GREEN),
            (3, lambda x: x - x**2/2 + x**3/3, r"P_3", BLUE),
            (5, lambda x: x - x**2/2 + x**3/3 - x**4/4 + x**5/5, r"P_5", PURPLE),
            (10, lambda x: sum([(-1)**(n+1) * x**n / n for n in range(1, 11)]), r"P_{10}", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            # Stay within convergence radius for approximation
            x_range = [-0.95, 0.95] if n <= 5 else [-0.99, 0.99]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-0.7, -1.5))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Final observation
        observation = Text(
            "Series converges slowly\nnear x = 1",
            font_size=28,
            color=GREEN,
            line_spacing=1.2
        )
        observation.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ExponentialExample(Scene):
    """Bonus example: e^x Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: e^x", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula
        exp_formula = MathTex(
            r"e^{x} = \sum_{n=0}^{\infty} \frac{x^n}{n!}",
            font_size=45
        )
        exp_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(exp_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots",
            font_size=40
        )
        expanded.next_to(exp_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait()
        
        # Special property
        special = Text(
            "All derivatives equal e^x!\nConverges everywhere!",
            font_size=30,
            color=GREEN,
            line_spacing=1.2
        )
        special.next_to(expanded, DOWN, buff=0.4)
        self.play(Write(special))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-2, 3, 1],
            y_range=[-1, 8, 2],
            x_length=9,
            y_length=5,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        self.play(Create(axes))
        
        # Actual e^x
        exp_graph = axes.plot(lambda x: np.exp(x), color=YELLOW, x_range=[-2, 2.3])
        exp_label = MathTex(r"e^{x}", color=YELLOW, font_size=30)
        exp_label.move_to(axes.c2p(1.8, 7))
        
        self.play(Create(exp_graph), Write(exp_label))
        self.wait()
        
        # Progressive approximations
        import math
        
        def taylor_exp(x, n):
            return sum([x**k / math.factorial(k) for k in range(n+1)])
        
        terms = [
            (0, lambda x: 1, r"P_0", RED),
            (1, lambda x: 1 + x, r"P_1", GREEN),
            (2, lambda x: taylor_exp(x, 2), r"P_2", BLUE),
            (4, lambda x: taylor_exp(x, 4), r"P_4", PURPLE),
            (6, lambda x: taylor_exp(x, 6), r"P_6", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-2, min(2.3, 2)]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-1.5, 6))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Final note
        note = Text("Fastest converging series!", font_size=30, color=GREEN)
        note.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ArctanExample(Scene):
    """Detailed example: arctan(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: arctan(x)", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Formula
        arctan_formula = MathTex(
            r"\arctan(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} x^{2n+1}",
            font_size=45
        )
        arctan_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(arctan_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"\arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \frac{x^9}{9} - \cdots",
            font_size=40
        )
        expanded.next_to(arctan_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait()
        
        # Important note
        note = Text("Converges for -1 ≤ x ≤ 1", font_size=30, color=GREEN)
        note.next_to(expanded, DOWN, buff=0.3)
        fun_fact = Text("Used to calculate π! (Leibniz formula)", font_size=26, color=YELLOW)
        fun_fact.next_to(note, DOWN, buff=0.2)
        self.play(Write(note), Write(fun_fact))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        self.play(Create(axes))
        
        # Actual arctan(x)
        arctan_graph = axes.plot(
            lambda x: np.arctan(x),
            color=YELLOW,
            x_range=[-1.5, 1.5]
        )
        arctan_label = MathTex(r"\arctan(x)", color=YELLOW, font_size=30)
        arctan_label.move_to(axes.c2p(1.2, 0.8))
        
        self.play(Create(arctan_graph), Write(arctan_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (1, lambda x: x, r"P_1", RED),
            (3, lambda x: x - x**3/3, r"P_3", GREEN),
            (5, lambda x: x - x**3/3 + x**5/5, r"P_5", BLUE),
            (7, lambda x: x - x**3/3 + x**5/5 - x**7/7, r"P_7", PURPLE),
            (9, lambda x: x - x**3/3 + x**5/5 - x**7/7 + x**9/9, r"P_9", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-1.5, 1.5]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-1.2, -0.7))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Final observation
        observation = Text(
            "Only odd powers!",
            font_size=30,
            color=GREEN
        )
        observation.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class GeometricSeriesExample(Scene):
    """Detailed example: 1/(1-x) geometric series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: 1/(1-x)", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Subtitle
        subtitle = Text("(The Geometric Series)", font_size=35, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        self.wait()
        
        # Formula
        geo_formula = MathTex(
            r"\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n",
            font_size=45
        )
        geo_formula.next_to(subtitle, DOWN, buff=0.5)
        self.play(Write(geo_formula))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"\frac{1}{1-x} = 1 + x + x^2 + x^3 + x^4 + x^5 + \cdots",
            font_size=40
        )
        expanded.next_to(geo_formula, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait()
        
        # Important note
        note = Text("Converges ONLY for |x| < 1", font_size=30, color=RED)
        note.next_to(expanded, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-0.5, 2, 0.5],
            y_range=[-2, 10, 2],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.5)
        
        self.play(Create(axes))
        
        # Actual 1/(1-x)
        geo_graph = axes.plot(
            lambda x: 1/(1-x),
            color=YELLOW,
            x_range=[-0.5, 0.95],
            use_smoothing=False
        )
        geo_label = MathTex(r"\frac{1}{1-x}", color=YELLOW, font_size=30)
        geo_label.move_to(axes.c2p(0.7, 3.5))
        
        self.play(Create(geo_graph), Write(geo_label))
        self.wait()
        
        # Vertical line at x=1 (divergence)
        div_line = DashedLine(
            axes.c2p(1, -2),
            axes.c2p(1, 10),
            color=RED,
            dash_length=0.1
        )
        div_label = Text("x = 1\n(diverges)", font_size=22, color=RED, line_spacing=0.8)
        div_label.next_to(axes.c2p(1, -2), DOWN, buff=0.2)
        
        self.play(Create(div_line), Write(div_label))
        self.wait()
        
        # Progressive approximations
        def partial_sum(x, n):
            return sum([x**k for k in range(n+1)])
        
        terms = [
            (0, lambda x: 1, r"P_0", RED),
            (1, lambda x: 1 + x, r"P_1", GREEN),
            (2, lambda x: partial_sum(x, 2), r"P_2", BLUE),
            (4, lambda x: partial_sum(x, 4), r"P_4", PURPLE),
            (8, lambda x: partial_sum(x, 8), r"P_8", ORANGE)
        ]
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-0.5, 0.9]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range)
            taylor_label = MathTex(f"{label_text}", color=color, font_size=30)
            taylor_label.move_to(axes.c2p(-0.3, 8))
            
            if prev_graph:
                self.play(
                    Transform(prev_graph, taylor_graph),
                    Transform(prev_label, taylor_label)
                )
            else:
                self.play(Create(taylor_graph), Write(taylor_label))
                prev_graph = taylor_graph
                prev_label = taylor_label
            
            self.wait(2)
        
        # Final observation
        observation = Text(
            "Simplest Taylor series!\nBut limited range",
            font_size=26,
            color=GREEN,
            line_spacing=1.2
        )
        observation.next_to(axes, RIGHT, buff=0.3)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class HyperbolicExample(Scene):
    """Example: sinh(x) and cosh(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: Hyperbolic Functions", font_size=48, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Two columns for sinh and cosh
        sinh_title = Text("sinh(x)", font_size=40, color=RED)
        sinh_title.move_to(LEFT * 3.5 + UP * 2.5)
        
        cosh_title = Text("cosh(x)", font_size=40, color=BLUE)
        cosh_title.move_to(RIGHT * 3.5 + UP * 2.5)
        
        self.play(Write(sinh_title), Write(cosh_title))
        self.wait()
        
        # Formulas
        sinh_formula = MathTex(
            r"\sinh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}",
            font_size=32,
            color=RED
        )
        sinh_formula.next_to(sinh_title, DOWN, buff=0.3)
        
        cosh_formula = MathTex(
            r"\cosh(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}",
            font_size=32,
            color=BLUE
        )
        cosh_formula.next_to(cosh_title, DOWN, buff=0.3)
        
        self.play(Write(sinh_formula), Write(cosh_formula))
        self.wait()
        
        # Expanded forms
        sinh_expanded = MathTex(
            r"x + \frac{x^3}{3!} + \frac{x^5}{5!} + \cdots",
            font_size=28,
            color=RED
        )
        sinh_expanded.next_to(sinh_formula, DOWN, buff=0.3)
        
        cosh_expanded = MathTex(
            r"1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots",
            font_size=28,
            color=BLUE
        )
        cosh_expanded.next_to(cosh_formula, DOWN, buff=0.3)
        
        self.play(Write(sinh_expanded), Write(cosh_expanded))
        self.wait(2)
        
        # Key insight
        insight = Text(
            "Like sin/cos but with positive signs!",
            font_size=30,
            color=YELLOW
        )
        insight.next_to(sinh_expanded, DOWN, buff=0.5).shift(RIGHT * 1.5)
        self.play(Write(insight))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 2],
            x_length=10,
            y_length=4.5,
            axis_config={"color": GREY, "include_numbers": True},
            tips=False
        )
        axes.to_edge(DOWN, buff=0.3)
        
        self.play(Create(axes))
        
        # Actual functions
        sinh_graph = axes.plot(lambda x: np.sinh(x), color=RED, x_range=[-2.5, 2.5])
        cosh_graph = axes.plot(lambda x: np.cosh(x), color=BLUE, x_range=[-2.5, 2.5])
        
        sinh_label = MathTex(r"\sinh(x)", color=RED, font_size=28)
        sinh_label.move_to(axes.c2p(2, 3.5))
        
        cosh_label = MathTex(r"\cosh(x)", color=BLUE, font_size=28)
        cosh_label.move_to(axes.c2p(0, 3.5))
        
        self.play(
            Create(sinh_graph), Create(cosh_graph),
            Write(sinh_label), Write(cosh_label)
        )
        self.wait()
        
        # Show approximations
        import math
        
        # sinh approximation
        def sinh_approx(x, n):
            result = 0
            for k in range(n+1):
                result += x**(2*k+1) / math.factorial(2*k+1)
            return result
        
        # cosh approximation
        def cosh_approx(x, n):
            result = 0
            for k in range(n+1):
                result += x**(2*k) / math.factorial(2*k)
            return result
        
        terms = [(0, ORANGE), (1, PURPLE), (2, GREEN)]
        
        for n, color in terms:
            sinh_taylor = axes.plot(
                lambda x: sinh_approx(x, n),
                color=color,
                x_range=[-2.5, 2.5]
            )
            cosh_taylor = axes.plot(
                lambda x: cosh_approx(x, n),
                color=color,
                x_range=[-2.5, 2.5]
            )
            
            term_label = MathTex(f"n={n}", color=color, font_size=25)
            term_label.next_to(axes, RIGHT, buff=0.2)
            
            self.play(
                Create(sinh_taylor),
                Create(cosh_taylor),
                Write(term_label)
            )
            self.wait(1.5)
            
            if n < 2:
                self.play(
                    FadeOut(sinh_taylor),
                    FadeOut(cosh_taylor),
                    FadeOut(term_label)
                )
        
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class TaylorSeriesConclusion(Scene):
    """Summary and conclusion"""
    def construct(self):
        # Title
        title = Text("Taylor Series: Key Takeaways", font_size=50, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Key points
        points = VGroup(
            Text("1. Approximates functions using polynomials", font_size=32),
            Text("2. More terms → Better approximation", font_size=32),
            Text("3. Converges within radius of convergence", font_size=32),
            Text("4. Different functions converge at different rates", font_size=32),
        )
        points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        points.move_to(ORIGIN).shift(UP * 0.5)
        
        for point in points:
            self.play(Write(point))
            self.wait(1.5)
        
        self.wait()
        
        # Examples summary
        examples_title = Text("Examples Covered:", font_size=36, weight=BOLD)
        examples_title.next_to(points, DOWN, buff=0.8)
        self.play(Write(examples_title))
        
        examples = VGroup(
            MathTex(r"\sin(x), \cos(x), e^x", font_size=28),
            MathTex(r"\ln(1+x), \arctan(x)", font_size=28),
            MathTex(r"\frac{1}{1-x}, \sinh(x), \cosh(x)", font_size=28),
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        examples.next_to(examples_title, DOWN, buff=0.4)
        
        for example in examples:
            self.play(Write(example))
            self.wait(1)
        
        self.wait(3)
        
        # Final message
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        final = Text(
            "Taylor Series:\nThe Foundation of Mathematical Analysis",
            font_size=45,
            line_spacing=1.3,
            weight=BOLD
        )
        self.play(Write(final))
        self.wait(3)
        
        self.play(FadeOut(final))



