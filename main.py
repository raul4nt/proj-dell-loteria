import random
#Biblioteca random, usada no código pra gerar números aleatórios
from time import sleep
#Comando sleep da biblioteca time, usada no código pra pausar o console para uma melhor visualização

usuarios_cadastrados = [
    {'id': 1, 'nome': 'Raul', 'cpf': '0', 'senha': '0', 'admin': True},
    #Coloquei assim pra testar mais rápido as funções de admin
    {'id': 2, 'nome': 'João', 'cpf': '2', 'senha': '2'},
    #Coloquei assim pra testar mais rápido as funções de usuário
    {'id': 3, 'nome': 'Maria', 'cpf': '04953933044', 'senha': 'atcpatcpi'},
    {'id': 4, 'nome': 'Ana', 'cpf': '95274808093', 'senha': '123aninha'},
    {'id': 5, 'nome': 'Pedro', 'cpf': '25462791062', 'senha': 'aleeeluia'},
    {'id': 6, 'nome': 'Fernanda', 'cpf': '01058513028', 'senha': 'senhapassword'},
    {'id': 7, 'nome': 'Carlos', 'cpf': '60630794081', 'senha': 'saladafrutas321'},
    {'id': 8, 'nome': 'Mariana', 'cpf': '68893223040', 'senha': 'windowsxphaha'},
    {'id': 9, 'nome': 'Gabriel', 'cpf': '25392436064', 'senha': '1', 'admin': True},
    {'id': 10, 'nome': 'Juliana', 'cpf': '34949156012', 'senha': 'apple444'},
    {'id': 11, 'nome': 'Lucas', 'cpf': '33657401040', 'senha': 'campominado'},
    {'id': 12, 'nome': 'Aline', 'cpf': '60218425023', 'senha': '9876543dois'},
    {'id': 13, 'nome': 'Rafael', 'cpf': '90021095043', 'senha': 'senhasenha'},
    {'id': 14, 'nome': 'Patricia', 'cpf': '88061785048', 'senha': 'cocada123'},
    {'id': 15, 'nome': 'Roberto', 'cpf': '65794339063', 'senha': 'bemtevi333'}
    #Dicionário com todos os usuarios cadastrados; possui id com autoincremento(realizado na função
# de cadastro), nome, cpf, senha e, se for admin, uma chave admin com um valor boolean True
]

todas_as_apostas = [
     {'id_apostador': 1, 'aposta': [2, 26, 33, 5, 9], 'id_aposta': 1000},
    {'id_apostador': 1, 'aposta': [2, 5, 1, 3, 4], 'id_aposta': 1001},
    {'id_apostador': 2, 'aposta': [26, 33, 5, 9, 23], 'id_aposta': 1002},
    {'id_apostador': 2, 'aposta': [30, 15, 19, 1, 2], 'id_aposta': 1003},
    {'id_apostador': 3, 'aposta': [33, 5, 9, 23, 30], 'id_aposta': 1004},
    {'id_apostador': 3, 'aposta': [3, 5, 2, 4, 1], 'id_aposta': 1005},
    {'id_apostador': 4, 'aposta': [5, 9, 23, 30, 15], 'id_aposta': 1006},
    {'id_apostador': 4, 'aposta': [19, 1, 2, 26, 33], 'id_aposta': 1007},
    {'id_apostador': 5, 'aposta': [9, 23, 30, 15, 19], 'id_aposta': 1008},
    {'id_apostador': 6, 'aposta': [2, 3, 5, 10, 15], 'id_aposta': 1009},
    {'id_apostador': 6, 'aposta': [7, 12, 18, 25, 32], 'id_aposta': 1010},
    {'id_apostador': 6, 'aposta': [1, 7, 11, 20, 28], 'id_aposta': 1011},
    {'id_apostador': 6, 'aposta': [8, 15, 17, 21, 35], 'id_aposta': 1012},
    {'id_apostador': 11, 'aposta': [2, 9, 16, 22, 45], 'id_aposta': 1013},
    {'id_apostador': 12, 'aposta': [10, 20, 25, 30, 40], 'id_aposta': 1014},
    {'id_apostador': 12, 'aposta': [3, 6, 9, 18, 27], 'id_aposta': 1015}, 
    {'id_apostador': 13, 'aposta': [1, 10, 19, 26, 33], 'id_aposta': 1016},
    {'id_apostador': 15, 'aposta': [11, 21, 31, 41, 50], 'id_aposta': 1017},
    {'id_apostador': 15, 'aposta': [4, 13, 24, 36, 49], 'id_aposta': 1018}
    #Dicionário com todas as apostas já feitas: possui id_aposta com autoincremento(realizado na função de registrar 
 # aposta), a aposta que o usuário fez(seja ela surpresa ou tradicional) e o id do apostador correspondente(aquele que fez 
# a aposta). Isso tudo feito de maneira automática na função de registro. 
]

