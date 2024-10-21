----LOTERIA CODEGAINS - OBJETIVO PRINCIPAL----

Este é um sistema de loteria desenvolvido em Python chamado Loteria Codegains. 
Ele permite que os usuários façam apostas em números e concorram a um prêmio em dinheiro. 
Segue abaixo uma explicação detalhada de como o sistema funciona e como utilizar:

----FUNCIONALIDADES PRINCIPAIS----

Cadastro de usuários:
Novos usuários podem se cadastrar fornecendo informações como nome completo, CPF e senha.
O sistema verifica se o CPF é válido e garante que não haja duplicação de CPFs cadastrados.

Login de usuários:
Usuários cadastrados podem fazer login com seu CPF e sua senha.

Registro de apostas:
Os usuários podem registrar novas apostas, escolhendo entre uma aposta tradicional(onde o usuário 
seleciona manualmente 5 números) ou uma aposta surpresinha(onde o sistema gera automaticamente 5 
números aleatórios entre 1 e 50). As apostas são armazenadas em um banco de dados(tempo de execução) 
juntamente com o ID do usuário que fez a aposta.

Sorteio e premiação:
O sistema permite que o administrador realize o sorteio pra verificar os vencedores.
Após o sorteio, os números premiados são exibidos e o sistema verifica se há vencedores.
Caso haja vencedores, o prêmio é distribuído igualmente entre eles. Se não houver vencedores, o 
prêmio acumula para a próxima edição.

Administração do sistema:
Um administrador pode listar todas as apostas feitas por todos os usuários, bem como todos os usuários 
cadastrados.
O mesmo consegue iniciar uma edição nova zerando todas as apostas feitas para que não haja conflito
com apostas de edições anteriores.

----ALGUMAS FUNÇÕES----

Cadastro e login de usuários: 
Funções para cadastro e login de novos usuários, verificando se o CPf é válido e se
o mesmo já existe no banco.

Registro de apostas: 
Funções para permitir que os usuários registrem novas apostas, escolhendo entre 
aposta tradicional e surpresinha.

Sorteio e premiação: 
Funções para realizar o sorteio, verificar os vencedores e distribuir os prêmios 
de acordo com as regras estabelecidas.

----REGRAS DA PREMIAÇÃO----

Ao término de cada edição da Loteria Codegains, as seguintes regras se aplicam à distribuição do prêmio:

Acúmulo do prêmio: Caso não haja nenhum vencedor na edição atual, o prêmio de R$10 milhões é 
acumulado para a próxima edição, aumentando assim o valor total do prêmio.

Divisão entre vencedores: Se houver mais de um ganhador na edição, o prêmio será dividido 
igualmente entre todos os vencedores participantes.

Prêmio para único ganhador: No caso de apenas uma aposta ser vencedora, o prêmio será entregue 
integralmente ao único ganhador, sem divisão.

----UTILIZAÇÃO DO SISTEMA----

Para utilizar o sistema, basta seguir as instruções apresentadas no console após executar o código. 
O sistema guiará o usuário por todas as etapas, desde o cadastro e login até o registro de apostas e
participação nos sorteios.
Este sistema foi feito pra ser usado pelo próprio console, por isso a interface é bem autoexplicativa e
completa.