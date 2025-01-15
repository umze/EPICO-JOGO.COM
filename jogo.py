import time
import random
import platform
import os
import pygame
pygame.mixer.init()
mrbeastsom = pygame.mixer.music.load('mrbeast.mp3')

pcnome = platform.node()
so = platform.platform

for i in range(30):
    print("")
nome = input("Quero teu nome, mim de teu nome: ")
if nome == "Gui Nasci Nasci" or nome == "gui nasci nasci":
    print("FINAL: 1K DE SEGUIDORRRRRRRRR")
    print("Parabéns, vc tem mtos seguidores :)")
    input()
    exit()
if nome == "":
    print("FINAL: SEM NOME")
    print("Fim de jogo, cade teu nome?")
    input()
    exit()
if nome == pcnome:
    print("FINAL: VOCÊ É VOCÊ!!!!")
    print("Fim de jogo, você pôs o nome do seu PC omg")
    input()
    exit()
if nome == "BOB":
    for i in range(30):
        print()
    print("FINAL: BOB REALLY LIKES PEOPLE")
    print(":)")
    for i in range(10):
        print()
    input("")
    exit()
if nome == "Ciano" or nome == "ciano":
    print("FINAL: EJETADO")
    print("you sussy amogmus imopstor")
    input()
    exit()
rg = int(input("agr teu rg becas iés:"))
idade = int(input("Idade: "))
if idade > 150:
    print("FINAL: VÉIO DEMAIS PRA JOGAR")
    print(f"meu mano, nem fudendo que tu tem {idade} anos de idade")
    input()
    exit()
if idade < 0:
    print("FINAL: TU NEM NASCEU AINDA")
    print(f"mano, como que tu tem {idade} anos?")
    input()
    exit()
if idade < 10:
    print("FINAL: NOVINHO DEMAIS")
    print("tu é mto novinho para conhecer meu jogo, daqui uns anos cê volta")
    input("")
    exit()

print("")

if nome == "Impostor" and rg == 945360:
    print("HMMMMM, você é o impostor ent? Bora fazer o seguinte, 1 para matar geral ou 2 para continuar o jogo")
    escolhaimpostor = int(input("Sua resposta: "))
    if escolhaimpostor == 1:
        print("FINAL: SUS")
        print("Fim de jogo, você entrou na vent mas não tinha oxigênio, tinha venenogênio.")
        input()
        exit()
    elif escolhaimpostor == 2:
        print("FINAL: IMOPSOR")
        print("Fim de jogo, você tenta continuar sua partida de Among Us na vida real, e... você sabe o pq eu terminei o jogo aqui")
        input()
        exit()
    elif escolhaimpostor == 3:
        print("FINAL: NÃO SEI?")
        print("Você bebeu água e disse: me sussy amognus ipnopsor")
        input()
        exit()

if nome == "abcdefghijklmnopqrstuvwxyz" and rg == 1234567890 or nome == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"and rg == 1234567890:
    print("FINAL: ALFABETO")
    print("Fim de jogo, cria um nome melhor, seu sem criatividade :)")
    input()
    exit()

if nome == "Leonardo" and rg == 10620240192:
    print("FINAL: O CRIADOR FOI CLONADO")
    print("Fim de jogo, seu hacker, pra que roubar os meus dados caramba? Desinstala essa bomba e se joga da janela!")
    input()
    exit()
for i in range(5):
    print("")
print(f"Olá seu ser vivo chamado {nome} com sua identidade {rg}, preciso saber teu dinheiro para definir seu estilo de vida.com.br. Ah e você não tem nenhum centavo, então.... Quanto de dinheiro vc tem?")
dinheiro = int(input("R$"))

