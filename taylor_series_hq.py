from manim import *
import numpy as np

config.frame_width = 14
config.frame_height = 8
config.pixel_width = 1920
config.pixel_height = 1080

class TaylorSeriesIntro(Scene):
    """Introduction to Taylor Series"""
    def construct(self):
        # Opening statement
        opening = Text(
            "What if we could represent\nANY smooth function\nusing only polynomials?",
            font_size=48,
            line_spacing=1.3,
            weight=BOLD
        )
        self.play(Write(opening))
        self.wait(3)
        self.play(FadeOut(opening))
        
        # Title
        title = Text("Taylor Series", font_size=72, weight=BOLD, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait()
        
        # Subtitle
        subtitle = Text(
            "The Bridge Between Functions and Polynomials",
            font_size=36,
            color=BLUE
        )
        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        # Taylor series formula
        formula = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n",
            font_size=60
        )
        formula.move_to(UP * 0.5)
        self.play(Write(formula))
        self.wait(2)
        
        # Box around formula
        formula_box = SurroundingRectangle(formula, color=YELLOW, buff=0.3)
        self.play(Create(formula_box))
        self.wait()
        
        # Expanded form
        expanded = MathTex(
            r"f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots",
            font_size=42
        )
        expanded.move_to(DOWN * 1)
        self.play(Write(expanded))
        self.wait(2)
        
        # Description points
        desc1 = Text("• Infinite sum of polynomial terms", font_size=32)
        desc2 = Text("• Each term uses derivatives at point a", font_size=32)
        desc3 = Text("• More terms = Better approximation", font_size=32)
        
        descriptions = VGroup(desc1, desc2, desc3)
        descriptions.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        descriptions.move_to(DOWN * 2.8)
        
        for desc in descriptions:
            self.play(FadeIn(desc, shift=RIGHT * 0.5))
            self.wait(1)
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class TaylorSeriesVisualization(Scene):
    """Visualize how Taylor series approximates a function"""
    def construct(self):
        # Title
        title = Text("Building a Taylor Series Approximation", font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Function label
        func_label = MathTex(r"f(x) = \sin(x)", color=YELLOW, font_size=40)
        func_label.next_to(title, DOWN, buff=0.3).shift(LEFT * 4)
        
        # Setup axes - positioned lower to avoid text overlap
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE, "include_numbers": True}
        )
        axes.move_to(DOWN * 1.5)
        
        # Labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("f(x)", edge=LEFT, direction=LEFT, buff=0.3)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait()
        
        # Example function: sin(x) around x=0
        func = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-4, 4], stroke_width=5)
        
        self.play(Create(func), Write(func_label))
        self.wait()
        
        # Center point
        center_dot = Dot(axes.c2p(0, 0), color=RED, radius=0.08)
        center_label = MathTex("a=0", color=RED, font_size=32)
        center_label.next_to(center_dot, DOWN + RIGHT, buff=0.15)
        self.play(Create(center_dot), Write(center_label))
        self.wait()
        
        # Info box for current approximation
        info_box = Rectangle(height=1.5, width=5, color=WHITE, stroke_width=2)
        info_box.to_corner(UR, buff=0.5)
        info_title = Text("Current Approximation:", font_size=26, weight=BOLD)
        info_title.next_to(info_box.get_top(), DOWN, buff=0.2)
        
        self.play(Create(info_box), Write(info_title))
        
        # Taylor approximations
        colors = [RED, GREEN, BLUE, PURPLE, ORANGE]
        
        terms_data = [
            (0, lambda x: np.zeros_like(x) if hasattr(x, '__iter__') else 0, r"P_0(x) = 0"),
            (1, lambda x: x, r"P_1(x) = x"),
            (3, lambda x: x - x**3/6, r"P_3(x) = x - \frac{x^3}{6}"),
            (5, lambda x: x - x**3/6 + x**5/120, r"P_5(x) = x - \frac{x^3}{6} + \frac{x^5}{120}"),
            (7, lambda x: x - x**3/6 + x**5/120 - x**7/5040, r"P_7(x) = x - \frac{x^3}{6} + \frac{x^5}{120} - \frac{x^7}{5040}")
        ]
        
        prev_graph = None
        prev_label = None
        
        for idx, (n, func_expr, label_text) in enumerate(terms_data):
            color = colors[idx]
            x_range = [-4, 4] if n >= 5 else [-3, 3]
            
            taylor_graph = axes.plot(func_expr, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(label_text, color=color, font_size=24)
            taylor_label.next_to(info_title, DOWN, buff=0.3)
            
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
        
        # Highlight convergence
        converge_text = Text("Getting closer to sin(x)!", font_size=36, color=GREEN, weight=BOLD)
        converge_text.next_to(axes, DOWN, buff=0.6)
        self.play(Write(converge_text))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class SineExample(Scene):
    """Detailed example: sin(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: sin(x)", font_size=56, weight=BOLD, color=YELLOW)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Formula section
        sine_formula = MathTex(
            r"\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1}",
            font_size=42
        )
        sine_formula.next_to(title, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!} - \cdots",
            font_size=38
        )
        expanded.next_to(sine_formula, DOWN, buff=0.3)
        
        property_text = Text("Only odd powers! Alternating signs!", font_size=30, color=GREEN)
        property_text.next_to(expanded, DOWN, buff=0.25)
        
        self.play(Write(sine_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(property_text))
        self.wait(2)
        
        # Axes - positioned lower
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=11,
            y_length=3.5,
            axis_config={"color": BLUE},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        # Custom x-axis labels
        x_labels = VGroup()
        for x_val in [-2*PI, -PI, 0, PI, 2*PI]:
            if x_val == -2*PI:
                label = MathTex(r"-2\pi", font_size=28)
            elif x_val == -PI:
                label = MathTex(r"-\pi", font_size=28)
            elif x_val == 0:
                label = MathTex(r"0", font_size=28)
            elif x_val == PI:
                label = MathTex(r"\pi", font_size=28)
            else:
                label = MathTex(r"2\pi", font_size=28)
            label.next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        self.play(Create(axes), Write(x_labels))
        
        # Actual sin(x)
        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-2*PI, 2*PI], stroke_width=6)
        sin_label = MathTex(r"\sin(x)", color=YELLOW, font_size=36)
        sin_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        sin_label.move_to(axes.c2p(PI*1.5, 1.15))
        
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
        
        # Create label box
        label_box = Rectangle(height=0.8, width=2, color=WHITE, stroke_width=2)
        label_box.to_corner(DL, buff=0.5).shift(UP * 0.3)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-min(2*PI, 3), min(2*PI, 3)] if n <= 5 else [-2*PI, 2*PI]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=40)
            taylor_label.move_to(label_box.get_center())
            
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
        note = Text("More terms = Better approximation!", font_size=34, color=GREEN, weight=BOLD)
        note.to_corner(DR, buff=0.5)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class CosineExample(Scene):
    """Detailed example: cos(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: cos(x)", font_size=56, weight=BOLD, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Formula section
        cosine_formula = MathTex(
            r"\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n}",
            font_size=42
        )
        cosine_formula.next_to(title, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - \cdots",
            font_size=38
        )
        expanded.next_to(cosine_formula, DOWN, buff=0.3)
        
        property_text = Text("Only even powers! Starts at 1!", font_size=30, color=GREEN)
        property_text.next_to(expanded, DOWN, buff=0.25)
        
        self.play(Write(cosine_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(property_text))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-2*PI, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=11,
            y_length=3.5,
            axis_config={"color": BLUE},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        # Custom x-axis labels
        x_labels = VGroup()
        for x_val in [-2*PI, -PI, 0, PI, 2*PI]:
            if x_val == -2*PI:
                label = MathTex(r"-2\pi", font_size=28)
            elif x_val == -PI:
                label = MathTex(r"-\pi", font_size=28)
            elif x_val == 0:
                label = MathTex(r"0", font_size=28)
            elif x_val == PI:
                label = MathTex(r"\pi", font_size=28)
            else:
                label = MathTex(r"2\pi", font_size=28)
            label.next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
            x_labels.add(label)
        
        self.play(Create(axes), Write(x_labels))
        
        # Actual cos(x)
        cos_graph = axes.plot(lambda x: np.cos(x), color=BLUE, x_range=[-2*PI, 2*PI], stroke_width=6)
        cos_label = MathTex(r"\cos(x)", color=BLUE, font_size=36)
        cos_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        cos_label.move_to(axes.c2p(0, 1.2))
        
        self.play(Create(cos_graph), Write(cos_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (0, lambda x: np.ones_like(x) if hasattr(x, '__iter__') else 1, r"P_0", RED),
            (2, lambda x: 1 - x**2/2, r"P_2", GREEN),
            (4, lambda x: 1 - x**2/2 + x**4/24, r"P_4", ORANGE),
            (6, lambda x: 1 - x**2/2 + x**4/24 - x**6/720, r"P_6", PURPLE),
            (8, lambda x: 1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320, r"P_8", YELLOW)
        ]
        
        # Label box
        label_box = Rectangle(height=0.8, width=2, color=WHITE, stroke_width=2)
        label_box.to_corner(DL, buff=0.5).shift(UP * 0.3)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-min(2*PI, 3), min(2*PI, 3)] if n <= 4 else [-2*PI, 2*PI]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=40)
            taylor_label.move_to(label_box.get_center())
            
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
        note = Text("Notice: Only even powers of x!", font_size=34, color=GREEN, weight=BOLD)
        note.to_corner(DR, buff=0.5)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class LnExample(Scene):
    """Detailed example: ln(1+x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: ln(1+x)", font_size=56, weight=BOLD, color=ORANGE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Formula section
        ln_formula = MathTex(
            r"\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} x^{n}",
            font_size=42
        )
        ln_formula.next_to(title, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \frac{x^5}{5} - \cdots",
            font_size=38
        )
        expanded.next_to(ln_formula, DOWN, buff=0.3)
        
        # Important notes
        note1 = Text("Converges for -1 < x ≤ 1", font_size=28, color=RED)
        note1.next_to(expanded, DOWN, buff=0.25)
        note2 = Text("Denominators are just integers!", font_size=28, color=GREEN)
        note2.next_to(note1, DOWN, buff=0.2)
        
        self.play(Write(ln_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(note1), FadeIn(note2))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-1, 1.5, 0.5],
            y_range=[-2, 1, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        self.play(Create(axes))
        
        # Actual ln(1+x)
        ln_graph = axes.plot(
            lambda x: np.log(1 + x),
            color=ORANGE,
            x_range=[-0.99, 1.5],
            stroke_width=6,
            use_smoothing=True
        )
        ln_label = MathTex(r"\ln(1+x)", color=ORANGE, font_size=36)
        ln_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        ln_label.move_to(axes.c2p(1.2, 0.7))
        
        self.play(Create(ln_graph), Write(ln_label))
        self.wait()
        
        # Convergence point
        convergence_line = DashedLine(
            axes.c2p(1, -2),
            axes.c2p(1, 1),
            color=RED,
            dash_length=0.1,
            stroke_width=3
        )
        conv_label = Text("x = 1\n(edge of\nconvergence)", font_size=22, color=RED, line_spacing=0.8)
        conv_label.next_to(axes.c2p(1, -2), DOWN, buff=0.15)
        
        self.play(Create(convergence_line), Write(conv_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (1, lambda x: x, r"P_1", RED),
            (2, lambda x: x - x**2/2, r"P_2", GREEN),
            (3, lambda x: x - x**2/2 + x**3/3, r"P_3", BLUE),
            (5, lambda x: sum([(-1)**(n+1) * x**n / n for n in range(1, 6)]), r"P_5", PURPLE),
            (10, lambda x: sum([(-1)**(n+1) * x**n / n for n in range(1, 11)]), r"P_{10}", YELLOW)
        ]
        
        # Label box
        label_box = Rectangle(height=0.8, width=2.2, color=WHITE, stroke_width=2)
        label_box.to_corner(UL, buff=0.5).shift(DOWN * 2)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-0.95, 0.95] if n <= 5 else [-0.99, 0.99]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=38)
            taylor_label.move_to(label_box.get_center())
            
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
            font_size=32,
            color=GREEN,
            line_spacing=1.1,
            weight=BOLD
        )
        observation.to_corner(DR, buff=0.5)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ExponentialExample(Scene):
    """Example: e^x Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: e^x", font_size=56, weight=BOLD, color=RED)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Formula section
        exp_formula = MathTex(
            r"e^{x} = \sum_{n=0}^{\infty} \frac{x^n}{n!}",
            font_size=42
        )
        exp_formula.next_to(title, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots",
            font_size=38
        )
        expanded.next_to(exp_formula, DOWN, buff=0.3)
        
        # Special properties
        prop1 = Text("All derivatives equal e^x!", font_size=28, color=GREEN)
        prop1.next_to(expanded, DOWN, buff=0.25)
        prop2 = Text("Converges everywhere! (fastest convergence)", font_size=28, color=YELLOW)
        prop2.next_to(prop1, DOWN, buff=0.2)
        
        self.play(Write(exp_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(prop1), FadeIn(prop2))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-2, 3, 1],
            y_range=[-1, 8, 2],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        self.play(Create(axes))
        
        # Actual e^x
        exp_graph = axes.plot(lambda x: np.exp(x), color=RED, x_range=[-2, 2.3], stroke_width=6)
        exp_label = MathTex(r"e^{x}", color=RED, font_size=36)
        exp_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        exp_label.move_to(axes.c2p(1.8, 7))
        
        self.play(Create(exp_graph), Write(exp_label))
        self.wait()
        
        # Progressive approximations
        import math
        
        def taylor_exp(x, n):
            return sum([x**k / math.factorial(k) for k in range(n+1)])
        
        terms = [
            (0, lambda x: np.ones_like(x) if hasattr(x, '__iter__') else 1, r"P_0", ORANGE),
            (1, lambda x: 1 + x, r"P_1", GREEN),
            (2, lambda x: taylor_exp(x, 2), r"P_2", BLUE),
            (4, lambda x: taylor_exp(x, 4), r"P_4", PURPLE),
            (6, lambda x: taylor_exp(x, 6), r"P_6", YELLOW)
        ]
        
        # Label box
        label_box = Rectangle(height=0.8, width=2, color=WHITE, stroke_width=2)
        label_box.to_corner(DL, buff=0.5).shift(UP * 0.3)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-2, min(2.3, 2)]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=40)
            taylor_label.move_to(label_box.get_center())
            
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
        note = Text("Fastest converging series!", font_size=34, color=GREEN, weight=BOLD)
        note.to_corner(DR, buff=0.5)
        self.play(Write(note))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class ArctanExample(Scene):
    """Detailed example: arctan(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: arctan(x)", font_size=56, weight=BOLD, color=PURPLE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Formula section
        arctan_formula = MathTex(
            r"\arctan(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} x^{2n+1}",
            font_size=42
        )
        arctan_formula.next_to(title, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \frac{x^9}{9} - \cdots",
            font_size=38
        )
        expanded.next_to(arctan_formula, DOWN, buff=0.3)
        
        # Important notes
        note = Text("Converges for -1 ≤ x ≤ 1", font_size=28, color=GREEN)
        note.next_to(expanded, DOWN, buff=0.25)
        fun_fact = Text("Used to calculate π! (Leibniz formula: π/4 = arctan(1))", font_size=26, color=YELLOW)
        fun_fact.next_to(note, DOWN, buff=0.2)
        
        self.play(Write(arctan_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(note), FadeIn(fun_fact))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        self.play(Create(axes))
        
        # Actual arctan(x)
        arctan_graph = axes.plot(
            lambda x: np.arctan(x),
            color=PURPLE,
            x_range=[-1.5, 1.5],
            stroke_width=6
        )
        arctan_label = MathTex(r"\arctan(x)", color=PURPLE, font_size=36)
        arctan_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        arctan_label.move_to(axes.c2p(1.2, 0.8))
        
        self.play(Create(arctan_graph), Write(arctan_label))
        self.wait()
        
        # Progressive approximations
        terms = [
            (1, lambda x: x, r"P_1", RED),
            (3, lambda x: x - x**3/3, r"P_3", GREEN),
            (5, lambda x: x - x**3/3 + x**5/5, r"P_5", BLUE),
            (7, lambda x: x - x**3/3 + x**5/5 - x**7/7, r"P_7", ORANGE),
            (9, lambda x: x - x**3/3 + x**5/5 - x**7/7 + x**9/9, r"P_9", YELLOW)
        ]
        
        # Label box
        label_box = Rectangle(height=0.8, width=2, color=WHITE, stroke_width=2)
        label_box.to_corner(DL, buff=0.5).shift(UP * 0.3)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-1.5, 1.5]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=40)
            taylor_label.move_to(label_box.get_center())
            
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
            font_size=34,
            color=GREEN,
            weight=BOLD
        )
        observation.to_corner(DR, buff=0.5)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class GeometricSeriesExample(Scene):
    """Detailed example: 1/(1-x) geometric series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: 1/(1-x)", font_size=56, weight=BOLD, color=GREEN)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Subtitle
        subtitle = Text("(The Geometric Series)", font_size=38, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))
        self.wait()
        
        # Formula section
        geo_formula = MathTex(
            r"\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n",
            font_size=42
        )
        geo_formula.next_to(subtitle, DOWN, buff=0.4)
        
        expanded = MathTex(
            r"= 1 + x + x^2 + x^3 + x^4 + x^5 + \cdots",
            font_size=38
        )
        expanded.next_to(geo_formula, DOWN, buff=0.3)
        
        # Important note
        note = Text("Converges ONLY for |x| < 1", font_size=30, color=RED, weight=BOLD)
        note.next_to(expanded, DOWN, buff=0.3)
        
        self.play(Write(geo_formula))
        self.wait()
        self.play(Write(expanded))
        self.wait()
        self.play(FadeIn(note))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-0.5, 2, 0.5],
            y_range=[-2, 10, 2],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE, "include_numbers": True},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        self.play(Create(axes))
        
        # Actual 1/(1-x)
        geo_graph = axes.plot(
            lambda x: 1/(1-x),
            color=GREEN,
            x_range=[-0.5, 0.95],
            stroke_width=6,
            use_smoothing=False
        )
        geo_label = MathTex(r"\frac{1}{1-x}", color=GREEN, font_size=36)
        geo_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        geo_label.move_to(axes.c2p(0.7, 3.5))
        
        self.play(Create(geo_graph), Write(geo_label))
        self.wait()
        
        # Vertical line at x=1 (divergence)
        div_line = DashedLine(
            axes.c2p(1, -2),
            axes.c2p(1, 10),
            color=RED,
            dash_length=0.1,
            stroke_width=4
        )
        div_label = Text("x = 1\n(diverges!)", font_size=26, color=RED, line_spacing=0.8, weight=BOLD)
        div_label.next_to(axes.c2p(1, -2), DOWN, buff=0.25)
        
        self.play(Create(div_line), Write(div_label))
        self.wait()
        
        # Progressive approximations
        def partial_sum(x, n):
            return sum([x**k for k in range(n+1)])
        
        terms = [
            (0, lambda x: np.ones_like(x) if hasattr(x, '__iter__') else 1, r"P_0", RED),
            (1, lambda x: 1 + x, r"P_1", ORANGE),
            (2, lambda x: partial_sum(x, 2), r"P_2", BLUE),
            (4, lambda x: partial_sum(x, 4), r"P_4", PURPLE),
            (8, lambda x: partial_sum(x, 8), r"P_8", YELLOW)
        ]
        
        # Label box
        label_box = Rectangle(height=0.8, width=2, color=WHITE, stroke_width=2)
        label_box.to_corner(UL, buff=0.5).shift(DOWN * 1.5)
        self.play(Create(label_box))
        
        prev_graph = None
        prev_label = None
        
        for n, func, label_text, color in terms:
            x_range = [-0.5, 0.9]
            
            taylor_graph = axes.plot(func, color=color, x_range=x_range, stroke_width=5)
            taylor_label = MathTex(f"{label_text}(x)", color=color, font_size=40)
            taylor_label.move_to(label_box.get_center())
            
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
            font_size=30,
            color=YELLOW,
            line_spacing=1.2,
            weight=BOLD
        )
        observation.to_corner(DR, buff=0.5)
        self.play(Write(observation))
        self.wait(3)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class HyperbolicExample(Scene):
    """Example: sinh(x) and cosh(x) Taylor series"""
    def construct(self):
        # Title
        title = Text("Taylor Series: Hyperbolic Functions", font_size=52, weight=BOLD)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait()
        
        # Two columns for sinh and cosh
        sinh_title = Text("sinh(x)", font_size=42, color=RED, weight=BOLD)
        sinh_title.move_to(LEFT * 3.5 + UP * 2.5)
        
        cosh_title = Text("cosh(x)", font_size=42, color=BLUE, weight=BOLD)
        cosh_title.move_to(RIGHT * 3.5 + UP * 2.5)
        
        self.play(Write(sinh_title), Write(cosh_title))
        self.wait()
        
        # Formulas
        sinh_formula = MathTex(
            r"\sinh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}",
            font_size=34,
            color=RED
        )
        sinh_formula.next_to(sinh_title, DOWN, buff=0.3)
        
        cosh_formula = MathTex(
            r"\cosh(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}",
            font_size=34,
            color=BLUE
        )
        cosh_formula.next_to(cosh_title, DOWN, buff=0.3)
        
        self.play(Write(sinh_formula), Write(cosh_formula))
        self.wait()
        
        # Expanded forms
        sinh_expanded = MathTex(
            r"x + \frac{x^3}{3!} + \frac{x^5}{5!} + \cdots",
            font_size=32,
            color=RED
        )
        sinh_expanded.next_to(sinh_formula, DOWN, buff=0.3)
        
        cosh_expanded = MathTex(
            r"1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots",
            font_size=32,
            color=BLUE
        )
        cosh_expanded.next_to(cosh_formula, DOWN, buff=0.3)
        
        self.play(Write(sinh_expanded), Write(cosh_expanded))
        self.wait(2)
        
        # Key insight
        insight = Text(
            "Like sin/cos but with positive signs!",
            font_size=32,
            color=YELLOW,
            weight=BOLD
        )
        insight.next_to(sinh_expanded, DOWN, buff=0.5).shift(RIGHT * 1.5)
        self.play(Write(insight))
        self.wait(2)
        
        # Axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 2],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY, "include_numbers": True},
            tips=False
        )
        axes.move_to(DOWN * 2)
        
        self.play(Create(axes))
        
        # Actual functions
        sinh_graph = axes.plot(lambda x: np.sinh(x), color=RED, x_range=[-2.5, 2.5], stroke_width=6)
        cosh_graph = axes.plot(lambda x: np.cosh(x), color=BLUE, x_range=[-2.5, 2.5], stroke_width=6)
        
        sinh_label = MathTex(r"\sinh(x)", color=RED, font_size=32)
        sinh_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
        sinh_label.move_to(axes.c2p(2, 3.5))
        
        cosh_label = MathTex(r"\cosh(x)", color=BLUE, font_size=32)
        cosh_label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.1)
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
        
        # Label box
        label_box = Rectangle(height=0.8, width=1.5, color=WHITE, stroke_width=2)
        label_box.to_corner(DL, buff=0.5)
        self.play(Create(label_box))
        
        for n, color in terms:
            sinh_taylor = axes.plot(
                lambda x: sinh_approx(x, n),
                color=color,
                x_range=[-2.5, 2.5],
                stroke_width=4
            )
            cosh_taylor = axes.plot(
                lambda x: cosh_approx(x, n),
                color=color,
                x_range=[-2.5, 2.5],
                stroke_width=4
            )
            
            term_label = MathTex(f"n={n}", color=color, font_size=36)
            term_label.move_to(label_box.get_center())
            
            self.play(
                Create(sinh_taylor),
                Create(cosh_taylor),
                Write(term_label)
            )
            self.wait(2)
            
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
        title = Text("Taylor Series: Key Takeaways", font_size=56, weight=BOLD, color=YELLOW)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait()
        
        # Key points
        points = VGroup(
            Text("1. Approximates functions using polynomials", font_size=36),
            Text("2. More terms → Better approximation", font_size=36),
            Text("3. Converges within radius of convergence", font_size=36),
            Text("4. Different functions converge at different rates", font_size=36),
        )
        points.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        points.move_to(UP * 0.3)
        
        for point in points:
            self.play(Write(point))
            self.wait(1.5)
        
        self.wait()
        
        # Examples summary
        examples_title = Text("Examples Covered:", font_size=42, weight=BOLD, color=GREEN)
        examples_title.next_to(points, DOWN, buff=0.8)
        self.play(Write(examples_title))
        
        examples = VGroup(
            MathTex(r"\sin(x), \cos(x), e^x", font_size=34),
            MathTex(r"\ln(1+x), \arctan(x)", font_size=34),
            MathTex(r"\frac{1}{1-x}, \sinh(x), \cosh(x)", font_size=34),
        )
        examples.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        examples.next_to(examples_title, DOWN, buff=0.5)
        
        for example in examples:
            self.play(Write(example))
            self.wait(1)
        
        self.wait(3)
        
        # Final message
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        final = Text(
            "Taylor Series:\nThe Foundation of Mathematical Analysis",
            font_size=52,
            line_spacing=1.3,
            weight=BOLD,
            color=YELLOW
        )
        self.play(Write(final))
        self.wait(3)
        
        self.play(FadeOut(final))
