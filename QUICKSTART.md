# Quick Start Guide

## 🚀 Fast Setup

### 1. Install Manim
```powershell
pip install manim
```

### 2. Install FFmpeg (if not already installed)
Choose one method:

**Option A: Chocolatey**
```powershell
choco install ffmpeg
```

**Option B: Scoop**
```powershell
scoop install ffmpeg
```

**Option C: Manual**
- Download from: https://www.gyan.dev/ffmpeg/builds/
- Extract to `C:\ffmpeg`
- Add `C:\ffmpeg\bin` to PATH

### 3. Verify FFmpeg
```powershell
ffmpeg -version
```

## 🎬 Render Your First Animation

### Quick Preview (Low Quality - Fast)
```powershell
manim -pql taylor_series_hq.py TaylorSeriesIntro
```

### High Quality
```powershell
manim -pqh taylor_series_hq.py SineExample
```

### All Scenes at Once
```powershell
manim -pqh -a taylor_series_hq.py
```

## 📊 Scene List

1. `TaylorSeriesIntro` - Introduction with opening statement
2. `TaylorSeriesVisualization` - Building approximations
3. `SineExample` - sin(x) series
4. `CosineExample` - cos(x) series
5. `LnExample` - ln(1+x) series
6. `ExponentialExample` - e^x series
7. `ArctanExample` - arctan(x) series
8. `GeometricSeriesExample` - 1/(1-x) series
9. `HyperbolicExample` - sinh(x) & cosh(x)
10. `TaylorSeriesConclusion` - Summary

## 🎨 Quality Options

- `-ql` = Low quality (480p, fast preview)
- `-qm` = Medium quality (720p)
- `-qh` = High quality (1080p) ⭐ **RECOMMENDED**
- `-qk` = 4K quality (2160p)

## 💡 Tips

- Use `-p` flag to automatically preview after rendering
- Use `-s` to show just the last frame
- Start with `-ql` for quick tests, then use `-qh` for final output
- Videos are saved in `media/videos/taylor_series_hq/`

## ⚡ Common Commands

```powershell
# Preview one scene quickly
manim -pql taylor_series_hq.py SineExample

# Render high quality version
manim -pqh taylor_series_hq.py SineExample

# Render all scenes in high quality
manim -pqh -a taylor_series_hq.py

# Just show last frame (no animation)
manim -pqh -s taylor_series_hq.py TaylorSeriesIntro
```

## 🎯 Recommended Workflow

1. **First time**: Render intro to test setup
   ```powershell
   manim -pql taylor_series_hq.py TaylorSeriesIntro
   ```

2. **Preview scenes**: Use low quality to see all scenes
   ```powershell
   manim -pql -a taylor_series_hq.py
   ```

3. **Final render**: High quality for presentation
   ```powershell
   manim -pqh -a taylor_series_hq.py
   ```

## 🐛 Troubleshooting

**Error: "Couldn't find ffmpeg"**
- Install ffmpeg (see step 2 above)
- Restart your terminal after installation

**Videos not playing**
- Check `media/videos/taylor_series_hq/` folder
- Try VLC or another media player

**Slow rendering**
- Use `-ql` for previews
- Only use `-qh` or `-qk` for final output