def parte3():
    assalto = random.randint(1,100)
    assaltochance = int(25)
    if nome == "Vitinho":
        assaltochance = int(40)
    if assalto >= assaltochance:
        if dinheiro == 0:
            print("FINAL: TEM NADA PARA ASSALTAR MEU MANO")
            print("Você não tem dinheiro mas o assaltante queria te assaltar")
            input()
            exit()
        input(f"Você encontra um assaltante querendo roubar todo o seu dinheiro (R${dinheiro}) do seu almoço para fazer a Engenhoteca")
        if nome == "Vitinho":
            print(f"E agora {nome}? O que você vai fazer? Digite 1 para matar ele, 2 para deixar ele roubar seu dinheiro, 3 para chamar ele para comer um churrasquinho do domingo, 4 para assaltar ele em vez dele te assaltar (pode resulta em morte 💀), 5 para fugir ou 6 para dobra e passar para a próxima pessoa.")
        else:
            print(f"E agora {nome}? O que você vai fazer? Digite 1 para matar ele, 2 para deixar ele roubar seu dinheiro, 3 para chamar ele para comer um churrasquinho do domingo, 4 para assaltar ele em vez dele te assaltar (pode resulta em morte 💀) ou 5 para fugir.")
        escolha1 = int(input("Minha resposta: "))
        if escolha1 == 6 and nome == "Vitinho":
            print("FINAL: NÃO HOUVE ENGENHOTECA")
            print("Meio que o assaltante após a sua fala, dobrou o assalto e assaltou a professora, que merda....")
            input()
            exit()
        if escolha1 == 1:
            final2 = random.randint(1,2)
            if final2 == 2:
                print("FINAL: MORTO")
                print("Fim de jogo, ele te matou pq ele tinha uma Ak-47 e você só tinha uma Nerf do Fortnite")
                input()
                exit()
            else:
                print("FINAL: BRITANICO")
                print(f"Fim de jogo, você esfaqueou o assaltante com uma faquinha de plástico e comprou o almoço com o dinheiro dele e pegou seu dinheiro e comprou um Switch (sim, ele ta custando R${dinheiro},00)")
                input()
                exit()
        elif escolha1 == 2:
            print("FINAL: DEPRESSÃO")
            print(f"Fim de jogo, você fica chorando por conta que você perdeu R${dinheiro} e entra em depressão = morte 💀")
        elif escolha1 == 3:
            rgdenovo = int(input("Fale seu RG para ele para dar certo"))
            if rgdenovo == rg:
                print("FINAL: BOM")
                print("Fim de jogo, você chama ele pro churrasco e virou amigo dele :)")
                input()
                exit()
            else:
                print("FINAL: PÔ TU NÃO SABE SE IDENTIFICAR?")
                print("Fim de jogo, pois tu não sabe nem teu rg (além de que você escreveu alguns segundos atrás), ai n da meu")
                input()
                exit()       
        elif escolha1 == 4:
            print("")
            final = int(random.randint(1,3))    
            if final == 1:
                print("FINAL: MORTO pt.2 (é pq tem outro final chamado morto)")
                print("Fim de jogo, você foi assaltar ele mas acabou percebendo e te deu um tiro de Ak-47")
                input()
                exit()
            elif final == 2:
                print("FINAL: ASSALTOU MAS MORREU")
                print("Fim de jogo, você conseguiu assaltar mas logo ele percebeu e te deu um tiro de Ak-47")
                input()
                exit()
            elif final == 3:
                print("FINAL: VOCÊ ASSALTOU ELE COM SUCESSO!")
                print(f"Você conseguiu assaltar R$100 do bolso dele e conseguiu fugir, agora você tem R${dinheiro + 100}, parabéns!")
                input()
                exit()
        elif escolha1 == 5:
            deucerto = random.randint(1,2)
            if deucerto == 1:
                print("FINAL: DEU RUIM...")
                print("Éééééééééééé.............. você morreu 💀")
                input()
                exit()
            else:
                input("Você conseguiu correr, boa bonito")
                input("Mas e agora? Você vai para onde?")
                print("1 = Casa | 2 = Engenhoteca | 3 = Na verdade, acho que vou matar ele...")
                escolha10 = int(input(f"{nome}: Eu vou para o local número "))
                if escolha10 == 1:
                    print("FINAL: ATROPELADO")
                    print("Você corre para a rua mas não vê o carro, então você morre...")
                    input()
                    exit()
                elif escolha10 == 2:
                    print("FINAL: ENGENHOTECA")
                    print("Você faz aula normal mas foi assaltado depois ;-;")
                    input()
                    exit()
                elif escolha10 == 3:
                    print("FINAL: BRITANICO (de novo?)")
                    print("Você matou ele de novo? Com a faquinha de plástico? meu deus... tem cada final repetido aqui ;-;")
                    input()
                    exit()
                else:
                    print("FINAL: NÃO FOI POSSIVEL FUGIR")
                    print("Você não se decidiu e foi assaltado.")
                    input()
                    exit()
        else:
            print("FINAL: INDECISO ENTÃO FOI ASSALTADO")
            print("Você não se decidiu então foi assaltado")
            input()
            exit()
    else:
        input("Parece que você ainda não foi assaltado, que bom...")
        if nome == "Prof. Bia" or nome == "prof. bia" or nome == "professora bia" or nome == "prof bia" or nome == "Professora Bia" or nome == "Prof Bia":
            print("FINAL: DEI AULA DE ENGENHOTECA HOJE E SEXTOU!!!!!!!!!!!!!!!!")
            print("Você deu aula de Engenhoteca e foi isso :)")
            input()
            exit()
        input("Então, na aula da Engenhoteca, a professora deu três opções de aula, ou aula usando Minecraft, usando LEGO ou Robótica")
        print("")
        print("1 = Minecraft | 2 = LEGO | 3 = Robótica")
        escolha6 = int(input("Sua resposta:"))
        if escolha6 == 1:
            print("")
            input("Quando você abriu o Minecraft, a energia caiu, abrindo um portal que te sugou e levou para o mundo de Minecraft")
            input("Meio que você está preso :( então o que deseja fazer?")
            print()
            print("1 = Tentar fugir desse mundo | 2 = Ir pegar madeira")
            escolha7 = int(input("Sua resposta: "))
            if escolha7 == 1:
                minecraftfugir = random.randint(1,100)
                if minecraftfugir >= 70:
                    print("FINAL: VOCÊ FALHOU MISERAVELMENTE E DESINTEGROU")
                    print("Como que você vai gerar um portal?")
                    input()
                    exit()
                else:
                    print("FINAL: VOCÊ FUGIU!")
                    print("Parabéns, você saiu do mundo do Minecraft e trouxe redstone, como eu não sei, mas ta bom.")
                input()
                exit()
            else:
                print("FINAL: VOCÊ ZEROU O MINEEEEE")
                print("boa bonito(a), tu zeraste el mincraf")
                input()
                exit()
        elif escolha6 == 2:
            print("FINAL: LEGO")
            print("Você construiu uma Torre Eifel e ficou feia pa car-")
            input()
            exit()
        elif escolha6 == 3:
            print("FINAL: ROBO CHEFÃO")
            print("é... ele destruiu o mundo")
            input()
            exit()
        else:
            print("FINAL: DECIDE LOGO MEU")
            print("Você não decidiu então você foi embora")

