import random
from PIL import Image
from collections import OrderedDict

# Pixel tuple index
RED = 0
GREEN = 1
BLUE = 2

# Define the codebook
codeBook = OrderedDict()
codeBook[0] = 'Dead Drop @'
codeBook[1] = 'Corner of Lexington Ave and E 48th Street'
codeBook[2] = 'Corner of Madison Ave and E 34th Street'
codeBook[3] = 'Drop Package in Potted Plant outside Wells Fargo'
codeBook[4] = 'Drop Package in Gold Garbage Can'
codeBook[5] = '12 PM Sharp'
codeBook[6] = '7 AM Sharp'
codeBook[7] = 'Abort if you see a Red Rose'

# Display the codebook
print("Codebook:")
for key, value in codeBook.items():
    print(f"{key}: {value}")

# Prompt the user for input
print("Choose 3 items from the codebook to embed:")
messages = []
for i in range(3):
    pixel_to_hide = int(input(f"Enter the codebook index for the {i + 1} message to embed: "))

    if pixel_to_hide not in codeBook:
        print(f"Invalid codebook index. Please choose a valid index.")
    else:
        messages.append(pixel_to_hide)

try:
    img = Image.open('monalisa.bmp')

    new_img = img.copy()  # Create a copy of the original image to save all messages
    usedPixelList = []

    # Define a list of unique pixel coordinates to hide messages
    pixels_to_hide = [(random.randint(0, img.width - 1), random.randint(0, img.height - 1)) for _ in range(3)]

    for message_index, (c, r) in zip(messages, pixels_to_hide):
        hide = [int(b) for b in bin(message_index)[2:].zfill(3)]  # Convert index to binary list

        # Read the Pixel
        pixel = new_img.load()[c, r]

        redPx = pixel[RED]  # Extract the RGB
        grnPx = pixel[GREEN]
        bluPx = pixel[BLUE]

        redPx = (redPx & 0b11111110) | hide[0]
        grnPx = (grnPx & 0b11111110) | hide[1]
        bluPx = (bluPx & 0b11111110) | hide[2]

        # Update the pixel
        pixel = (redPx, grnPx, bluPx)

        # Save the changed Pixel in the pixel proper
        new_img.load()[c, r] = pixel

    # Save this as a new image
    new_img.save('monaLisaTest_combined.bmp')

    print("\nSteganography Done")

except Exception as err:
    print("Steg Failed: ", str(err))
