from dearpygui.core import *
from dearpygui.simple import *
from functions import *

set_main_window_size(100, 100)
set_style_window_padding(30, 30)
set_theme("Gold")
set_global_font_scale(0.8)


a = []
with window("win", width=1680, height=1050):
    set_window_pos("win", 0, 0)
    def applySelectedDirectory(sender, data):
        add_text(PTA(sender, data), color=[150, 150, 150], parent="win")
        add_drawing("pic", width=1000, height=1000, parent="win")
        a = data
        draw_image("pic", data[0] + "/" + data[1], [0, 240], pmax=[50, 240], uv_min=[0, 0], uv_max=[255, 255], tag="pic")




    def ask_for_file():
        open_file_dialog(callback=applySelectedDirectory, extensions=".jpg,.png")
    #add_text("Input a file")
    add_button("FILE", callback=ask_for_file)




start_dearpygui()