# Podemos dizer que existe relação entre os dois dicionários, pois o id_apostador da tabela todas_as_apostas é o id do usuário
# da tabela usuarios_cadastrados.

valor_premio_fixo = 10000000
# Setando o valor padrão do prêmio
numeros_permitidos = range(1, 51)
# Variável com todos os números permitidos na hora da aposta(apenas números entre 1 e 50)


#TODAS AS FUNÇÕES:
def numeros_apostados_ordenados():
    todos_os_numeros_apostados = [numero for aposta in todas_as_apostas for numero in aposta['aposta']]

    contagem_numeros = {}
    for numero in todos_os_numeros_apostados:
        if numero in contagem_numeros:
            contagem_numeros[numero] += 1
        else:
            contagem_numeros[numero] = 1

    numeros_ordenados = sorted(contagem_numeros.items(), key=lambda x: x[1], reverse=True)
    print("Nro apostado   Qtd de apostas")
    for numero, quantidade_apostas in numeros_ordenados:
        print(f"{numero:<14}{quantidade_apostas}")
        pausar(1)
    
#Função que pega todos os números apostados e mostra quantas aparições eles tem nas apostas, ordenado de maneira descrescente.. Pega 
# especificamente a parte de apostas do dicionário todas_as apostas pegando cada número de cada aposta feita. Feito isso, é 
#adicionado a um dicionário novo chamado contagem_números. Se o número já tiver sido adicionado no dicionário, ele aumenta a aparição em 1.
#Se ele não estiver no dicionário ainda, ele adiciona o número ao dicionário com o valor de 1(uma aparição apenas). 
#Por fim, fiz uma variável com um sorted reverse=True(ordem decrescente) pra organizar os itens(chave e valor) do dicionário criado,
#e um lambda(função anonima de uma linha só) pra indicar no key que é a quantidade de vezes que eles aparecem que tem que ser colocado
#em ordem decrescente.


def pausar(tempo):
    sleep(tempo)
    
#Minha idéia aqui era criar uma função pra utilizar o sleep com outro nome, de 
# maneira que fique mais clara a função do comando


