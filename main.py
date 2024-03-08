import spacy
from fuzzywuzzy import fuzz

instalacao = 'Ok! Um chamado está sendo aberto para: Solicitar Instalação/Desinstalação de Software ou Aplicativo'
erro = 'Ok! Um chamado está sendo aberto para: Solicitar Reparo no Aplicativo, Software ou Sistema Operacional Lento ou Indisponível'
pasta = 'Ok! Um chamado está sendo aberto para: Solicitar Acesso a Pasta de Arquivos'
email = 'Ok! Um chamado está sendo aberto para: Solicitar Configuração da Conta de E-mail Vinculada a Conta Corporativa'
remanejamento = "Ok! Um chamado está sendo aberto para: Solicitar Remanejar Computador"
lentidao = 'Ok! Um chamado está sendo aberto para: Solicitar Suporte em Estação de Trabalho Apresentando Lentidão ou Indisponibilidade'
offiline = 'Ok! Um chamado está sendo aberto para: Comunicar falha na conexão'

def abrir_chamado(mensagem):

    nlp = spacy.load("pt_core_news_sm")

    dicionario = {
        'instalação': instalacao,
        'instalar': instalacao,
        'download': instalacao,
        'baixar': instalacao,
        'deinstalar': instalacao,
        'erro': erro,
        'pasta': pasta,
        'email': email,
        'remanejar': remanejamento,
        'lentidão': lentidao,
        'internet': offiline,
    }

    doc = nlp(mensagem.lower())

    resposta = None

    for chave, valor in dicionario.items():
        for token in doc:
            if fuzz.partial_ratio(token.text, chave) >= 90:
                resposta = valor
                break

    if resposta:
        return resposta
    else:
        print('Desculpe, não consegui identificar a necessidade. Por favor, tente explicar de outra forma.')
        inicial()

def inicial():
    mensagem_do_usuario = input('Usuário: ')
    resposta_do_bot = abrir_chamado(mensagem_do_usuario)
    print('Cacau:', resposta_do_bot)
    global sim_ou_nao
    sim_ou_nao = input('Essa categoaria está certa? Digite "s" para sim e "n" para não\n')

def confirmacao():
    if sim_ou_nao == 's' or sim_ou_nao == 'S':
        print('Chamado aberto, número 000000')
    elif sim_ou_nao == 'n' or sim_ou_nao == 'N':
        print('Voltando ao início')
        inicial()
    else:
        print('Opção inválida.')
        confirmacao()

inicial()
confirmacao()