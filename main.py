from ws2812_led_strip import WS2812_LED_STRIP
from color_service import COLOR_SERVICE

pio_processor = 1
gpio_pin = 15
led_count = 8
led_strip = WS2812_LED_STRIP(
    pio_processor,
    gpio_pin,
    led_count)

color_service = COLOR_SERVICE()

def map_colors():
    color_index = 0
    for led_index in range(led_count): 
        led_strip[led_index] = color_service.color_rgb(
            colors[color_index], 
            brightness)
        color_index += 1
        if (color_index >= len(colors)):
            color_index = 0       

colors =[
    "white",
    "red",
    "orange",
    "yellow",
    "green",
    "blue","violet"]
brightness = 100

map_colors()
led_strip.write()