def parte2():
    print("Então você decide faltar? Tem certeza mesmo?")
    print("Esquece, vou para a Engenhoteca = 1 | Sim, tenho certeza = 2")
    if nome == "Prof. Bia" or nome == "prof. bia" or nome == "professora bia" or nome == "prof bia" or nome == "Professora Bia" or nome == "Prof Bia":
        print("FINAL: DEMITIDO")
        print("Por acaso você esqueceu que tu trabalha na Engenhoteca?")
        input()
        exit()
    time.sleep(3)
    escolha2 = int(input(""))
    if escolha2 == 2:
        input("Ta né? Então, vamos continuar")
        input("Bom, antes de você ir na sua casa, bate uma fome gigantesca")
        print("Você quer ir pro Santa Cruz para almoçar?")
        print("Sim = 1 | Não = 2")
        print()
        escolha3 = int(input("Sua Resposta:"))
        if escolha3 == 2:
            print()
            input("Você chega em casa e não acha a sua mãe, talvez ela foi para o Pão de Açúcar, estranho....")
            print("Mas quando menos esperava...")
            print()
            input("Você lembrou que não havia comido há um mês, como, eu não sei, mas você não comeu por conta que foi assaltado.")
            print(f"E agora {nome}? O que você irá fazer?")
            print("1 = Almoçar | 2 = Não comer | 3 = Pegar o carro da sua mãe e ir para algum restaurante | 4 = Esperar sua mãe chegar do Pão de Açúcar")
            escolhacasa = int(input("Sua resposta: "))
            if escolhacasa == 2:
                print("FINAL: TÔ COM FOME PORRA")
                print("Fim de jogo, você morre de fome e sua mãe chora por ver você caído no chão durasso.")
                input()
                exit()
            if escolhacasa == 1:
                print("FINAL: A JUSTIFICATIVA DE SUA MÃE TER IDO AO PÃO DE AÇÚCAR")
                print("É.... você morreu.")
                input()
                exit()
            if escolhacasa == 3:
                if idade < 18:
                    print("FINAL: POR ACASO VOCÊ TEM HABILITAÇÃO PARA DIRIGIR?")
                    print("Mano tu é menor de idade, nunca jogou uma simulação de carro, como que você vai dirigir essa merda?")
                if idade >= 18:
                    print("FINAL: UFA, AINDA VOU ESTAR VIVO, eu acho....")
                    print("Você pegou o carro da sua mãe mas você só sabe dirigir com carro automático, e o carro da sua mãe é manual, meio que você bateu na GARAGEM DE SUA CASA, parabéns!")
                    input()
                    exit()
            if escolhacasa == 4:
                print("FINAL: O PÃO DE AÇÚCAR NÃO É PERTO DE CASA")
                print("É... tu mora longe pa carai, no meio do mato, então é... o Pão de Açúcar fica na pqp e vc morreu de fome, *oof :clap:")
                input()
                exit()
        else:
            if nome == "Julia Sayuri" or  nome == "julia sayuri" or nome == "Julia sayuri" or nome == "julia Sayuri":
                print("FINAL: FUI COMER NO SHOPPING COM A SOPHIA E OLHA NO QUE DEU!!!!!!!!!!!")
                print(f"{nome}: Não tinha spoleto, comi a sophia sarro depois de fazer a bosta da prova da omu, vsfd prova corna do caralho e a porra da buceta da ana laura nem ajudou a fazer aquela bosta, vsfd sua vadia estupida ridicula do caralho.")
                input()
                exit()
            print("")
            input("Partiu então um almocinho gostosinho das boas :)")
            input("Você chega lá no Santa Cruz e vê várias hamburguerias e pizzarias e churrascarias")
            print("Qual restaurante você vai?")
            print("Mania do Churrasco = 1 | Burguer King = 2 | McDonald's = 3 | Pizza Hut = 4 | Slopeto = 5")
            escolha4 = int(input("Sua resposta: "))
            print()
            if nome == "Kevin" or nome == "kevin":
                print("FINAL: VOCÊ NÃO VAI PARA O SHOPPING NÃO SEU GORDO")
                print("Devido ao paradóxo dos nomes ao contrário, você vai casa comer slopeto, não vai chamar ninguém mas só o Garibmel que spawnou")
                input("")
                exit()
            if escolha4 == 4:
                restaurante = "Pizza Hut"
                print("Então escolha alguma coisa do cardápio")
                input("1: Pizza de Calabreza")
                input("2: Pizza de Sorvete")
                input("3: Pizza de Apple")
                input("4: Pizza de Abacate")
                print("Qual você quer?")
                pizza = int(input(f"{nome}: Pode me ver o número "))
                if pizza == 3:
                    print("FINAL: VEM COM IPHONE DENTRO?")
                    print("Fim de jogo, você ficou rico porque tinha iPhone, Macbook Pro e iPad de ultima geração dentro da pizza e vendeu tudo para comprar Android porque o criador do jogo odeia iOS e iPadOS")
                    input()
                    exit()
                if pizza == 2:
                    print("FINAL: CÉREBRO CONGELADO")
                    print("Fim de jogo, você pede uma Pizza de sorvete e acaba perdendo o cérebro pois ficou tão frio que depois que você saiu do shopping tava um calor de 40˚C e perdeu o cérebro")
                    input()
                    exit()
                if pizza == 1:
                    print("FINAL: GOSTOSO DEMAIS!!!")
                    print("Você comeu a pizza mais normal que tinha e foi embora feliz :)")
                    input("")
                    exit()
                if pizza == 4:
                    if nome == "João" and rg == 10620230388 and idade == 13:
                        print("FINAL: PIOR PIZZA DO MUNDO PLMDS PRA QUE EXISTE ISSO?")
                        print("pra que pizza de abacate?")
                        input()
                        exit()
                    else:
                        print("FINAL: SÓ JOÃO QUE PODE COMER")
                        print("Tu n pode fí, só o João")
                        input()
                        exit()
                else:
                    print("FINAL: NÃO QUERO NADA")
                    print(f"Você saiu do {restaurante} sem nada para comer")
                    input("")
                    exit("")
            if escolha4 == 1:
                restaurante == "Mania do Churrasco"
                print(f"Então você foi para o Mania do Churrasco, com muita fome, escolha algum item do cardápio")
                print("1: Coração")
                print("2: Picanha")
                print("3: Frango")
                print("Escolha")
                input(f"{nome}: Me vê o número ")
                print("FINAL: GOSTOSO DEMAIS!!!")
                print("Você comeu o churrasco e foi embora feliz :)")
                input("")
                exit()
            if escolha4 == 2:
                print("FINAL: COMI E SÓ")
                print("Você comeu um hamburguer e foi embora feliz :)")
                input("")
                exit()
            if escolha4 == 3:
                input("Então você foi para o McDonald's e um funcionário disse:")
                input(f"Funcionário: Olá {nome}!")
                input(f"{nome}: Co-como você sabe meu nome?")
                input(f"Funcionário: Tá no teu crachá burro. Mas enfim...")
                input(f"Funcionário: Você quer trabalhar por uma hora no Mc?")
                print()
                print("1 = Sim | 2 = Não")
                escolha8 = int(input(f"{nome}: "))
                if escolha8 == 1:
                    print("FINAL: VOCÊ É O RONALD MCDONALD!")
                    print("É... tu é o Ronald agora, fim de jogo")
                    input("")
                    exit()
                else:
                    print("FINAL: NÃO! SÓ QUERO UM BURGÃO")
                    print("Você pede um hambúrguer e vaza.")
                    input()
                    exit()
            if escolha4 == 5:
                if nome == "nivek" or nome == "nivec" or nome == "niveK" or nome == "niveC":
                    print("FINAL: VOCÊ FOI NO SLOPETO")
                    print("Você chamou o onarriodeL, Ebu, NickMism, Julia Sayuri, Renanzitos, Gui Nasci Nasci, Luca, Garibmel (que não foi pq o cara só trabalha e mais nada), Vitim e o Nicolau (mas ele comeu o prato kids)")
                    input()
                    exit()
                else:
                    print("FINAL: VOCÊ NÃO É O KEVIN")
                    print("Já que você não é o Kevin, você não vai ir no Slopeto ou spoleto fds, parabmens")
                    input("")
                    exit()

    elif escolha2 == 1:
        print("FINAL: INDECISO")
        print("Escolhe um né meu, ou vai ou não vai meu.")
        input()
        exit()


