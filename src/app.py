from binary_image import read_image, display_image

if __name__ == "__main__":
    image_path = '../images/coca_cola/coca_cola_truck.jpg'
    image = read_image(image_path)
    display_image(image=image, name="Test coca cola")