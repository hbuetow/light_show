import json

class COLORS():
    
    def __init__(self):
        colors_file = open('colors.json')
        colors_file_contents = colors_file.read()
        colors_file.close()
        self.colors = json.loads(colors_file_contents)

    def color_rgb(self, color, brightness):
        try:
            rgb = self.colors[color]
            rgb_out = []
            for color in rgb:
                rgb_out.append(int(color * brightness / 100))
            return(rgb_out)
        except:
            return ([100,0,0])