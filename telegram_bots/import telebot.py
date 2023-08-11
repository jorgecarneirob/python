#user and bot
#jorgecarneiro
#JorgeCarneiroBot

import telebot
CHAVE_API = "6395897725:AAG8xxkWWJkR_7zsl6stHjfCPN3RP-qbhsY"

#registra chave API
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizzaria"])
def cliente(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id,"""MENU:
    /americana - massa de pizza, molho de tomate, queijo muçarela, presunto, orégano.
    
    /calabresa - massa de pizza, molho de tomate, queijo muçarela, calabresa, orégano.
    
    /mussarela - massa de pizza, molho de tomate, queijo mussarela, orégano
    
    /portuguesa - massa de pizza, molho de tomate, queijo mussarela, presunto, orégano, ovo, linguiça, batata frita, azeitonas, cebola e pimentão.
    """)


@bot.message_handler(commands=["americana"])
def americana(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Quantas pizzas america?
    /UMA unidade
    /DUAS unidades
    /TRES unidades
    /QUATRO unidades
    /CINCO unidades
    /+""")
    
@bot.message_handler(commands=["calabresa"])
def calabresa(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Quantas pizzas calabresa?
    /UMA unidade
    /DUAS unidades
    /TRES unidades
    /QUATRO unidades
    /CINCO unidades
    /+""")
    
@bot.message_handler(commands=["mussarela"])
def mussarela(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Quantas pizzas mussarela?
    /UMA unidade
    /DUAS unidades
    /TRES unidades
    /QUATRO unidades
    /CINCO unidades
    /+""")
    
@bot.message_handler(commands=["portuguesa"])
def portuguesa(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Quantas pizzas portuguesa?
    /UMA unidade
    /DUAS unidades
    /TRES unidades
    /QUATRO unidades
    /CINCO unidades
    /+""")
    

@bot.message_handler(commands=["UMA"])
def UMA(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """1 pizza adicionada ao carrinho.
    Qual a forma de pagamento?
    /dinheiro
    /credito
    /debito
    /pix
    /outros""")
    
@bot.message_handler(commands=["DUAS"])
def DUAS(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """2 pizza adicionada ao carrinho.
    Qual a forma de pagamento?
    /dinheiro
    /credito
    /debito
    /pix
    /outros""")

@bot.message_handler(commands=["TRES"])
def TRES(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """3 pizza adicionada ao carrinho.
    Qual a forma de pagamento?
    /dinheiro
    /credito
    /debito
    /pix
    /outros""")

@bot.message_handler(commands=["QUATRO"])
def QUATRO(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """4 pizza adicionada ao carrinho.
    Qual a forma de pagamento?
    /dinheiro
    /credito
    /debito
    /pix
    /outros""")

@bot.message_handler(commands=["CINCO"])
def CINCO(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """5 pizza adicionada ao carrinho.
    Qual a forma de pagamento?
    /dinheiro
    /credito
    /debito
    /pix
    /outros""")
    
@bot.message_handler(commands=["dinheiro"])
def dinheiro(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Informe o endereço para entrega:""")        

@bot.message_handler(commands=["credito"])
def credito(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Informe o endereço para entrega:""")
    
@bot.message_handler(commands=["debito"])
def debito(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Informe o endereço para entrega:""")
    
@bot.message_handler(commands=["pix"])
def pix(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, """Informe o endereço para entrega:""")

@bot.message_handler(commands=["lanchonete"])
def orcamento(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Me informe os sintomas e/ou problema")

@bot.message_handler(commands=["agendamento"])
def reclamacao(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, "Para reclamações enviar e-mail para jorgecarneiroconsultoria@gmail.com")
   
def verificar(mensagem):
#    if mensagem.text = "Coe":
        return True
#    else
#        return False

@bot.message_handler(func=verificar)
def responder(mensagem):
    bot.reply_to(mensagem, """Jorge Carneiro Consultorias em T.I
    Este chatbot é para demonstração de possiveis utilidades para sua empresa
    Seja bem vindo!.
    /pizzaria: Tem uma pizzaria?
    /lanchonete: Tem uma lanchonete?
    /agendamento: Seus cliente agendam horário?""")


#mantém o bot em loop
bot.polling()