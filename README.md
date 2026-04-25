# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

### 👤 Identificação do Candidato

- **Nome completo:**  Esdras Rodrigues de Andrade
- **GitHub:**  https://github.com/esdrasrandrade

---

## 1️⃣ Visão Geral da Solução

O objetivo deste projeto é implementar uma interface embarcada de seleção interativa, inspirada em sistemas de navegação de menus de videogames, utilizando um joystick analógico e um microcontrolador ESP32.

O sistema permite ao usuário navegar entre diferentes opções (representadas por LEDs) através do eixo horizontal do joystick. A seleção é confirmada por meio de um botão físico, acionando um feedback visual temporário (piscadas do LED selecionado).

A interação ocorre da seguinte forma:

Movimentação do joystick → altera a seleção
Pressionamento do botão → confirma a opção selecionada
Feedback visual → indica confirmação por piscadas.

---

## 2️⃣ Arquitetura do Sistema Embarcado

O sistema foi projetado utilizando uma abordagem baseada em máquina de estados finitos (FSM), garantindo clareza na lógica e separação de responsabilidades.

Estados do sistema:
SELECIONANDO: leitura contínua do joystick e atualização da seleção
CONFIRMANDO: execução de efeito visual (piscadas) após confirmação
Fluxo principal (main loop):
Leitura do valor analógico do joystick (ADC)
Interpretação da direção (esquerda/direita)
Atualização do índice de seleção (com comportamento circular)
Verificação do botão com debounce lógico
Execução do comportamento conforme o estado atual
Controle de tempo:

A temporização é realizada utilizando time.ticks_ms(), evitando delays bloqueantes (sleep) e garantindo execução contínua e responsiva.

Interação entre componentes:
Joystick → ADC → Processamento → Atualização de estado → LEDs
Botão → Entrada digital → Mudança de estado → Feedback visual
---

## 3️⃣ Componentes Utilizados na Simulação
- ESP32 DevKit V4
- Microcontrolador responsável pelo processamento e controle do sistema
- Joystick analógico
- Entrada principal do usuário (eixo horizontal para navegação)
- Botão (pushbutton)
- Entrada digital para confirmação de seleção
- 3 LEDs (azul, vermelho, amarelo)
- Representam as opções disponíveis no sistema
- Resistores (1kΩ)
- Limitam a corrente nos LEDs, garantindo segurança do circuito

Função das componentes:
Joystick: Navegação entre opções.
Botão: Confirmação da escolha.
LEDs: Feedback visual do sistema.
Resistores: Proteção elétrica.
---

## 4️⃣ Decisões Técnicas Relevantes
- Uso de máquina de estados (FSM)
- Separação clara entre navegação e confirmação, melhorando organização e escalabilidade.
- Temporização não-bloqueante
- Utilização de time.ticks_ms() para evitar travamento do sistema e permitir leitura contínua dos inputs.
- Debounce lógico do botão
- Implementado via controle de tempo, evitando múltiplas leituras indesejadas.
- Modularização do código
- Separação em funções específicas:
- leitura de joystick
- movimentação de seleção
- atualização de LEDs
- verificação de botão
- efeito visual
- Comportamento circular da seleção
- Implementado com operador módulo (%), garantindo melhor experiência de navegação.

---

## 5️⃣ Resultados Obtidos

O sistema apresentou comportamento correto e estável durante a simulação:

- Navegação fluida entre LEDs via joystick
- Atualização imediata da seleção
- Confirmação funcional via botão
- Execução do efeito de piscadas com temporização controlada
- Retorno automático ao modo de seleção após confirmação

A simulação foi validada com sucesso no ambiente Wokwi, incluindo execução automatizada via GitHub Actions, garantindo integridade do projeto em ambiente de integração contínua.
---

## 6️⃣ Comentários Adicionais
Dificuldades:
- Ajuste da leitura analógica do joystick (definição de thresholds)
- Implementação de temporização sem uso de delays bloqueantes
- Compatibilidade de métodos entre versões do MicroPython
Limitações:
- Interface visual limitada ao uso de LEDs
- Ausência de persistência de dados (estado não é salvo após reinicialização)
Melhorias futuras:
- Adição de display OLED para interface mais rica
- Armazenamento da seleção em memória flash
- Integração com comunicação IoT (MQTT ou HTTP)
Principais aprendizados:
- Aplicação prática de máquina de estados em sistemas embarcados
- Controle de tempo eficiente sem bloqueio
- Integração entre hardware simulado e lógica de firmware
- Importância de organização e clareza no código  

---

