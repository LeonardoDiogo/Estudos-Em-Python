from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def opcao_jogador():
    esc_jogador = input('Escola pedra, papel ou tesoura: ')
    esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print('opção invalida. tente novamente')
        opcao_jogador()


def opcao_Maquina():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


while True:

    print('-' * 30)
    esc_jogador = opcao_jogador()
    print('-' *30)
    esc_maquina = opcao_Maquina()
    print('-' *30)

    if(esc_jogador == 'pedra') and (esc_maquina == 'tesoura') \
        or (esc_jogador == 'papel') and (esc_maquina == 'pedra') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'papel'):
            print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
            ' Resultado: Você Ganhou!!!!')
            jogador_vitorias += 1

    elif esc_maquina == esc_maquina:
       print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
            ' Resultado: Empate!!!!') 

    else:
        print(f'Jogador escolheu {esc_jogador} e a Maquina escolheu {esc_maquina}'
            ' Resultado: Você Perdeu!!!!')
        maq_vitorias += 1

        esc_jogador = opcao_jogador()
        
    print('-' *30)
    print(f'VITORIAS DO JOGADOR: {jogador_vitorias}')
    print(f'VITORIAS DA MAQUINA: {maq_vitorias}')
    print('-' *30)

    esc_jogador = input('voce quer jogar novamente? ')
    if esc_jogador in ['SIM', 'sim', 'Sim', 's', 'S']:
        pass
    elif esc_jogador in ['NAO', 'Nao', 'N', 'n']:
        break
    else:
        break
