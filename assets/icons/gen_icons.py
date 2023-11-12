from PIL import Image

def generate_icons(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Generate android-chrome-192x192.png
        img.resize((192, 192)).save("android-chrome-192x192.png", "PNG")

        # Generate android-chrome-512x512.png
        img.resize((512, 512)).save("android-chrome-512x512.png", "PNG")

        # Generate apple-touch-icon.png
        img.resize((180, 180)).save("apple-touch-icon.png", "PNG")

        # Generate favicon-16x16.png
        img.resize((16, 16)).save("favicon-16x16.png", "PNG")

        # Generate favicon-32x32.png
        img.resize((32, 32)).save("favicon-32x32.png", "PNG")

        # Generate favicon.ico
        img.resize((256, 256)).save("favicon.ico", "ICO")

# Use the function
generate_icons("photo.jpg")
