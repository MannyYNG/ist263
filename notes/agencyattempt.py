import PIL
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Load the user's uploaded image
image_path = "image_e52959.png"
base_img = Image.open(image_path)

# Instagram Standard Size (Square 1080x1080)
target_size = (1080, 1080)

# Function to crop and resize image to fill square
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

# Calculate aspect ratio to fill 1080 height
aspect_ratio = base_img.width / base_img.height
new_height = 1080
new_width = int(new_height * aspect_ratio)
resized_img = base_img.resize((new_width, new_height))

# Center crop to 1080x1080
final_bg = crop_center(resized_img, 1080, 1080)

# Load Fonts (Using default system fonts for demonstration, aiming for bold sans-serif)
# In a real environment we would load a specific brand font.
try:
    # Try to load a standard bold font
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
    body_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
except:
    # Fallback default
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    body_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# --- SLIDE 1: The Hook ---
slide1 = final_bg.copy()
draw1 = ImageDraw.Draw(slide1)

# Add a slight dark gradient at the bottom for text readability
overlay1 = Image.new('RGBA', target_size, (0,0,0,0))
draw_overlay1 = ImageDraw.Draw(overlay1)
draw_overlay1.rectangle([(0, 700), (1080, 1080)], fill=(0,0,0,180))
slide1 = Image.alpha_composite(slide1.convert('RGBA'), overlay1)
draw1 = ImageDraw.Draw(slide1)

# Text Slide 1
draw1.text((540, 780), "EAST MEETS", font=title_font, fill="white", anchor="ms")
draw1.text((540, 880), "WESTCOTT", font=title_font, fill="#90EE90", anchor="ms") # Light green for 'Westcott/Wasabi' vibe
draw1.text((540, 960), "The Blue Tusk Slice", font=subtitle_font, fill="white", anchor="ms")

# --- SLIDE 2: The Ingredients ---
slide2 = final_bg.copy()
# Darken image more heavily to make text lists readable
enhancer = ImageEnhance.Brightness(slide2)
slide2 = enhancer.enhance(0.4) 
draw2 = ImageDraw.Draw(slide2)

# Text Slide 2
draw2.text((100, 150), "BOLD FLAVOR JOURNEY", font=subtitle_font, fill="#90EE90", anchor="ls")

# Ingredients List
y_start = 300
spacing = 120
ingredients = [
    ("THE BASE", "Zesty Wasabi Cream"),
    ("THE BEEF", "Slow-Braised & Tender"),
    ("THE CHEESE", "Melted Havarti & Sharp Cheddar"),
    ("THE CRUNCH", "Pickled Banana Peppers")
]

for label, desc in ingredients:
    draw2.text((100, y_start), label, font=subtitle_font, fill="#FFA500", anchor="ls") # Orange for 'Bold'
    draw2.text((100, y_start + 50), desc, font=body_font, fill="white", anchor="ls")
    y_start += spacing

# --- SLIDE 3: CTA & QR Placeholder ---
slide3 = final_bg.copy()
slide3 = enhancer.enhance(0.3) # Dark background
draw3 = ImageDraw.Draw(slide3)

draw3.text((540, 150), "TRY IT TONIGHT", font=title_font, fill="white", anchor="ms")

# Location Info
draw3.text((540, 300), "FAT BOY PIZZA", font=subtitle_font, fill="#FFA500", anchor="ms")
draw3.text((540, 360), "Inside The Westcott Theatre", font=body_font, fill="white", anchor="ms")

# QR Code Box Placeholder
qr_box_size = 400
qr_x = (1080 - qr_box_size) // 2
qr_y = 450
draw3.rectangle([(qr_x, qr_y), (qr_x + qr_box_size, qr_y + qr_box_size)], fill="white")
draw3.text((540, qr_y + qr_box_size/2), "PLACE QR CODE HERE", font=small_font, fill="black", anchor="ms")

draw3.text((540, 950), "fatboypizza.com", font=body_font, fill="white", anchor="ms")

# Save images
slide1.save("slide1_hook.png")
slide2.save("slide2_ingredients.png")
slide3.save("slide3_cta.png")