def calcular_digitos_verificadores(cpf):
    nove_digitos_cpf = cpf[:9]
    resultados_digito1 = [int(nove_digitos_cpf[i]) * (10 - i) for i in range(len(nove_digitos_cpf))]
    digito_1 = (sum(resultados_digito1) * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos_cpf = nove_digitos_cpf + str(digito_1)
    resultados_digito2 = [int(dez_digitos_cpf[i]) * (11 - i) for i in range(len(dez_digitos_cpf))]
    digito_2 = (sum(resultados_digito2) * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    return f'{nove_digitos_cpf}{digito_1}{digito_2}'

    #Função que calcula os últimos dois digitos do CPF digitado pelo usuário que está tentando se cadastrar afim de verificar se o
#cálculo é valido, checando assim se o cpf é válido ou não.

def validar_cpf(cpf):
    cpf_gerado_pelo_calculo = calcular_digitos_verificadores(cpf)
    return cpf == cpf_gerado_pelo_calculo
# Função que verifica se o cpf digitado pelo usuário é igual ao cpf que foi gerado pelo cálculo.
# Retorna um boolean. Se for igual ao cálculo, ele é válido, então é True. Se não, False.

def gerar_aposta_surpresinha():
    return random.sample(numeros_permitidos, 5)

#Função que gera 5 números aleatórios entre 1 a 50 sem repetição.

def login():
    while True:
        cpf_do_usuario = input('Digite seu CPF: ').strip()
        senha_do_usuario = input('Digite sua senha: ').strip()

        for usuario in usuarios_cadastrados:
            if usuario['cpf'] == cpf_do_usuario and usuario['senha'] == senha_do_usuario:
                print("\nLogin bem-sucedido! Bem-vindo,", usuario['nome'])
                pausar(2)
                return usuario
        print("CPF ou senha incorretos. Tente novamente.")

#Função que efetua o login do usuário. Verifica se o cpf e a senha estão no banco. Se sim, o usuário é logado.
#Se não, aparece uma mensagem de erro pedindo pra tentar novamente.


def obter_nome_completo():
    while True:
        nome = input('Digite seu nome completo: ').strip().title()

        if len(nome.split()) < 2:
            print('Por favor, digite seu nome completo (nome e sobrenome).')
            continue
        
        nome_sem_espacos = nome.replace(" ", "")
        if not nome_sem_espacos.isalpha() or len(nome_sem_espacos) < 3:
            print('O nome deve conter apenas letras e ter no mínimo 3 caracteres.')
            continue
        
        return nome
    
    #Função pra certificar que o usuário digitou um nome válido no cadastro(no mínimo duas palavras, apenas letras e ter 
# no mínimo 3 caracteres)

def obter_cpf():
    while True:
        cpf = input('Digite seu CPF: ').strip()

        if len(cpf) != 11 or not cpf.isdigit():
            print('CPF inválido. O CPF deve conter 11 dígitos numéricos.')
            continue

        if not validar_cpf(cpf):
            print('CPF inválido. Digite novamente.')
            continue

        if any(usuario['cpf'] == cpf for usuario in usuarios_cadastrados):
            print('Este CPF já possui registro. Por favor, digite outro CPF.')
            continue
        return cpf
    
    #Função pra certificar que o usuário digitou um CPF válido no cadastro. Deve conter 11 digitos, apenas números, não pode já estar no banco
#e deve ser um cpf válido.

def obter_senha():
    while True:
        senha = input('Digite sua senha (entre 6 e 16 caracteres): ').strip()
        if len(senha) < 6 or len(senha) > 16:
            print('Senha inválida. A senha deve conter entre 6 e 16 caracteres.')
            continue
        return senha

#Função pra certificar que o usuário digitou uma senha válida no cadastro(deve ter entre 6 e 16 caracteres)

def verificar_admin(usuario_logado):
    try:
       if usuario_logado['admin'] == True:
           return True
    except:
        return False
    
    #Função pra verificar se o usuário que logou no sistema possui uma chave 'admin' com o valor 'True' lá no banco. Se possuir,
#isto significa que o usuário é um administrador, e a função retorna True. 


def cadastrar():
    usuario_novo = {'id': len(usuarios_cadastrados) + 1}
    usuario_novo['nome'] = obter_nome_completo()
    usuario_novo['cpf'] = obter_cpf()
    usuario_novo['senha'] = obter_senha()
    usuarios_cadastrados.append(usuario_novo)
    print('Cadastrado com sucesso! Agora é só logar.')

#Função pra realizar o cadastro do usuário. Ela puxa as outras 3 funções pra validar o nome, cpf e a senha. Se tudo ok, usuário é adicionado
#ao banco.

def registrar_nova_aposta(usuario_logado):
    print('Você selecionou a opção: REGISTRAR NOVA APOSTA')
    pausar(1)
    print("""\nNo nosso sistema de sorteio nós temos dois tipos de aposta.
Existe a aposta tradicional, onde o usuário escolhe 5 números de 1 a 50, mas também temos
a aposta "surpresinha", onde os números são escolhidos de forma aleatória""")
    pausar(3)
    
    while True:  
        opcao_tipo_de_aposta = selecionar_tipo_aposta()

        if opcao_tipo_de_aposta == '0':
            realizar_aposta_tradicional(usuario_logado)
        elif opcao_tipo_de_aposta == '1':
            realizar_aposta_surpresinha(usuario_logado)

        quer_continuar = input("""\n0 - SIM
1 - NÃO
Deseja continuar apostando? """).strip()
        if quer_continuar == '1':
            print('Entendido! Obrigado pela participação.')
            break
        elif quer_continuar != '0':
            print('Opção inválida. Por favor, digite 0 ou 1.')

#Função pra registrar nova aposta. Ela puxa uma função que pede pra ele selecionar o tipo de aposta, e outras 2 
# funções de acordo com qual tipo de aposta o usuário escolher. Também pergunta se o usuário quer continuar apostando 
# após a última aposta feita.

def selecionar_tipo_aposta():
    while True:
        opcao_tipo_de_aposta = input("""
0 - APOSTA TRADICIONAL
1 - APOSTA SURPRESINHA
Digite o número correspondente a aposta desejada: """).strip()

        if opcao_tipo_de_aposta in ('0', '1'):
            return opcao_tipo_de_aposta
        else:
            print('Opção inválida. Por favor, digite 0 ou 1.')

#Função pra selecionar tipo de aposta. Ela apenas verifica qual aposta o usuário quer, se a tradicional ou surpresa.

def realizar_aposta_tradicional(usuario_logado):
    print('\nVocê selecionou a opção: APOSTA TRADICIONAL')
    pausar(1)
    while True:
        mostrar_aposta_atual = []
        for n in range(0, 5):
            while True:
                numero_digitado = input(f'Digite o {n+1}° número: ').strip()
                if not numero_digitado.isdigit():
                    print('Por favor, digite apenas números.')
                    continue
                numero_digitado = int(numero_digitado)
                if numero_digitado not in numeros_permitidos:
                    print('Apenas números entre 1 a 50.')
                elif numero_digitado in mostrar_aposta_atual:
                    print('Você já digitou esse número. Por favor, digite outro.')
                else:
                    mostrar_aposta_atual.append(numero_digitado)
                    break
        print('\nVocê realizou a aposta com os seguintes números:')
        print(*mostrar_aposta_atual)
        pausar(1)
                
        nova_aposta = {'id_apostador': usuario_logado['id'], 'aposta': mostrar_aposta_atual, 'id_aposta': 1000 + len(todas_as_apostas)}
        todas_as_apostas.append(nova_aposta)

        break
#Função criada para caso o usuário queira realizar uma aposta tradicional. Ela tem várias verificações pra evitar apostas inválidas.
#Tem um for in range pra executar 5 vezes(são 5 números diferentes por aposta), verificando se o número digitado já foi digitado na aposta,
#se o usuário digitou apenas números e se o usuário digitou apenas numeros permitidos(numeros de 1 a 50)
#Após, mostra a aposta feita.

def realizar_aposta_surpresinha(usuario_logado):
    print('\nVocê selecionou a opção: "APOSTA SURPRESINHA"')
    print('Gerando os números...')
    pausar(1)
    mostrar_aposta_atual = gerar_aposta_surpresinha()
    print('Nosso sistema gerou a seguinte aposta pra você:')
    print(*mostrar_aposta_atual)

    nova_aposta = {'id_apostador': usuario_logado['id'], 'aposta': mostrar_aposta_atual, 'id_aposta': 1000 + len(todas_as_apostas)}
    todas_as_apostas.append(nova_aposta)

#Função criada para caso o usuário queira realizar a aposta surpresa. Ele gera 5 números entre 1 a 50 sem repetição através da função
#gera_aposta_surpresinha, e mostra os números gerados pro usuário.


def listar_minhas_apostas(usuario_logado):
    print('Você selecionou a opção: LISTAR MINHAS APOSTAS')
    pausar(1)
    tem_aposta = False
    print('\nVerificando apostas...')
    pausar(2)
    for aposta in todas_as_apostas:
        if aposta['id_apostador'] == usuario_logado['id']:
            print(f"Aposta: {aposta['aposta']}, ID: {aposta['id_aposta']}")
            pausar(1)
            tem_aposta = True
    
    if not tem_aposta: 
        print('Você não tem aposta nenhuma registrada!')
        pausar(1)

#Função que lista todas as apostas do usuário logado(mostrando a aposta e o id dela). Caso ele não tenha aposta nenhuma, aparece uma 
# mensagem dizendo que o usuário não possui aposta registrada
    
    
    
def deslogar():
    print("\nDeslogando...")
    print()
    pausar(2)
    menu_inicial()  

#Função simples construida pro usuário ter a possibilidade de deslogar. 

def menu_usuario(usuario_logado):
    while True:
        print("\nMenu:")
        print("1. Registrar nova aposta")
        print("2. Listar todas as minhas apostas")
        print("3. Ver regras da premiação")
        print("4. Deslogar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            registrar_nova_aposta(usuario_logado)
        elif opcao == '2':
            listar_minhas_apostas(usuario_logado)
        elif opcao == '3':
            regras_premiacao()
        elif opcao == '4':
            deslogar()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

#Função que mostra o menu do usuário. É usado pro usuário escolher qual funcionalidade ele quer realizar dentro da loteria.
#Quando ele escolher a opção, vai ser executada a função relacionada a funcionalidade escolhida.

  
def menu_inicial(): 
    print('-'*30)
    print('LOTERIA CODEGAINS')
    print('-'*30)     
    print("""Olá! Seja bem-vindo ao sistema de loteria Codegains.
É um prazer ter você aqui conosco.
Antes de iniciarmos, me conta uma coisa:
0 - Já sou cliente
1 - Sou novo aqui""")
    while True:
        opcao_escolhida = input("Digite a opção desejada: ").strip()
        if opcao_escolhida == '0': 
            print('\nPerfeito! Vamos realizar seu login então.')
            pausar(1)
            usuario_logado = login()
            if usuario_logado:
                if verificar_admin(usuario_logado):
                    menu_admin()
                menu_usuario(usuario_logado)

        elif opcao_escolhida == '1':
            print('\nSeja bem-vindo! Vamos criar uma conta novinha pra você.')
            pausar(1)
            cadastrar()
            usuario_logado = login()
            if usuario_logado:
                menu_usuario(usuario_logado)
        else:
            print('Opção inválida! Digite 0 ou 1.')
            continue

#Função que mostra o menu inicial. É onde o usuário coloca se ele quer se logar ou se cadastrar, e também verifica se o usuário que logou
#é um administrador ou não(pra verificar qual menu é pra ser mostrado, se o menu de admin ou o menu de usuário)
          
def sortear_numeros():
    print('Você selecionou a opção: EXECUTAR O SORTEIO')
    pausar(1)
    while True:
        confirmar_sorteio = input("""\n0 - SIM
1 - NÃO
Para executarmos o sorteio, teremos que finalizar as apostas. Isto não poderá 
ser desfeito. Deseja continuar? """).strip()
        
        if confirmar_sorteio == '1':
            print("\nSorteio cancelado.")
            pausar(1)
            return
        elif confirmar_sorteio == '0':
            quantidade_de_apostas = len(todas_as_apostas)
            if quantidade_de_apostas == 0:
                print('\nImpossível fazer sorteio: 0 apostas registradas.')
                pausar(1)
                print('Voltando ao menu...')
                pausar(1)
                break
            else:
                realizacao_do_sorteio()
                return
        else:
            print("Opção inválida. Por favor, digite 0 ou 1.")

#Função que realiza o sorteio dos números para o administrador. O admin deve confirmar o sorteio. Após a confirmação, é verificado
#se existe alguma aposta registrada. Se existir pelo menos uma, é executada a função realizacao_do_sorteio onde o sorteio de fato acontece.

def ordenar_vencedores_por_nome(apostas_vencedoras):
    info_vencedores = []
    for id_aposta in apostas_vencedoras:
        for aposta in todas_as_apostas:
            if aposta['id_aposta'] == id_aposta:
                id_apostador = aposta['id_apostador']
                for usuario in usuarios_cadastrados:
                    if usuario['id'] == id_apostador:
                        info_vencedores.append((usuario['nome'], aposta['aposta'], id_aposta))
                        break
                break
    return sorted(info_vencedores, key=lambda x: x[0])

#Função que ordena todos os nomes dos vencedores da edição atual. Primeiro, é criado uma lista vazia chamada info_vencedores. Depois, 
#a função pega o set vencedores(é colocado como argumento) criado na funçao realizacao_do_sorteio, pega cada id do set(que são os ids das 
# apostas vencedoras) e  compara esse id com o id de cada aposta do banco.
#Se o id da aposta vencedora for igual ao id da aposta atual que o for está iterando, ele cria uma variável chamada id_apostador
#que armazena o id do vencedor. Após isso, ele itera sobre cada usuário do banco, verifica se o id do apostador vencedor é igual
#ao id do usuário atual que o for está iterando, e, se for, significa que este é um dos vencedores. A informação do apostador vencedor(nome, 
# aposta e ID) é colocada na lista info_vencedores. Depois de coletar os dados de todos os ganhadores do sorteio, a função retorna
#a lista dos vencedores com os nomes ordenados de maneira crescente. Fiz isso usando o lambda(função anonima de uma linha só) junto da key=, 
# onde coloquei um parametro x onde x[0]. Isso significa que estou pegando o index 0 da tupla do vencedor. Ou seja, o sorted vai ser usado
#apenas nos elementos do index 0, que neste caso é o nome. 

def realizacao_do_sorteio():
        print('\nFinalizando apostas...')
        pausar(2)
        print(f'Nesta edição, tivemos um total de {len(todas_as_apostas)} apostas')
        pausar(1.0)
        print('Hora de sortear os números vencedores!')
        pausar(1.0)
        print('Gerando números premiados...')
        pausar(2)
        numeros_premiados = random.sample(range(1, 51), 5)
        print(f'Os números premiados foram esses: {numeros_premiados}')
        pausar(2)
        print('\nIniciando fase de apuração e verificando ganhadores...')
        pausar(2)
        temos_um_vencedor = False
        vencedores = set()
        qt_rodadas_sorteio = 1
        for aposta in todas_as_apostas:       
            if sorted(numeros_premiados) == sorted(aposta['aposta']):
                temos_um_vencedor = True
                vencedores.add(aposta['id_aposta'])
            
        if not temos_um_vencedor:
            for v in range(25):
                novo_numero = random.randint(1, 50)
                while novo_numero in numeros_premiados:
                    novo_numero = random.randint(1, 50)
                numeros_premiados.append(novo_numero)
                qt_rodadas_sorteio += 1
                for aposta in todas_as_apostas:
                    if all(numero in numeros_premiados for numero in aposta['aposta']):         
                        temos_um_vencedor = True
                        vencedores.add(aposta['id_aposta'])
                if temos_um_vencedor:
                    break
                        
        if temos_um_vencedor:
            numero_de_vencedores = len(vencedores)
            print(f'Tivemos um total de {numero_de_vencedores} aposta(s) vencedor(as)!')
            pausar(1)
            print(f'\nEstes foram todos os números sorteados: {numeros_premiados}')
            pausar(1)
            print(f'Isso significa que tivemos {qt_rodadas_sorteio} rodadas neste sorteio!')
            pausar(1)
            vencedores_ordenados = ordenar_vencedores_por_nome(vencedores)
            print('\nVencedores:')
            pausar(1)
            for nome, aposta, id_aposta in vencedores_ordenados:
                print(f"Nome: {nome}, Aposta: {aposta}, ID da Aposta: {id_aposta}")
                pausar(1)
            pausar(2)
            print('\nAbaixo segue a lista de todos os números apostados, junto da quantidade que aparecem: ')
            print()
            pausar(1)
            numeros_apostados_ordenados()
        
        if not temos_um_vencedor:
            numero_de_vencedores = 0
            print("Nenhum vencedor encontrado após as 25 tentativas adicionais.")
            pausar(1)
        
        premiacao(numero_de_vencedores)
    
#Função que efetua de fato o sorteio pro admin. Ela que gera os primeiros números premiados e checa se houve alguma aposta vencedora 
# logo de cara.
#Se não houve, entra dentro de um for de 25 loops que adiciona um número premiado novo a cada iteração e verifica se possui alguma aposta
#que tenha 5 números que estejam dentro dos números premiados. Se acabar os 25 loops e não achar nenhum vencedor, vai informar isso pro admin.
#Se achar, vai mostrar todos os dados de fim de apuração(quantidade de rodadas, quantidade de vencedores, todos os números sorteados,
# os nomes dos vencedores ordenados de maneira crescente junto de sua aposta e o id da aposta, e a lista de todos os números apostados
# junto da quantidade que aparecem no dicionario todas_as_apostas).
#Os ids das apostas vencedoras ficam armazenadas dentro de um set pra ter certeza que não haverá repetições.

def iniciar_nova_edicao():
    print('Você selecionou a opção: INICIAR NOVA EDIÇÃO')
    pausar(1)
    todas_as_apostas.clear()
    print('Todas as apostas foram zeradas! Nova edição iniciada.')
    pausar(1)
    
    #Função simples que o admin utiliza pra iniciar uma nova edição deletando todas as apostas feitas na outra.


def regras_premiacao():
    print('\nNosso sistema de premiação funciona da seguinte forma:')
    pausar(1)
    regras = [
        '1 - O prêmio fixo é de R$10 milhões de reais.',
        '2 - O apostador precisa necessariamente acertar todos os 5 números para ganhar',
        '3 - Caso aconteça de termos mais de um vencedor, o prêmio fixo é dividido pela quantidade de ganhadores',
        '4 - Se não houver vencedor nenhum, o prêmio é acumulado para a próxima edição. '
    ]
    for r in regras:
        print(r)
        pausar(1)
    
    #Função simples pra mostrar pro usuário cada regra da premiação.

def checar_se_premio_acumulou():
    if valor_premio_fixo > 10000000:
            vezes_que_acumulou = (valor_premio_fixo / 10000000) - 1
            print(f'Isto significa que o prêmio havia acumulado {vezes_que_acumulou:.0f} vez(es)')
            pausar(1)
    
    #Função usada pra verificar se o prêmio havia acumulado alguma vez antes de achar o atual vencedor.
    #É mais pra informar pro admin quantas edições da loteria haviam sido terminadas sem encontrar vencedor algum.


def premiacao(numero_de_vencedores):
    global valor_premio_fixo
    print('\nChecando premiação...')
    pausar(1)
    if numero_de_vencedores > 1:
        print('Como tivemos mais de um vencedor, o prêmio será dividido entre todos')
        pausar(1)
        print(f'Levando em conta que tivemos {numero_de_vencedores} vencedores, o prêmio de 10 milhões será dividido.')
        pausar(1)
        premio_dividido = (valor_premio_fixo / numero_de_vencedores)
        print(f'Cada um vai ficar com R${premio_dividido:.2f}')
        checar_se_premio_acumulou()
        valor_premio_fixo = 10000000
    
    elif numero_de_vencedores == 1:
        print('Como tivemos apenas um vencedor, o prêmio será entregue de maneira integral.')
        pausar(1)
        print(f'Nosso único ganhador levará R${valor_premio_fixo:.2f} pra casa.')
        pausar(1)
        checar_se_premio_acumulou()
        valor_premio_fixo = 10000000
    
    else:
        print('Como não tivemos vencedor nesta edição, o prêmio será acumulado para a próxima.')
        pausar(1)
        print(f'Prêmio atual: R${valor_premio_fixo:.2f}')
        pausar(1)
        valor_premio_fixo += 10000000
        print(f'Prêmio da próxima edição: R${valor_premio_fixo:.2f}')
        pausar(1)

    #Função que verifica como será executada a premiação. Se houver exatamente um vencedor, o prêmio será entregue integralmente pra ele.
    #Se houver mais de um, o prêmio será dividido entre todos.
    #Se não achar vencedor nenhum, o prêmio será acumulado. Logo, a variável usada pra registrar o valor atual do prêmio(valor_premio_fixo)
#aumentará em 10 milhões
    #Interessante ressaltar que é nesta função que é feita a verificação de quantas vezes o prêmio acumulou através da 
# função checar_se_premio_acumulou

def menu_admin():
    while True:
        print("\nMENU DE ADMINISTRADOR:")
        print("1. Iniciar nova edição")
        print("2. Listar apostas de todos os usuários")
        print("3. Listar todos os usuários")
        print("4. Finalizar apostas e executar sorteio")
        print("5. Deslogar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            iniciar_nova_edicao()
        elif opcao == '2':
            listar_todas_as_apostas()
        elif opcao == '3':
            listar_todos_os_usuarios() 
        elif opcao == '4':
            sortear_numeros()
        elif opcao == '5':
            deslogar()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    
    #Função que mostra o menu do administrador(se o usuário tiver permissão de admin). É nela que o admin escolhe a funcionalidade
#que ele quer executar. 

def listar_todas_as_apostas():
    print('Você selecionou a opção: LISTAR TODAS AS APOSTAS')
    pausar(1)
    tem_aposta = False
    print('\nVerificando apostas...')
    pausar(2)
    for aposta in todas_as_apostas:
        print(f"Aposta: {aposta['aposta']}, ID: {aposta['id_aposta']}")
        pausar(0.2)
        tem_aposta = True
    
    if not tem_aposta:
        print('Ninguém apostou ainda!')
        pausar(1)
    
    #Função que mostra pro administrador todas as apostas já feitas na edição atual
    #Se não houver nenhuma aposta, mostrará uma mensagem dizendo que ninguém apostou.

def listar_todos_os_usuarios():
    print('Você selecionou a opção: LISTAR TODOS OS USUÁRIOS')
    pausar(1)
    tem_usuario = False
    print('\nVerificando usuários...')
    pausar(2)
    for usuario in usuarios_cadastrados:
        print(f"Nome: {usuario['nome']}, ID: {usuario['id']}, CPF: {usuario['cpf']}")
        pausar(0.2)
        tem_usuario = True
    if not tem_usuario:
        print('Nenhum usuário registrado!')
        pausar(1)
    
    #Função que mostra pro administrador todas as informações pertinentes de todos os usuários já cadastrados(não mostra a senha)]
    #Se não houver nenhum usuário registrado, mostrará uma mensagem dizendo que ninguém apostou.



#Iniciando o programa...
menu_inicial()

        

















  