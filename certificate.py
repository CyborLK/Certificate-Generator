from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from tqdm import tqdm 

# Load CSV
csv_file = "name.csv"
template_path = "icts-certificate.jpg"
output_folder = "generated_certificates"
font_path = "bahnschrift.ttf"  # font for names

# Check if CSV file exists
if not os.path.isfile(csv_file):
    print(f"Error: CSV file '{csv_file}' not found.")
    exit()

# Check if template image file exists
if not os.path.isfile(template_path):
    print(f"Error: Template image file '{template_path}' not found.")
    exit()

# Ensure output folder exists
try:
    os.makedirs(output_folder, exist_ok=True)
except Exception as e:
    print(f"Error creating output folder '{output_folder}': {e}")
    exit()

try:
    df = pd.read_csv(csv_file)  # Ensure CSV contains a column with names
    if "Names" not in df.columns:
        raise KeyError("CSV file does not contain a 'Names' column.")
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit()

# Font settings
font_size = 60
font_color = (0, 0, 0)  # Black
y_position = 682  # Keep the same Y coordinate

# get template dimensions
template = Image.open(template_path)
template_width = template.width

print(f"Generating certificates for {len(df)} names...")

# Progress bar
for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing Certificates"):
    try:
        name = row["Names"].strip()  # Ensure there are no spaces

        # Open certificate template
        img = Image.open(template_path)
        draw = ImageDraw.Draw(img)

        # Load font
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            print("Error: Font file not found. Please ensure 'bahnschrift.ttf' exists.")
            exit()

        # Calculate text width and height
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        
        # Calculate center position
        x_position = (template_width - text_width) // 2

        # Add text (name) to the certificate
        draw.text((x_position, y_position), name, fill=font_color, font=font)

        # Save the certificate
        output_path = os.path.join(output_folder, f"Certificate_{name}.jpg")
        img.save(output_path)

    except Exception as e:
        print(f"Error processing {row['Names']}: {e}")

print(f"✅ Certificates successfully generated in '{output_folder}' folder!")