class ColorText:
    def text_in_color(txt:str, color_font_name:str=None, color_bg_name:str=None):
        '''
        output the text with a foreground and a background color
        args:
            `txt`(str): text to be printed
            `color_font_name`(str): font color amongst ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
            `color_bg_name`(str): back ground color amongst ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
        '''
        colors = ['black', 'red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'grey']
        dict_color_map_font = {k:v for k,v in zip(colors, range(30,38))}
        dict_color_map_bg = {k:v for k,v in zip(colors, range(40,48))}
        color_font = dict_color_map_font.get(color_font_name, 30)
        color_bg = dict_color_map_bg.get(color_bg_name, 49)

        txt_w_col = f"{txt}"

        if not color_font:
            txt_w_col = f"{txt_w_col}"
        else:
            txt_w_col = f"\x1b[{color_font}m{txt_w_col}"

        if not color_bg:
            txt_w_col = f"{txt_w_col}"
        else:
            txt_w_col = f"\x1b[{color_bg}m{txt_w_col}"

        return txt_w_col

    def text_to_green(txt:str):
        txt_w_col = ColorText.text_in_color(txt, 'green')
        return txt_w_col

    def text_to_red(txt:str):
        txt_w_col = ColorText.text_in_color(txt, 'red')
        return txt_w_col