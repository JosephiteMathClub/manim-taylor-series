# Taylor Series Animation with Manim

A comprehensive and educational visualization of Taylor series using the Manim library.

## Files

- **taylor_series_hq.py** - High quality version with optimized layout and spacing (RECOMMENDED)
- **taylor_series_animation.py** - Original version

## Overview

This animation explains and visualizes how Taylor series work, showing how polynomial approximations can represent complex mathematical functions. The presentation includes:

1. **Introduction** - Formula and concept explanation with opening statement
2. **Visual Building** - Step-by-step construction of approximations
3. **sin(x) Example** - Taylor series expansion with progressive terms
4. **cos(x) Example** - Even powers demonstration
5. **ln(1+x) Example** - Convergence radius visualization
6. **e^x Example** - Fastest converging series
7. **arctan(x) Example** - Used in calculating π
8. **1/(1-x) Example** - Geometric series with limited convergence
9. **sinh(x) & cosh(x) Example** - Hyperbolic functions
10. **Conclusion** - Key takeaways and summary

## Key Improvements in HQ Version

✨ **Better Layout** - Graphs positioned to avoid overlapping with formulas
✨ **Enhanced Visuals** - Thicker lines, better colors, background rectangles for labels
✨ **Clearer Text** - Larger fonts, bold weights, color-coded examples
✨ **Info Boxes** - Dedicated areas for current approximation labels
✨ **High Quality** - Optimized for 1920x1080 resolution

## Prerequisites

Make sure you have Python and Manim installed:

```bash
pip install manim
```

For better quality rendering, you may also want to install:
```bash
pip install numpy
```

## How to Run

### Render High Quality Scenes (RECOMMENDED)

Use the improved high-quality version for best results:

```bash
# Introduction with opening statement
manim -pqh taylor_series_hq.py TaylorSeriesIntro

# Visual demonstration
manim -pqh taylor_series_hq.py TaylorSeriesVisualization

# sin(x) example
manim -pqh taylor_series_hq.py SineExample

# cos(x) example
manim -pqh taylor_series_hq.py CosineExample

# ln(1+x) example
manim -pqh taylor_series_hq.py LnExample

# e^x example
manim -pqh taylor_series_hq.py ExponentialExample

# arctan(x) example
manim -pqh taylor_series_hq.py ArctanExample

# Geometric series 1/(1-x)
manim -pqh taylor_series_hq.py GeometricSeriesExample

# Hyperbolic functions
manim -pqh taylor_series_hq.py HyperbolicExample

# Conclusion
manim -pqh taylor_series_hq.py TaylorSeriesConclusion

# Or render ALL scenes at once:
manim -pqh -a taylor_series_hq.py
```

### Quality Options

- `-ql` or `--quality l` - Low quality (fastest, 480p)
- `-qm` or `--quality m` - Medium quality (720p)
- `-qh` or `--quality h` - High quality (1080p)
- `-qk` or `--quality k` - 4K quality (2160p)

### Additional Flags

- `-p` - Preview after rendering
- `-s` - Show last frame only
- `-a` - Render all scenes in the file

### High Quality Full Presentation

To render the entire presentation in high quality:

```bash
manim -pqh -a taylor_series_hq.py
```

For lower quality/faster preview:
```bash
manim -pql -a taylor_series_hq.py
```

## Scene Descriptions

### 1. TaylorSeriesIntro
Opens with a thought-provoking question, then introduces the Taylor series formula with visual emphasis and key properties.

### 2. TaylorSeriesVisualization
Builds a Taylor approximation step-by-step for sin(x), showing how adding more terms improves accuracy. Uses an info box to clearly display the current approximation.

### 3. SineExample
Detailed visualization of sin(x) Taylor series:
- Shows the infinite series formula and expanded form
- Highlights that only odd powers appear
- Displays approximations from P₁ to P₉
- Demonstrates convergence over multiple periods

### 4. CosineExample
Explores cos(x) Taylor series:
- Highlights even powers only
- Shows it starts at 1
- Smooth convergence from P₀ to P₈

### 5. LnExample
Demonstrates ln(1+x) Taylor series:
- Shows convergence radius (-1 < x ≤ 1)
- Vertical line marking convergence boundary
- Illustrates slower convergence near x = 1
- Progressive approximations up to P₁₀

### 6. ExponentialExample
Visualizes e^x Taylor series:
- Fastest converging series
- Converges everywhere
- All derivatives equal e^x
- Shows approximations from P₀ to P₆

### 7. ArctanExample
Demonstrates arctan(x) Taylor series:
- Only odd powers (similar to sin)
- Connection to calculating π via Leibniz formula
- Convergence for |x| ≤ 1

### 8. GeometricSeriesExample
The simplest Taylor series 1/(1-x):
- Classic geometric series: 1 + x + x² + x³ + ...
- Shows strict convergence at |x| < 1
- Vertical line showing divergence at x = 1

### 9. HyperbolicExample
Side-by-side comparison of sinh(x) and cosh(x):
- Like sin/cos but with positive signs
- Both functions visualized together
- Shows approximations for both simultaneously

### 10. TaylorSeriesConclusion
Summarizes key concepts and lists all 8 examples covered.

## Educational Features

- **Improved Layout** - No overlapping text and graphs
- **Color-coded approximations** - Each polynomial order has a distinct color
- **Progressive building** - Shows how adding terms improves approximation
- **Mathematical formulas** - LaTeX-rendered equations with proper positioning
- **Visual comparisons** - Side-by-side original function and approximation
- **Convergence insights** - Demonstrates where and how series converge
- **Info boxes** - Dedicated areas for current approximation labels
- **Background rectangles** - Labels stand out clearly against graphs
- **Bold and clear text** - Easy to read titles and explanations
- **High resolution** - Optimized for 1920x1080 rendering

## Customization

You can modify the animations by editing the Python file:
- Change colors in the `colors` lists
- Adjust animation speeds with `wait()` durations
- Modify axis ranges for different viewing windows
- Add more polynomial terms to approximations
- Change font sizes and positions

## Output

Videos are saved in the `media/videos/taylor_series_animation/` directory, organized by quality setting.

## Tips

1. Start with low quality (`-ql`) for quick previews
2. Use high quality (`-qh`) for final presentations
3. Render individual scenes when working on specific sections
4. The complete presentation runs for approximately 5-7 minutes

## Mathematical Background

Taylor series expansion around point a:
```
f(x) = Σ(n=0 to ∞) [f⁽ⁿ⁾(a) / n!] × (x-a)ⁿ
```

For Maclaurin series (a=0):
```
f(x) = f(0) + f'(0)x + f''(0)x²/2! + f'''(0)x³/3! + ...
```

## License

Feel free to use and modify this educational content for learning purposes.
