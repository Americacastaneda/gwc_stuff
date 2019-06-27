# from PIL import Image

# img = Image.open("image5.jpg")
# img.show()
# print(img.size)
import filters

def main():
   img = filters.load_img("image5.jpg")
   filters.obamicon(img)


if __name__ == "__main__"
    main()