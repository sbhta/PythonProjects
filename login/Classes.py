import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]  # ["⣿", "⣷", "⣧", "⣦", "⣤", "⣄", "⣀", "."]


def resize_image(image, new_width=100):
    width, height = image.size
    height += 300
    ratio = width / height
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixel_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return (characters)


def PTA(sender, PATH):
    path = PATH
    path = path[0] + "/" + path[1]
    #print(path)
    new_width = 100
    try:
        image = PIL.Image.open(path)
        new_image_data = pixel_to_ascii(grayify(resize_image(image)))
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

    except:
        print(path, "isn't valid")
    return ascii_image

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
