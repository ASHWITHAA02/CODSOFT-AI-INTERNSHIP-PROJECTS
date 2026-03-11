from PIL import Image

def load_image(path):
    try:
        image = Image.open(path)
        return image
    except:
        print("Error loading image")
        return None