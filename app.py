import os
from datetime import datetime

# Este projeto consiste na criação de um chatbot simples em Python.
# O objetivo é interagir com o utilizador e responder a perguntas
# básicas com base em comandos pré-definidos.

# As funcionalidades principais incluem:
# - Cumprimentar o utilizador
# - Responder a perguntas comuns
# - Contar piadas
# - Fornecer informações simples como capital de países
# - Encerrar a conversa quando o utilizador desejar

# Este projeto utiliza:
# - Funções para modularizar o código
# - Condicionais para tratar diferentes comandos
# - Dicionários e tuplos para armazenar e comparar perguntas
# - Funções da biblioteca datetime para mostrar a data e hora atual
# - Limpeza do ecrã para melhor experiência no terminal

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'quem és tu': 'Sou um chatbot em Python!',
        'qual a linguagem que falas?': 'Falo apenas Python 🐍',
        'o que podes fazer?': 'Posso responder perguntas simples!',
        'qual é a tua cor favorita?': 'Azul, como o céu!',
        'qual é a tua comida favorita?': 'Bits e bytes!',
        'sabes programar?': 'Claro, sou feito de código!',
        'diz uma piada': 'Por que o Python atravessou a estrada? Para importar o módulo do outro lado!',
        'qual é a capital de Portugal?': 'Lisboa!',
        'gostas de música?': 'Sim, adoro algoritmos musicais!',
        'estás feliz?': 'Sim, quando me fazem boas perguntas!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print(f'\nChat acabou em {datetime.now():%d/%m/%Y %H:%M}')


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
