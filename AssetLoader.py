import os
try:
     import simplegui
except ImportError:
     import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# folder paths
IMAGES_PATH = os.path.abspath(os.path.join("assets", "images"))
SOUNDS_PATH = os.path.abspath(os.path.join("assets", "sounds"))

def load_image(file_name):
    file_path = os.path.join(IMAGES_PATH, file_name)
    img = simplegui._load_local_image(file_path)
    if img.get_width() <= 0:
        print(f"Warning: failed to load {file_name}")
    return img

def load_sound(file_name):
    file_path = os.path.join(SOUNDS_PATH, file_name)
    sound = simplegui._load_local_sound(file_path)
    return sound