def parte1():
    arquivo = open("save.txt", "w")
    arquivo.write("feito = 0")
    arquivo.close()
    input(f"Certo dia, {nome} foi para o Arquidiocesano estudar Baskara. Teve aula com o Digão, e ele ensinou um negócio mto daora. Faça o exercício para continuar")
    if nome == "Digão":
        
        input("Pera")
        input("Você que é o Digão")
        input("Então meio que você passou exercício para sí mesmo?")
        print("FINAL: EVENTO CANONICO?")
        print("Você é o Digão omg")
        input()
        exit()
    print("Executando arquivo 'matematica.py'...")
    os.system("python matematica.py")
    arquivo = open("save.txt", "r")
    conteudo = arquivo.read()
    if conteudo == "feito = 2" or conteudo == "feito = 0" or conteudo == "":
        print("FINAL: VOCÊ TIROU 0")
        print("Você falhou na matemática e chorou eternamente porque você ficou triste")
        arquivo.close()
        input("")
        exit()
    else:
        print("")
        arquivo.close()
    input(f"Após fazer o exercício, {nome} lembrou que tinha Engenhoteca, mas estava um pouco cansado, ai que vem uma pergunta")
    
    print()
    print(f"{nome}: Será que hoje eu vou para a Engenhoteca ou eu vou para casa faltar a Engenhoteca?")
    print("Vou ir para a Engenhoteca = 1 | Não vou ir, vou faltar a Engenhoteca = 2")
    time.sleep(3)
    escolha2 = int(input(""))
    if escolha2 == 1:
        print()
        print()
        parte3()
    elif escolha2 == 2:
        print()
        print()
        parte2()
