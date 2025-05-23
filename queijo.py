import turtle

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("white")
tela.title("Queijo Suíço do Professor")

# Configuração do desenhador (tartaruga)
queijo = turtle.Turtle()
queijo.speed(5)  # Velocidade média

# Desenha o queijo (retângulo amarelo)
queijo.color("yellow")
queijo.begin_fill()
for _ in range(2):
    queijo.forward(200)
    queijo.right(90)
    queijo.forward(150)
    queijo.right(90)
queijo.end_fill()

# Desenha os buracos (círculos pretos)
def fazer_buraco(x, y):
    queijo.penup()
    queijo.goto(x, y)
    queijo.pendown()
    queijo.color("black")
    queijo.begin_fill()
    queijo.circle(10)
    queijo.end_fill()

# Posições aleatórias para os buracos
fazer_buraco(30, -20)
fazer_buraco(80, 40)
fazer_buraco(120, -30)
fazer_buraco(160, 10)
fazer_buraco(60, -60)

# Esconde a tartaruga e finaliza
queijo.hideturtle()
turtle.done()
