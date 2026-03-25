import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Generate random text
def generate_text(length=5):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Create CAPTCHA image
def create_captcha(text):
    width, height = 200, 80
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Load default font
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Draw text
    for i, char in enumerate(text):
        x = 20 + i * 30
        y = random.randint(5, 20)
        draw.text((x, y), char, font=font, fill=random_color())

    # Add noise lines
    for _ in range(5):
        draw.line(
            (random.randint(0, width), random.randint(0, height),
             random.randint(0, width), random.randint(0, height)),
            fill=random_color(), width=2
        )

    # Add dots
    for _ in range(100):
        draw.point((random.randint(0, width), random.randint(0, height)),
                   fill=random_color())

    # Apply blur filter
    image = image.filter(ImageFilter.BLUR)

    return image

# Generate random color
def random_color():
    return (random.randint(0, 150),
            random.randint(0, 150),
            random.randint(0, 150))

# Main
if __name__ == "__main__":
    text = generate_text()
    captcha = create_captcha(text)

    print("CAPTCHA Text:", text)
    captcha.show()        # Display image
    captcha.save("captcha.png")  # Save image
