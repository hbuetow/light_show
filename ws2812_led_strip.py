import array
import rp2
from rp2 import PIO, StateMachine, asm_pio

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def output_to_led_strip():
    label("start_loop")
    out(x, 1).side(0)[2]              # the pin is low for 3 cycles
    jmp(not_x, "zero_bit").side(1)[1] # the pin is high for 2 cycles
    jmp("start_loop").side(1)[4]      # when outputting a one bit, the pin is high for 5 cycles
    label("zero_bit")
    nop().side(0)[4]                  # when outputting a zero bit, the pin is low for 5 cycles

class WS2812_LED_STRIP():   
    def __init__(self, processor, pin, led_count):
        self.sm = StateMachine(processor, output_to_led_strip, freq=8000000, sideset_base=pin)
        self.sm.active(1)        
        self.buf = array.array("I", [0 for _ in range(led_count)])

    def write(self):
        self.sm.put(self.buf, 8)

    def __setitem__(self, i, value):
        value = (value[0] << 8) + (value[1] << 16) + (value[2])
        self.buf[i] = value
