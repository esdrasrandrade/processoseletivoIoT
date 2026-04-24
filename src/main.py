from machine import Pin, ADC
import time

# ====== CONFIG ======
LED_PINS = [4, 5, 2]  # LEDs (ordem = seleção)
BTN_PIN = 26
JOY_X_PIN = 35

DELAY_JOYSTICK = 300  # ms entre movimentos

# ====== HARDWARE ======
leds = [Pin(p, Pin.OUT) for p in LED_PINS]
button = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)

joy_x = ADC(Pin(JOY_X_PIN))
joy_x.atten(ADC.ATTN_11DB)  # faixa 0-3.3V

# ====== ESTADOS ======
SELECIONANDO = 0
CONFIRMADO = 1

estado = SELECIONANDO
indice = 0

# ====== CONTROLE DE TEMPO ======
ultimo_mov = 0
ultimo_btn = 0

# ====== FUNÇÕES ======
def atualizar_leds():
    for i, led in enumerate(leds):
        led.value(1 if i == indice else 0)

def ler_joystick():
    return joy_x.read()
