import comp110_image

def negative(my_pic):
    """ Applies the 'negative' filter to my_pic. """
    for row in range(my_pic.getHeight()):
        for col in range(my_pic.getWidth()):
            pix = my_pic.getPixel(col, row)
            pix.setRed(255 - pix.getRed())
            pix.setGreen(255 - pix.getGreen())
            pix.setBlue(255 - pix.getBlue())


def main():
    image_filename = input("Enter the name of a picture file: ")
    pic = comp110_image.Picture(filename=image_filename)
    pic.setTitle("Original Picture")
    pic.show()

    negative(pic)

    pic.setTitle("Filtered Picture")
    pic.show()

    # saves the modified picture to a new file
    pic.save("filtered.jpg")



""" DO NOT MODIFY ANYTHING BELOW THIS LINE! """
if __name__ == "__main__":
    main()
