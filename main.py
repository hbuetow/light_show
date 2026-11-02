from ws2812_led_strip import WS2812_LED_STRIP
from color_service import COLORS

colors = COLORS()

pio_processor = 1
gpio_pin = 15
led_count = 8
brightness = 100

led_strip = WS2812_LED_STRIP(pio_processor, gpio_pin, led_count)

led_strip[0] = colors.color_rgb("white", 100)
led_strip[1] = colors.color_rgb("red", 100)
led_strip[2] = colors.color_rgb("orange", 100)
led_strip[3] = colors.color_rgb("yellow", 100)
led_strip[4] = colors.color_rgb("green", 100)
led_strip[5] = colors.color_rgb("blue", 100)
led_strip[6] = colors.color_rgb("violet", 100)
led_strip[7] = colors.color_rgb("white", 100)

led_strip.write()
