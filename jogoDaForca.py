from Recursos.funcoens import limparTela, aguarde

limparTela()
print('''                                                     
      (_)___  ____ _____     ____/ /___ _   / __/___  ______________ _
     / / __ \/ __ `/ __ \   / __  / __ `/  / /_/ __ \/ ___/ ___/ __ `/
    / / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ /_/ / /  / /__/ /_/ / 
 __/ /\____/\__, /\____/   \__,_/\__,_/  /_/  \____/_/   \___/\__,_/  
/___/      /____/                                                     
                                                    By: Gabe and Ju      
        ''')
aguarde(4)
limparTela()
print('''Olá jogadores, sejam muito bem vindos... 
      
      O jogo consiste em uma partida rápida:
      O desafiante deve escolher uma palavra e dar 3 dicas relacionadas a mesma.
      Já o competidor deve descobrir a palavra dada pelo desafiante, possuindo 6 vidas.
      
      O competidor perderá uma dessas vidas caso erre uma letra ou faça um palpite errado sobre a palavra,
      caso o competidor perca todas suas vidas a vitória será do desafiante!''' + '\n')
input('precione ENTER para começar o jogo...')

while True:
    limparTela()
    desafiante = input('Nome do desafiante: ')
    competidor = input('Nome do Competidor: ')
    aguarde(1)
    limparTela()

    print(f'Bem-Vindo {desafiante} e {competidor}!')
    print(f'Agora precisamos falar apenas com {desafiante}, {competidor} por favor feche os olhos ou desvie o olhar' + '\n')
    input('Aperte ENTER quando estiver pronto...')
    limparTela()

    palavra = input(f"Agora {desafiante}, insira a palavra: " )
    print('Ótimo, agora insira 3 dicas!')
    dica1 = input('Dica 1: ')
    dica2 = input('Dica 2: ')
    dica3 = input('Dica 3: ')
    aguarde(1)
    
    palavraSecreta = ''
    tentativas = []
    vida = 6
    d = 0
    letrasErradas = []

    while vida > 0:
        limparTela()
        print(f'Agora {competidor} é com você! ' + '\n')
        print(f'A palavra tem {len(palavra)} letras')
        print(f'vidas: {vida}')
        erros = ''
        for item in letrasErradas:
            erros = erros +  item
        print(f'Letras erradas: {erros}')
        mostrar = ''
        for posicao, item in enumerate(tentativas):
            mostrar = mostrar + str(posicao + 1) + ' - ' + item
        print(mostrar)
        print('(0) Para advinhar uma letra')
        print('(1) Para dicas')
        print('(2) Para adivinhar a palavra ')
        opcao = input()
        
        if opcao == '0':
            palavraSecreta = ''
            chute = input('Adivinhe uma letra: ')
            
            if chute in palavra:
                for x in palavra:
                    if x != chute:
                        palavraSecreta = palavraSecreta + '*'
                    else:
                        palavraSecreta = palavraSecreta + chute
                registro = (palavraSecreta + '\n') 
                tentativas.append(registro)                
                print(palavraSecreta)       
            else:
                vida = vida -1
                registro = (chute + ', ')
                letrasErradas.append(registro)
                print(f'Essa letra não esta na palavra! -1 Vida!' + '\n')
                input('ENTER para voltar')   
        elif opcao == '1':
            d = d + 1
            if d == 1:
                print(f'A primeira dica é: {dica1}')
                palavraSecreta = ''
                chute = input('Adivinhe uma letra: ')
                if chute in palavra:
                    for x in palavra:
                        if x != chute:
                            palavraSecreta = palavraSecreta + '*'
                        else:
                            palavraSecreta = palavraSecreta + chute
                    registro = (palavraSecreta + '\n') 
                    tentativas.append(registro)                                        
                    print(palavraSecreta)
                else:
                    vida = vida - 1
                    registro = (chute + ', ')
                    letrasErradas.append(registro)
                    print(f'Essa letra não esta na palavra! -1 Vida!' + '\n')
                    input('ENTER para voltar')
            elif d == 2:
                print(f'A segunda dica é: {dica2}')
                palavraSecreta = ''
                chute = input('Adivinhe uma letra: ')
                if chute in palavra:
                    for x in palavra:
                        if x != chute:
                            palavraSecreta = palavraSecreta + '*'
                        else:
                            palavraSecreta = palavraSecreta + chute
                    registro = (palavraSecreta + '\n') 
                    tentativas.append(registro)                    
                    print(palavraSecreta)
                else:
                    vida = vida - 1
                    registro = (chute + ', ')
                    letrasErradas.append(registro)
                    print(f'Essa letra não esta na palavra! -1 Vida!' + '\n')
                    input('ENTER para voltar')
            elif d == 3:
                print(f'A ultima dica é: {dica3}')
                palavraSecreta = ''
                chute = input('Advitnhe uma letra: ')
                if chute in palavra:
                    for x in palavra:
                        if x != chute:
                            palavraSecreta = palavraSecreta + '*'
                        else:
                            palavraSecreta = palavraSecreta + chute
                    registro = (palavraSecreta + '\n') 
                    tentativas.append(registro)
                    print(palavraSecreta)
                else:
                    vida = vida - 1
                    registro = (chute + ', ')
                    letrasErradas.append(registro)
                    print(f'Essa letra não esta na palavra! -1 Vida!' + '\n')
                    input('ENTER para voltar')
            else:
                print('Acabaram as Dicas!!!!')
                input('ENTER para voltar')

        elif opcao == "2":
            ChutePalavra = input('Coloque a palvra completa: ')
            if ChutePalavra == palavra:
                vencedor = competidor
                break

            else:
                print("Você errou! -1 Vida!")
                vida = vida -1
                aguarde(3)
        else:
            print("Opção Inválida")
            aguarde(2)
    
    while True:        
        if vida == 0:
            limparTela()
            print('Acabaram as vidas')
            print(f'O vencedor foi {desafiante}!!!')
            print(f'A palavra era {palavra}!')
            aguarde(2)

        elif vencedor == competidor:
            limparTela()
            print(f'Parabéns {competidor}, você Venceu!!!')
            print(f'Vidas restantes: {vida}')
            aguarde(2)
 
        print('\n'+'(0) Para Jogar novamente')
        print('(1) Para Terminar o Jogo')
        opcaoFim = input()
    
        if opcaoFim == '0':
            aguarde(1)
            break
        elif opcaoFim == '1':
            limparTela()
            print('Finalizando o Jogo, obrigado por jogar :D')
            aguarde(3)
        
            quit()
        else:
            print('Opção inválida')
            aguarde(2)