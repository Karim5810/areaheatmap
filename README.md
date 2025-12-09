# 🔥 Customer Location Heatmap

An interactive heatmap visualization of customer locations with 884 data points.

## Features

✨ **Interactive Heatmap**
- Modern, responsive design
- Heat gradient: Blue (min) → Yellow → Orange → Red (max)
- Zoom and pan controls

📥 **Download Data**
- Export as CSV
- Export as JSON with statistics

📤 **Share & Collaborate**
- Shareable link
- Portable HTML file (works offline)

## Local Usage

### Prerequisites
- Python 3.7+
- pip

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Generate heatmap
python generate_heatmap.py
```

### Open the Map
```bash
# Simply open heatmap.html in your browser
start heatmap.html  # Windows
open heatmap.html   # macOS
xdg-open heatmap.html  # Linux
```

## Deployment to Netlify

### Option 1: Direct GitHub Integration (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - heatmap project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/areaheatmap.git
   git push -u origin main
   ```

2. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Select GitHub and authorize
   - Choose your `areaheatmap` repository
   - Netlify will auto-detect `netlify.toml` settings
   - Click "Deploy"

### Option 2: Deploy Folder Directly

1. **Build Locally**
   ```bash
   python generate_heatmap.py
   ```

2. **Deploy to Netlify**
   - Go to [netlify.com/drop](https://app.netlify.com/drop)
   - Drag and drop the entire `areaheatmap` folder
   - Get your live URL instantly

### Option 3: Netlify CLI

1. **Install Netlify CLI**
   ```bash
   npm install -g netlify-cli
   ```

2. **Deploy**
   ```bash
   netlify deploy --prod
   ```

## Files

- `heatmap.html` - The interactive map (generated)
- `coordinates.txt` - Your raw coordinate data
- `generate_heatmap.py` - Python script to generate the heatmap
- `requirements.txt` - Python dependencies
- `netlify.toml` - Netlify configuration

## Customization

Edit `generate_heatmap.py` to:
- Change map radius and blur intensity
- Modify color gradient
- Add custom markers or overlays
- Update center point

## Data Format

Input coordinates in `coordinates.txt`:
```
latitude,longitude
24.5980473,46.7365921
24.6636867,46.7303188
...
```

## Live Demo

Once deployed, your heatmap will be live at:
```
https://your-site-name.netlify.app/
```

## License

MIT License - Feel free to use and modify

---

**Made with ❤️ | Deployed on Netlify**
