from binary_image import read_image, display_image, detect_edges, prepare_output_matrix, save_output_matrix, resize_image

if __name__ == "__main__":
    image_path = '../images/coca_cola/coca_cola_bottle.jpg'
    image = read_image(image_path)
    image = resize_image(400, 300, image)
    edges = detect_edges(image)
    template = prepare_output_matrix(edges)
    save_output_matrix(template_matrix=template, file_name='coca_cola_bottle_matrix.txt')
    print(template.shape)

    # display_image(image=image, name="Test coca cola")
    display_image(image=template, name="Test coca cola Edges")