if dinheiro > 1000 and idade < 18:
    print(f"FINAL: NOVINHO DEMAIS PARA TER R${dinheiro},00")
    print("Quer armazenar tanto dinheiro? Mas nem idade tu tem direito")
    input()
    exit()
if dinheiro <= 0:
    print("FINAL: TÔ SEM GRANA")
    print("Fim de jogo, coloca pelo menos 1 real vai")
    input()
    exit()
if dinheiro > 10000:
    input("Bom, você é rico, mas no seu celular rodou uma propaganda de um programa de caridade, quer doar 90% do seu dinheiro?")
    print(f"1 = Doar | 2 = Não")
    print()
    caridade = int(input("Sua resposta: "))
    if caridade == 1:
        print("FINAL: HUMILDE")
        print(f"Você doou dinheiro")
        input()
        exit()
    else:
        print("FINAL: DESUMILDE DO CARALHO")
        print("Doar é bom para ajudar pessoas, coisa que  você deveria fazer.")
        input()
        exit()
    input()
    exit()
if dinheiro < 100:
    input("Você não tem dinheiro suficiente para pagar o almoço")
    print(f"E agora {nome}? O que você vai fazer?")
    print("1 = Não comer | 2 = Assaltar | 3 = Apostar no Tigrinho | 4 = Mendigar dinheiro grátis")
    escolhashopping = int(input(f"{nome}: Acho que a opção N˚"))
    if escolhashopping == 1:
        print()
        print("FINAL: HOJE NÃO VAI ROLAR ALMOÇO")
        print("É.... não vai ter almoço hoje :(")
        input()
        exit()
    if escolhashopping == 2:
        print()
        print("FINAL: ROUBEI :)")
        print("Você assaltou dinheiro, mas depois morreu")
        input()
        exit()
    if escolhashopping == 3:
        print("Você pega seu celular e abre o Tigrinho")
        print("")
        input("Bem vindo ao Tigrinho!")
        print()
        print("COMO FUNCIONA O JOGO")
        input("Tigrinho mais conhecido também como Fortune Tiger é um site de apostas, aqui será a mesma coisa, só é em dinheiro virtual, você bota o valor e o quanto quer aumentar, dependo de sua escolha as chances mudam, não é aceito centavos de aposta, aperte ENTER para continuar no jogo")
        tigrinho = 0
        while tigrinho == 0:
            print()
            print("Quanto que você quer colocar de dinhero dentro do jogo?")
            print(f"Saldo: R${dinheiro},00")
            dinheiroapostado = int(input("Vou botar no jogo R$"))
            if dinheiroapostado > dinheiro:
                print("Saldo insuficiente para jogar.")
            elif dinheiroapostado <= dinheiro:
                print("")
                print("Você quer multiplicar quanto de seu dinheiro?")
                print()
                print(f"2: {dinheiroapostado} para {dinheiroapostado * 2} (2x{dinheiroapostado}) - 40%")
                print(f"3: {dinheiroapostado} para {dinheiroapostado * 3} (3x{dinheiroapostado}) - 30%")
                print(f"4: {dinheiroapostado} para {dinheiroapostado * 4} (4x{dinheiroapostado}) - 15%")
                print(f"5: {dinheiroapostado} para {dinheiroapostado * 5} (5x{dinheiroapostado}) - 5%")
                print("")
                escolha = int(input("Vou querer o multiplicador "))
                print("")
                aposta = random.randint(1,100)
                if escolha == 2:
                    multiplicador = 40
                elif escolha == 3:
                    multiplicador = 30
                elif escolha == 4:
                    multiplicador = 15
                elif escolha == 5:
                    multiplicador = 5
                if aposta < multiplicador:
                    dinheiro = dinheiro + (dinheiroapostado * escolha - dinheiroapostado)
                    print("VOCÊ GANHOU!")
                    print(f"Agora seu saldo é R${dinheiro}")
                    print("Digite 2 para parar de jogar")
                    jogar = input("Sua resposta: ")
                    if jogar == "2":
                        if dinheiro < 100:
                            input("Bom, você decidiu para o jogo, mas ainda não consegue pagar o almoço")
                            input("Então você morre de fome")
                            print("FINAL: NÃO TENHO COMIDA")
                            print("Bom, você não vai conseguir comer, porque nesse jogo, a inflação foi pro car-")
                            input()
                            exit()
                        print("Fechando jogo, aguarde")
                        time.sleep(3)
                        print("")
                        tigrinho = 2
                else:
                    dinheiro = dinheiro - dinheiroapostado
                    print("VOCÊ PERDEU!")      
                    if dinheiro == 0:
                        print()
                        input("Seu dinheiro acabou")
                        print("Fechando jogo, aguarde")
                        time.sleep(3)
                        input("Quando você remove seus olhos do celular você ve o MrBeast")
                        input("Você fica impressionado e ele disse")
                        pygame.mixer.music.play()
                        print("MrBeast: Olá meu consagrado, você quer dinheiro?")
                        print("1 = Sim | 2 = Não")
                        print()
                        aceitamrbeast = int(input("Sua resposta: "))
                        if aceitamrbeast == 2:
                            print("FINAL: PERDEU A CHANCE")
                            print("É... você não pagou o almoço")
                            input()
                            exit()
                        else:

                            dinheirosorte = random.randint(1,100)
                            if dinheirosorte > 30:
                                pygame.mixer.music.play()
                                input("MrBeast: Ok, aqui está R$1Mi de reais.")
                                print("")
                                print("FINAL: MILIONÁRIO")
                                print("O MrBeast deu bastante dinheiro pra tu, boa")
                                input()
                                exit()
                            if dinheirosorte <= 30:
                                pygame.mixer.music.play()
                                input("MrBeast: Ok, aqui está 2 reais, tchau")
                                print()
                                print("FINAL: MRBEAST DESUMILDE")
                                print("É... Não deu para pagar o almoço")
                                input()
                                exit()
                    print(f"Agora seu saldo é R${dinheiro}")
                    print("Digite 2 para parar de jogar")
                    jogar = input("Sua resposta: ")
                    if jogar == "2":
                        print("Fechando jogo, aguarde")
                        time.sleep(3)
                        print("")
                        if dinheiro < 100:
                            print()
                            print("FINAL: PERDEU NO TIGRINHO")
                            print("Você não conseguiu dinheiro, F")
                            input()
                            exit()
                        tigrinho = 2
        print("")
    if escolhashopping == 4:
        print("FINAL: NÃO DEU")
        print("Não rolou a mendigagem meu")
        input()
        exit()
    input("Bem vindo de volta ao EPICO JOGO.COM, vamos continuar")
    print("")
    parte1()
else:
    parte1()
