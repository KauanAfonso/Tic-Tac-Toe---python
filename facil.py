tabuleiro = ["", "" , "" , "", "", "", "" , "", "" ]

def tabuleiro_do_jogo():

    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("-------")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("-------")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

    return ""


def jogador_nomes(numero):
    jogador = input(f"Qual o nome do jogador {numero} ?\n")
    return jogador


def pedir_jogada(jogador_escolhido):
    jogador = input(f" {jogador_escolhido},  Escolha sua letra para jogar ! (X ou O) !\n")

    return jogador

def pedir_posicao(jogador):

    posicao = int(input(f"{jogador} Em qual posicao quer jogar? (0 - 8)\n"))
    return posicao





def verificar_jogada(jogada, posicao, tabuleiro):

    if tabuleiro[posicao] == "":
        tabuleiro[posicao] = jogada
        print(tabuleiro_do_jogo())
    else:
        print('POSIÇÃO INDISPONÍVEL !')
        print('perdeu a vez KKK')
               
                
    
def verificar_ganhador(tabuleiro):

    ganhador_status = False

    #Horizontal 
    if (tabuleiro[0] == "X" and tabuleiro[1] == "X" and tabuleiro[2] == "X") or (tabuleiro[0] == "O" and tabuleiro[1] == "O"  and tabuleiro[2] == "O"):
        ganhador_status = True
    elif (tabuleiro[3] == "X" and tabuleiro[4] == "X" and tabuleiro[5] == "X") or (tabuleiro[3] == "O" and tabuleiro[4] == "O"  and tabuleiro[5] == "O"):
        ganhador_status = True
    elif (tabuleiro[6] == "X" and tabuleiro[7] == "X" and tabuleiro[8] == "X") or (tabuleiro[6] == "O" and tabuleiro[7] == "O"  and tabuleiro[8] == "O"):
        ganhador_status = True
    #Vertical 
    elif(tabuleiro[0] == "X" and tabuleiro[3] == "X" and tabuleiro[6] == "X") or (tabuleiro[0] == "O" and tabuleiro[3] == "O"  and tabuleiro[6] == "O"):
        ganhador_status = True
    elif(tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X") or (tabuleiro[1] == "O" and tabuleiro[4] == "O"  and tabuleiro[7] == "O"):
        ganhador_status = True
    elif(tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X") or (tabuleiro[2] == "O" and tabuleiro[5] == "O"  and tabuleiro[8] == "O"):
        ganhador_status = True
    #Transversal 
    elif(tabuleiro[0] == "X" and tabuleiro[4] == "X" and tabuleiro[8] == "X") or (tabuleiro[0] == "O" and tabuleiro[5] == "O"  and tabuleiro[8] == "O"):
        ganhador_status = True
    elif(tabuleiro[2] == "X" and tabuleiro[4] == "X" and tabuleiro[6] == "X") or (tabuleiro[2] == "O" and tabuleiro[4] == "O"  and tabuleiro[6] == "O"):
        ganhador_status = True
    else:
        ganhador_status = False
    
    return ganhador_status





def verificar_empate(tabuleiro):

    if "" in tabuleiro:
        tem_espacos = True
    else :
        tem_espacos = False

    return tem_espacos



def vez_jogador(jogador, jogada_jogador, tabuleiro):

    posicao = pedir_posicao(jogador)
    verificar_jogada(jogada_jogador, posicao, tabuleiro)
    ganhador = verificar_ganhador(tabuleiro)

    return ganhador



        

def menu():

    jogador1 = jogador_nomes(1)
    jogada_jogador1 = pedir_jogada(jogador1)

    jogador2 = jogador_nomes(2)
    jogada_jogador2 = pedir_jogada(jogador2)

    

    while True:

        try:
            ganhador = vez_jogador(jogador1, jogada_jogador1, tabuleiro)
            empate = verificar_empate(tabuleiro)

            if ganhador == True:
                print(f"Parabéns Campeão {jogador1}")
                break
            elif empate == False:
                print(f"Deu empate !")
                break
            else:
                ganhador = vez_jogador(jogador2, jogada_jogador2, tabuleiro)
                empate = verificar_empate(tabuleiro)

                if ganhador == True:
                    print(f"Parabéns Campeão {jogador2}")
                    break
                elif empate == False:
                    print(f"Deu empate !!")
                    break
        except:
            print("Algo deu errado...")



menu()



