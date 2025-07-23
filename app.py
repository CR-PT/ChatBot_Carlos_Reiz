import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

# if comando in ('olá', 'boa tarde', 'bom dia'):
#     return 'Olá tudo bem!'
# if comando == 'como estás':
#     return 'Estou bem, obrigado!'
# if comando == 'como te chamas?':
#     return 'O meu nome é: Bot :)'
# if comando == 'tempo':
#     return 'Está um dia de sol!'
# if comando in ('bye', 'adeus', 'tchau'):
#     return 'Gostei de falar contigo! Até breve...'
# if 'horas' in comando:
#     return f'São: {datetime.now():%H:%M} horas'
# if 'data' in comando:
#     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
# return f'Desculpa, não entendi a questão! {texto}'


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
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break


    print(f'Chat acabou em {datetime.now():%d/%m/%Y %H:%M}')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()