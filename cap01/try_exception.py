def numDiv (num1, num2):
    resultado = num1 / num2
    print(resultado)

# Execução não gera erro
numDiv(4,2)
# Execução gerando erro
#numDiv(4,0)

# Utilizando try, except e else
try:
    with open('./cap04/arquivos/testandoerros.txt','w') as f:
        f.write('Gravando texto com funcao WITH')
except IOError: # IOError é um erro de entrada e saída
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()

# Utilizando try, except e else
try:
    f = open('./cap04/arquivos/testandoerros','r')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser lido.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()

try:
    f = open('./cap04/arquivos/testandoerros.txt','w')
    f.write('Gravando no arquivo teste de escrita')
except IOError:
    print ("Erro: arquivo não encontrado ou não pode ser salvo.")
else:
    print ("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print ("Comandos no bloco finally são sempre executados!")

# função para ler inteiro v1
def askint():
    try:
        val = int((input("Digite um número: ")))
    except UnboundLocalError:
        print ("Você não digitou um número!")
    finally:
        print ("Obrigado!")
        print (val) 

askint()
# função para ler inteiro v2
def askint():
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            val = int(input("Tente novamente. Digite um número: "))
        finally:
            print ("Obrigado!")
        print (val) 

askint()
# função para ler inteiro v3
def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print ("Você não digitou um número!")
            continue
        else:
            print ("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print (val) 

# Capturando o código do errado gerado
tuple = (1,2,3,4,5)
try:
    tuple.append(6)
    for each in tuple:
        print(each)
except AttributeError as e:
    print('Erro: ', e)
except IOError as e:
    print('Erro de I/O:', e)