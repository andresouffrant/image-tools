from PIL import Image
import numpy
white = (255, 255, 255)

def check_color(mystery, litmus):
    if mystery == litmus:
        return True
    else:
        return False

def main():
    image = Image.open('test_image.jpg')
    width, height = image.size
    pixels = image.load()
    # loop through each row
    for h in range(0, height, 1):
        # loop through each column
        for w in range(0, width, 1):
            print(pixels[w,h])

if __name__ == "__main__":
    main()
