# VideoToFrames

This is a simple python script that converts a video file into a series of images. 
The script uses the OpenCV library to read the video file and save each frame as an image. 

The script takes two arguments: 
the path to the video file and the output directory where the images will be saved.

## Usage
Run the script with the following command:

```
python video_to_frames.py
```

## Requirements
- Python 3
- OpenCV
### For HEIC to PNG conversion support:
- **Pillow** _(version 11.2.1)_, execute the following command
```bash
pip install pillow
```
- **pillow-heif** _(version 0.22.0)_, execute the following command
```bash 
pip install pillow-heif
```

## Important Considerations
- Converting HEIC to JPG file format:
> Warning: JPG does not support a color depth of 16 bits per channel. The JPEG standard is designed for 8 bits per channel. If your original HEIC image has 10 or 12 bits of color depth (HDR), converting it to JPG will result in the loss of that color depth information, reducing it to 8 bits.

**You can specify the quality when saving to control the JPEG compression level. A higher quality (quality = 100) will result in a larger file but with fewer compression artifacts.**

```python
heic_file = "file.HEIC" # Reemplaza
output_jpg_file = "file.jpg"
convert_heic_to_jpg(heic_file, output_jpg_file, quality=100)
```