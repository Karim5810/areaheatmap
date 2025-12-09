"""
Heat Map Generator for Customer Locations
Creates an interactive heatmap visualization using folium and generates a static image
"""

import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np
from pathlib import Path

def parse_coordinates(file_path):
    """Parse lat,lng coordinates from file"""
    coordinates = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                parts = line.split(',')
                if len(parts) == 2:
                    lat = float(parts[0].strip())
                    lng = float(parts[1].strip())
                    coordinates.append([lat, lng])
            except ValueError:
                print(f"Skipping invalid line: {line}")
                continue
    
    return coordinates

def create_heatmap(coordinates, output_file='heatmap.html'):
    """Create a modern interactive heatmap using folium"""
    
    # Calculate center of map
    coords_array = np.array(coordinates)
    center_lat = coords_array[:, 0].mean()
    center_lng = coords_array[:, 1].mean()
    
    # Create base map with modern tile
    m = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=13,
        tiles='CartoDB positron',
        prefer_canvas=True
    )
    
    # Add modern heatmap layer with gradient
    HeatMap(
        coordinates,
        name='Heat Density',
        radius=20,
        blur=30,
        max_zoom=1,
        min_opacity=0.3,
        gradient={0.0: '#0000FF', 0.33: '#FFFF00', 0.66: '#FF8800', 1.0: '#FF0000'}
    ).add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Add title with custom CSS
    title_html = '''
    <div style="position: fixed; 
                top: 10px; left: 50px; width: 350px; height: auto;
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size: 14px; padding: 15px; border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h3 style="margin: 0 0 10px 0; color: #333;">Customer Location Heatmap</h3>
        <p style="margin: 5px 0; color: #666;"><b>Total Locations:</b> {}</p>
        <p style="margin: 5px 0; color: #666;"><b>Center:</b> {:.4f}°, {:.4f}°</p>
        <p style="margin: 5px 0; font-size: 12px; color: #999;">Red = High Density | Blue = Low Density</p>
    </div>
    '''.format(len(coordinates), center_lat, center_lng)
    
    m.get_root().html.add_child(folium.Element(title_html))
    
    # Save map
    m.save(output_file)
    print(f"✓ Modern heatmap saved to: {output_file}")
    
    return m

def create_statistics(coordinates):
    """Generate statistics about the coordinates"""
    coords_array = np.array(coordinates)
    
    stats = {
        'total_locations': len(coordinates),
        'center_lat': coords_array[:, 0].mean(),
        'center_lng': coords_array[:, 1].mean(),
        'lat_min': coords_array[:, 0].min(),
        'lat_max': coords_array[:, 0].max(),
        'lng_min': coords_array[:, 1].min(),
        'lng_max': coords_array[:, 1].max(),
        'lat_std': coords_array[:, 0].std(),
        'lng_std': coords_array[:, 1].std(),
    }
    
    return stats

def print_statistics(stats):
    """Print statistics to console"""
    print("\n" + "="*50)
    print("LOCATION STATISTICS")
    print("="*50)
    print(f"Total locations: {stats['total_locations']}")
    print(f"\nCenter point: {stats['center_lat']:.6f}, {stats['center_lng']:.6f}")
    print(f"\nLatitude range:  {stats['lat_min']:.6f} to {stats['lat_max']:.6f}")
    print(f"Longitude range: {stats['lng_min']:.6f} to {stats['lng_max']:.6f}")
    print(f"\nLatitude std dev:  {stats['lat_std']:.6f}")
    print(f"Longitude std dev: {stats['lng_std']:.6f}")
    print("="*50 + "\n")

def main():
    # File paths
    script_dir = Path(__file__).parent
    coord_file = script_dir / 'coordinates.txt'
    output_html = script_dir / 'heatmap.html'
    
    print("Parsing coordinates...")
    coordinates = parse_coordinates(coord_file)
    
    if not coordinates:
        print("No valid coordinates found!")
        return
    
    print(f"Found {len(coordinates)} locations\n")
    
    # Generate statistics
    stats = create_statistics(coordinates)
    print_statistics(stats)
    
    # Create heatmap
    print("Generating heatmap...")
    create_heatmap(coordinates, output_html)
    
    print(f"\n✓ Heatmap created successfully!")
    print(f"✓ Open '{output_html.name}' in your browser to view the interactive map")

if __name__ == '__main__':
    main()
