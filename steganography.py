from PIL import Image


def decode_image(path_to_png):
  """
  TODO: Add docstring and complete implementation.
  """
  # Open the image using PIL:
  encoded_image = Image.open(path_to_png)

  # Separate the red channel from the rest of the image:
  red_channel = encoded_image.split()[0]

  # Create a new PIL image with the same size as the encoded image:
  decoded_image = Image.new("RGB", encoded_image.size)
  pixels = decoded_image.load()
  x_size, y_size = encoded_image.size

  # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:
  for x in range(x_size):
    for y in range(y_size):
      if red_channel.getpixel((x, y)) & 1: 
        pixels[x, y] = (0, 0, 0) 
      else: 
        pixels[x, y] = (255, 255, 255)
  # print(red_channel.getpixel((0,0)))  # Start coding here!

  # DO NOT MODIFY. Save the decoded image to disk:
  decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
  """
  TODO: Add docstring and complete implementation.
  """
  pass


decode_image('es.png')