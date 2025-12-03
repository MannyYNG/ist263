import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap

# Load the uploaded image
img_path = 'image_e52959.png'
original_img = Image.open(img_path)

# Define target size for Instagram (Square)
target_size = (1080, 1080)

# Helper function to crop and resize
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

# Resize logic to fill the square
aspect_ratio = original_img.width / original_img.height
new_height = 1080
new_width = int(new_height * aspect_ratio)
resized_img = original_img.resize((new_width, new_height))
base_img = crop_center(resized_img, 1080, 1080)

# Create font objects (using a default sans-serif font available in the environment)
# Since we can't load external fonts, we rely on the default PIL font behavior or basic specific paths
try:
    font_path_bold = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    font_path_reg = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    
    title_font = ImageFont.truetype(font_path_bold, 95)
    subtitle_font = ImageFont.truetype(font_path_bold, 50)
    body_font = ImageFont.truetype(font_path_reg, 40)
    small_font = ImageFont.truetype(font_path_reg, 30)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# --- SLIDE 1: INTRO ---
slide1 = base_img.copy()
draw1 = ImageDraw.Draw(slide1)

# Add dark gradient at bottom
overlay1 = Image.new('RGBA', target_size, (0,0,0,0))
draw_overlay1 = ImageDraw.Draw(overlay1)
draw_overlay1.rectangle([(0, 600), (1080, 1080)], fill=(0,0,0,160)) # Semi-transparent black
slide1 = Image.alpha_composite(slide1.convert('RGBA'), overlay1)
draw1 = ImageDraw.Draw(slide1)

# Text
draw1.text((540, 750), "EAST MEETS", font=title_font, fill="white", anchor="ms")
draw1.text((540, 850), "WESTCOTT", font=title_font, fill="#98FB98", anchor="ms") # Pale green
draw1.text((540, 950), "The Blue Tusk Slice", font=subtitle_font, fill="white", anchor="ms")

# --- SLIDE 2: DETAILS ---
slide2 = base_img.copy()
enhancer = ImageEnhance.Brightness(slide2)
slide2 = enhancer.enhance(0.3) # Darken significantly for text legibility
draw2 = ImageDraw.Draw(slide2)

draw2.text((100, 150), "BOLD FLAVOR JOURNEY", font=subtitle_font, fill="#98FB98", anchor="ls")

# Ingredients
ingredients_y = 300
items = [
    ("THE BASE", "Zesty Wasabi Cream"),
    ("THE MEAT", "Slow-Braised Beef"),
    ("THE CHEESE", "Melted Havarti & Cheddar"),
    ("THE CRUNCH", "Pickled Banana Peppers")
]

for title, desc in items:
    draw2.text((100, ingredients_y), title, font=subtitle_font, fill="#FFA500", anchor="ls") # Orange
    draw2.text((100, ingredients_y + 60), desc, font=body_font, fill="white", anchor="ls")
    ingredients_y += 160

# --- SLIDE 3: CTA ---
slide3 = base_img.copy()
enhancer = ImageEnhance.Brightness(slide3)
slide3 = enhancer.enhance(0.25) # Darker
draw3 = ImageDraw.Draw(slide3)

draw3.text((540, 200), "TRY IT TONIGHT", font=title_font, fill="white", anchor="ms")

draw3.text((540, 350), "FAT BOY PIZZA", font=subtitle_font, fill="#FFA500", anchor="ms")
draw3.text((540, 420), "Inside The Westcott Theatre", font=body_font, fill="white", anchor="ms")

# QR Box
qr_size = 400
qr_x = (1080 - qr_size) // 2
qr_y = 500
draw3.rectangle([(qr_x, qr_y), (qr_x + qr_size, qr_y + qr_size)], fill="white")
draw3.text((540, qr_y + qr_size/2), "PASTE QR HERE", font=small_font, fill="black", anchor="ms")

draw3.text((540, 1000), "fatboypizza.com", font=body_font, fill="white", anchor="ms")

# Display images using Matplotlib
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(slide1)
axes[0].axis('off')
axes[0].set_title("Slide 1")

axes[1].imshow(slide2)
axes[1].axis('off')
axes[1].set_title("Slide 2")

axes[2].imshow(slide3)
axes[2].axis('off')
axes[2].set_title("Slide 3")

plt.tight_layout()
plt.show()
