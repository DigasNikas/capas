from colorthief import ColorThief
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    CSS21_HEX_TO_NAMES,
    hex_to_rgb,
)

class RGBTranslate:

    css3_names = []
    css21_names = []


    def __init__(self):
        # a dictionary of all the hex and their respective names in css3
        rgb_values = []
        for color_hex, color_name in CSS3_HEX_TO_NAMES.items():
            self.css3_names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))
        
        self.kdt_db_css3 = KDTree(rgb_values)

        # a dictionary of all the hex and their respective names in css21
        rgb_values = []
        for color_hex, color_name in CSS21_HEX_TO_NAMES.items():
            self.css21_names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))
        
        self.kdt_db_css21 = KDTree(rgb_values)


    def convert_rgb_to_names_css3(self, rgb_tuple):
        _, index = self.kdt_db_css3.query(rgb_tuple)
        return f'{self.css3_names[index]}'

    def convert_rgb_to_names_css21(self, rgb_tuple):

        _, index = self.kdt_db_css21.query(rgb_tuple)
        return f'{self.css21_names[index]}'

    def get_palette(self, image_path):
        color_thief = ColorThief(image_path)
        return color_thief.get_palette(color_count=10, quality=1)

    def get_colors(self, image_path):
        colors = self.get_palette(image_path)

        colors_list_css3 = []
        colors_list_css21 = []
        for color in colors:
            colors_list_css3.append(self.convert_rgb_to_names_css3(color))
            colors_list_css21.append(self.convert_rgb_to_names_css21(color))
        
        return colors_list_css3, colors_list_css21
