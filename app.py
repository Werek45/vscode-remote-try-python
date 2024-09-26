#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return app.send_static_file("index.html")
import random
"""

def jogar_novamente():
    while True:
        resposta = input("Quer jogar novamente? (s/n): ").lower()
        if resposta == 's':
            return True
        elif resposta == 'n':
            return False
        else:
            print("Resposta inválida. Escolha 's' para sim ou 'n' para não.")

def verificar_vencedor(player, computer):
    if player == computer:
        return "Empate"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "Vitória"
    else:
        return "Derrota"

def jogo():
    opcoes = ['rock', 'paper', 'scissors']
    pontuacao = 0

    while True:
        player_choice = input("Escolha rock, paper ou scissors: ").lower()

        if player_choice not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        computer_choice = random.choice(opcoes)
        print(f"O computador escolheu: {computer_choice}")

        resultado = verificar_vencedor(player_choice, computer_choice)
        if resultado == "Vitória":
            pontuacao += 1
        print(f"Resultado: {resultado}")

        if not jogar_novamente():
            print(f"Pontuação final: {pontuacao}")
            break

# Inicia o jogo
jogo()
"""