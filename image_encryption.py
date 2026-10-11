from PIL import Image


def process_image(input_file, output_file, key):
    image = Image.open(input_file).convert("RGB")

    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):

            r, g, b = pixels[x, y]

            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[x, y] = (r, g, b)

    image.save(output_file)


print("================================")
print("     IMAGE ENCRYPTION TOOL")
print("================================")

input_file = input("Enter input image: ")
output_file = input("Enter output image: ")
key = int(input("Enter encryption key (0-255): "))

process_image(input_file, output_file, key)

print("\nImage processed successfully.")
print("Output saved as:", output_file)
