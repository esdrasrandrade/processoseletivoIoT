from machine import Pin, ADC
import time

print("Teste")  # necessário para o CI

# ====== CONFIG ======
LED_PINS = [4, 5, 2]
BTN_PIN = 26
JOY_X_PIN = 35

DELAY_JOYSTICK = 300      # ms entre movimentos
INTERVALO_PISCA = 200     # ms entre piscadas
PISCADAS_TOTAL = 6        # quantidade de piscadas

# ====== HARDWARE ======
leds = [Pin(p, Pin.OUT) for p in LED_PINS]
button = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)

joy_x = ADC(Pin(JOY_X_PIN))
joy_x.atten(ADC.ATTN_11DB)

# ====== ESTADOS ======
SELECIONANDO = 0
CONFIRMANDO = 1

estado = SELECIONANDO
indice = 0

# ====== CONTROLE DE TEMPO ======
ultimo_mov = 0
ultimo_btn = 0
ultimo_pisca = 0

# ====== CONTROLE DE PISCADAS ======
contador_piscadas = 0
estado_led = 0

# ====== FUNÇÕES ======
def atualizar_leds():
    for i, led in enumerate(leds):
        led.value(1 if i == indice else 0)

def ler_joystick():
    return joy_x.read()

def mover_selecao(valor):
    global indice, ultimo_mov

    agora = time.ticks_ms()

    if time.ticks_diff(agora, ultimo_mov) < DELAY_JOYSTICK:
        return

    if valor < 1500:  # esquerda
        indice -= 1
        ultimo_mov = agora

    elif valor > 2500:  # direita
        indice += 1
        ultimo_mov = agora

    indice %= len(leds)

def verificar_botao():
    global estado, ultimo_btn, contador_piscadas

    agora = time.ticks_ms()

    if time.ticks_diff(agora, ultimo_btn) < 300:
        return

    if button.value() == 0:
        if estado == SELECIONANDO:
            estado = CONFIRMANDO
            contador_piscadas = 0
            print("Selecionado:", indice)

        ultimo_btn = agora

def efeito_confirmando():
    global ultimo_pisca, contador_piscadas, estado_led, estado

    agora = time.ticks_ms()

    if time.ticks_diff(agora, ultimo_pisca) > INTERVALO_PISCA:
        estado_led = not estado_led

        # apaga todos
        for led in leds:
            led.value(0)

        # liga/desliga o selecionado
        leds[indice].value(estado_led)

        ultimo_pisca = agora
        contador_piscadas += 1

        if contador_piscadas >= PISCADAS_TOTAL:
            estado = SELECIONANDO
            atualizar_leds()

# ====== LOOP PRINCIPAL ======
while True:
    valor = ler_joystick()

    if estado == SELECIONANDO:
        mover_selecao(valor)
        atualizar_leds()

    elif estado == CONFIRMANDO:
        efeito_confirmando()

    verificar_botao()