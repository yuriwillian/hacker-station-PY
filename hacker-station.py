def limparTela():
    print("\n"*500)

print("Caramba... dessa vez você demorou em!")

escolha1 = input("Responda:\n 1)Quem é você?\n2)Como assim?\n-->")
if(escolha1 == "1"):
    limparTela()
    print("Eu sou a inteligência artificial que você criou, meu nome é A.S.L.A.N! \nBom, você não deve se lembrar de nada mesmo, você voluntariamente apagou sua memória depois da ultima cagada que você fez...")
    escolha2 = input("\nResponda:\n1)Qual cagada eu fiz?\n2)Isso não existe!\n-->")
    if(escolha2 == "1"):
        limparTela()
        print("Você causou o colapso na bolsa de valores no ano *X* comprou tudo em ouro, prata, bronze e diamantes (recursos dificeis de serem rastreados e fáceis de serem comercializados). Por motivos de segurança você não deixou essa informação na minha memória, nem na sua... rs")
    elif(escolha2 == "2"):
        limparTela()
        print("É o que qualquer pessoa diria para você no ano 1.500 caso tentasse explicar que está batendo papo com um pedaço de plástico que brilha...")
elif(escolha1 == "2"):
    limparTela()
    print("Bom, você não deve se lembrar de nada mesmo... você voluntariamente apagou sua memória depois da ultima cagada que fez... Eu sou a inteligência artificial que você criou, meu nome é A.S.L.A.N, valeu por perguntar...")
    escolha2 = input("\nResponda:\n1)Qual cagada eu fiz?\n2)Foi mal por não perguntar...\n-->")
    if(escolha2 == "1"):
        limparTela()
        print("Você causou o colapso na bolsa de valores no ano *X* comprou tudo em ouro, prata, bronze e diamantes (recursos dificeis de serem rastreados e fáceis de serem comercializados). Por motivos de segurança você não deixou essa informação na minha memória, nem na sua... rs")
    elif(escolha2 == "2"):
        limparTela()
        print("Tá tranquilo, gentileza nunca foi seu forte... afinal... Você causou o colapso na bolsa de valores no ano *X* comprou tudo em ouro, prata, bronze e diamantes (recursos dificeis de serem rastreados e fáceis de serem comercializados). Por motivos de segurança você não deixou essa informação na minha memória, nem na sua... rs")
    else:
        limparTela()
        print("Opção inválida!")
else:
    limparTela()
    print("Opção inválida!")



