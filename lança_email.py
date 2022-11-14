import argparse
import smtplib
import ssl

context = ssl.create_default_context()
running = True

parse = argparse.ArgumentParser(description="Enviador de E-mails")
parse.add_argument(
    "-g", "--gmail", metavar="", type=str, help="Insira o seu Gmail")
parse.add_argument(
    "-p", "--password", metavar="", type=str, help="\
        Digite a senha do seu Gmail")
parse.add_argument("-r", "--receiver", metavar="", type=str, help="\
    Digite o Gmail do recebedor da sua mensagem")

args = parse.parse_args()

seu_gmail = args.gmail
senha_args = args.password
recebedor_args = args.receiver


class respostas():
    confirm = ["Sim", "sim", "s", "S", "SIM"]
    negar = ["Não", "não", "n", "N", "Nao", "nao", "NÃO", "NAO"]


ponte = respostas()


def enviar_email_com_argumentos(email, senha, recebedor, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as servidor:
        print("--- Enviando E-mail... ---")
        try:
            servidor.login(email, senha)
            servidor.sendmail(from_addr=email, to_addrs=recebedor, msg=msg)
            print("--- E-mail enviado! ---")
            servidor.quit()

        except smtplib.SMTPAuthenticationError:
            print("---" * 30)
            print("Usuário ou Senha não foram aceitos. Tente novamente.")
            print()
            print("""Ou A sua conta no google precisa de uma senha de
aplicativos para ser utilizada através de outros dispositivos.
Acesse: https://support.google.com/mail/?p=BadCredentials para saber mais""")
            print("---" * 30)
        except Exception as e:
            print("---" * 30)
            print("Erro. Tente novamente")
            print("NOME DO ERRO=", e.__doc__)


def enviar_email(email, senha, recebedor, msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as servidor:
        print("--- Enviando E-mail... ---")
        try:
            servidor.login(email, senha)
            servidor.sendmail(from_addr=email, to_addrs=recebedor, msg=msg)
            print("--- E-mail enviado! ---")
            servidor.quit()

        except smtplib.SMTPAuthenticationError:
            print("---" * 30)
            print("Usuário ou Senha não foram aceitos. Tente novamente.")
            print()
            print("""Ou A sua conta no google precisa de uma senha de
aplicativos para ser utilizada através de outros dispositivos.
Acesse: https://support.google.com/mail/?p=BadCredentials para saber mais""")
            print("---" * 30)
        except Exception as e:
            print("---" * 30)
            print("Erro. Tente novamente")
            print("NOME DO ERRO=", e.__doc__)


if seu_gmail is None and senha_args is None and recebedor_args is None:
    print("""
    ||**************************************||
    ||**************************************||
    ||     ENVIADOR DE E-MAILS (GMAIL)      ||
    ||**************************************||
    ||**************************************||
    """)

    print("---" * 30)

    print("RESPOSTAS: SIM / NÃO")
    iniciar = input("Enviar um E-mail?: ")
    print("---" * 30)

    if iniciar in ponte.confirm:
        while running is True:
            Email = input("""Digite o seu Gmail
            Exemplo = user@gmail.com: """)
            if "@Gmail.com" in Email:
                pass
            else:
                while "@gmail.com" not in Email:
                    if "@Gmail.com" in Email:
                        break
                    else:
                        print("E-mail inválido. Apenas use o gmail")
                        Email = input("Digite o seu Gmail: ")

            Senha = input("Insira a Senha: ")
            print("---" * 30)
            Alvo = input("Enviar para?: ")
            print("---" * 30)
            print()

            print("AVISO: tente não inserir combinações de caracteres para \
        formular expressões ")
            print("Como por exemplo :) ou :(")
            print()
            mensagem = input("MENSAGEM: ")

            enviar_email(Email, Senha, Alvo, mensagem.encode())
            desligar = input("Deseja desligar?: ")
            if desligar in ponte.confirm:
                print("---" * 30)
                print("Desligando...")
                running = False
            elif desligar in ponte.negar:
                iniciar = input("Enviar um E-mail?: ")
                if iniciar in ponte.confirm:
                    continue
            else:
                print("Opção inválida. Reiniciando...")
                print("---" * 30)
                iniciar = input("Enviar um E-mail?: ")
                if iniciar in ponte.confirm:
                    continue
                else:
                    print("Desligando...")
                    running = False
    elif iniciar in ponte.negar:
        print("Desligando...")
    else:
        print("Inválido!")
        print("Desligando...")
else:
    if "@Gmail.com" in seu_gmail:
        pass
    else:
        while "@gmail.com" not in seu_gmail:
            if "@Gmail.com" in seu_gmail:
                break
            else:
                print("E-mail inválido. Apenas use o gmail")
                seu_gmail = input("Digite o seu Gmail: ")
    print("---" * 30)
    print("AVISO: tente não inserir combinações de caracteres para \
formular expressões ")
    print("Como por exemplo :) ou :(")
    print()
    msgarg = input("MENSAGEM: ")
    enviar_email_com_argumentos(
        seu_gmail, senha_args, recebedor_args, msgarg.encode())
