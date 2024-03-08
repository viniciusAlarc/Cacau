import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from time import sleep

nltk.download('punkt')
nltk.download('stopwords')

instalacao = 'Ok! Um chamado está sendo aberto para: Solicitar Instalação/Desinstalação de Software ou Aplicativo'
erro = 'Ok! Um chamado está sendo aberto para: Solicitar Reparo no Aplicativo, Software ou Sistema Operacional Lento ou Indisponível'
pasta = 'Ok! Um chamado está sendo aberto para: Solicitar Acesso a Pasta de Arquivos'
email = 'Ok! Um chamado está sendo aberto para: Solicitar Configuração da Conta de E-mail Vinculada a Conta Corporativa'
remanejamento = "Ok! Um chamado está sendo aberto para: Solicitar Remanejar Computador"
lentidao = 'Ok! Um chamado está sendo aberto para: Solicitar Suporte em Estação de Trabalho Apresentando Lentidão ou Indisponibilidade'
offiline = 'Ok! Um chamado está sendo aberto para: Comunicar falha na conexão'
atualizacao = 'Ok! Um chamado está sendo aberto para: Solicitar Atualização de Software, Aplicativo ou Sistema Operacional'
perifericos = 'Ok! Um chamado está sendo aberto para: Instalar Periféricos'
formatacao = 'Ok! Um chamado está sendo aberto para: Solicitar Formatação de Estação de Trabalho'

atividades = {
    # INSTALAÇÃO
    'instalação': instalacao,
    'instalar': instalacao,
    'download': instalacao,
    'baixar': instalacao,
    'deinstalar': instalacao,

    # ERRO
    'erro': erro,
    'falha': erro,

    # PASTA
    'pasta': pasta,
    'drive': pasta,
    'diretório': pasta,
    'diretorio': pasta,

    # EMAIL
    'email': email,
    'E-mail': email,

    # REMANEJAMENTO
    'remanejar': remanejamento,
    'remanejamento': remanejamento,

    # LENTIDÃO
    'lentidão': lentidao,
    'lentidao': lentidao,
    'lento': lentidao,
    'lenta': lentidao,

    # INTERNET
    'internet': offiline,
    'rede': offiline,

    # PERIFÉRICOS
    'mouse': perifericos,
    'teclado': perifericos,
    'fone': perifericos,
    'webcam': perifericos,
    'camera': perifericos,
    'monitor': perifericos,

    # FORMATAÇÃO
    'formatação': formatacao,
    'formataçao': formatacao,
    'formatar': formatacao,
}

def categorizar_problema(mensagem):
    palavras = word_tokenize(mensagem.lower(), language='portuguese')
    stop_words = set(stopwords.words('portuguese'))
    palavras = [word for word in palavras if word.isalnum() and word not in stop_words]
    for palavra in palavras:
        if palavra in atividades:
            return atividades[palavra]
    return 'Não foi possível categorizar o problema. Por favor, forneça mais informações.'

sleep(1)
mensagem_usuario = input('\nDescreva o problema que está enfrentando: ')
resposta_bot = categorizar_problema(mensagem_usuario)
print(resposta_bot)