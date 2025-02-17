# Certificate Generator

A Python script to automatically generate personalized certificates from a template image and a CSV file containing names. The script centers each name horizontally on the certificate for professional presentation.

## Features

- Bulk certificate generation from a CSV file
- Automatic text centering
- Progress bar to track generation status
- Error handling for missing files and invalid inputs
- Customizable font size and color
- Maintains high image quality

## Prerequisites

- Python 3.x
- Required Python packages:
  - Pillow (PIL)
  - pandas
  - tqdm

## Required Files

1. `name.csv` - CSV file with a "Names" column containing the list of names
2. `icts-certificate.jpg` - Certificate template image
3. `bahnschrift.ttf` - Font file (or replace with your preferred font)

## Installation

```bash
pip install Pillow pandas tqdm
```

## Usage

1. Place your certificate template as `icts-certificate.jpg` in the script directory
2. Create a CSV file named `name.csv` with a column header "Names"
3. Ensure the font file `bahnschrift.ttf` is in the script directory
4. Run the script:

```bash
python certificate_generator.py
```

Generated certificates will be saved in the `generated_certificates` folder.

## Customization

You can modify the following variables in the script:
- `font_size`: Change the size of the text
- `font_color`: Adjust the color of the text (RGB format)
- `y_position`: Modify the vertical position of the text

## Error Handling

The script includes error checking for:
- Missing CSV file
- Missing template image
- Missing font file
- Invalid CSV format
- Failed certificate generation

## License

[Add your chosen license here]

## Contributing

Feel free to submit issues and enhancement requests!
