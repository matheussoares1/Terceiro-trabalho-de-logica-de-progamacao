import os
nome = "NÃO ENCONTRADO"
datanasc = "NÃO ENCONTRADO"
cpf = "NÃO ENCONTRADO"
idade = "NÃO ENCONTRADO"
filiado = "NÃO ENCONTRADO"


i = 0
while i != "5":
    print("SISTEMA DE CADASTRO")
    print('-1- Inserir Dados de Pessoa Fisica')
    print('-2- Visualizar Dados')
    print('-3- Deletar Dados')
    print('-4- Atualizar Dados')
    print('-5- Finalizar')
    i = input("Digite o codigo da opção que você deseja: ")
        
    if i == "1":
        variavel = int(input("Digite a quantidade de cadastros gostaria de inserir: "))
        cont = 0
        while cont<variavel:
            print("\n-Inserir dados de Pessoa Fisica - ID", cont)
            nome=input("Nome Completo: ")
            cpf=input("CPF: ")
            datanasc=input("Ano de nasciemento: ")
            idade=input("Idade: ")
            filiado=input("Filiado: ")
            i2 = input("Clique 1 Para Salvar\n Ou 2 Para Refazer\n")
            if i2=="1":
                arqv2 = open('teste.txt', 'a')
                arqv2.write("nome completo: "+nome+"\n")
                arqv2.write("Cpf: " +cpf+"\n")
                arqv2.write("Ano de Nascimento: " +datanasc+"\n")
                arqv2.write("idade: " +idade+"\n")
                arqv2.write("filiado:  " +filiado+"\n")
                arqv2.close()
                cont+=1
            elif i2=="2":
                cont=0
        #i=i-1
    if i == "2":
        if nome == "Não cadastrado" and cpf == "Não cadastrado" and datanasc == "Não cadastrado" and idade == "Não cadastrado" and filiado == "Não cadastrado":
            print("Nenhum dado foi cadastrado")
        else:
            print("\nCONSULTAR CADASTRO")
            print("Nome Completo: ", nome)
            print("CPF: ", cpf)
            print("Ano de Nascimento: ", datanasc)
            print("Idade: ", idade)
            print("Filiado: ", filiado)
            i2 = input("Clique enter para retornar ao INICIO")
    if i == "3":
        print("\nDELETAR DADOS")
        print("1- Nome Completo: ", nome)
        print("2- CPF: ", cpf)
        print("3- Ano De nascimento: ", datanasc)
        print("4- Idade: ", idade)
        print("5- Filiado: ", filiado)
        print("6- Deletar todos os dados")
        i2 = input("Opção: ")
        if i2 == "1":
            nome = "Não cadastrado"
            print("O Nome Digitado Anteriormente Foi Deletado")
        elif i2 == "2":
            cpf = "Não cadastrado"
            print("O CPF Digitado Anteriormente Foi Deletado")
        elif i2 == "3":
            anonascimento = "Não cadastrado"
            print("O Ano de Nascimento Digitado Anteriormente Foi Deletado")
        elif i2 == "4":
            idade = "Não cadastrado"
            print("A Idade Digitada Anteriormente Foi Deletada")
        elif i2 == "5":
            filiado = "Não cadastrado"
            print("O Filiado Digitado Anteriormente Foi Deletado")
        elif i2 == "6":
            nome = "Não cadastrado"
            cpf = "Não cadastrado"
            datanasc = "Não cadastrado"
            idade = "Não cadastrado"
            filiado = "Não cadastrado"
            print("Todos os dados foram deletados!")
        else:
            print("Opção inválida")
    if i =="4":
        if nome == "Não cadastrado" and cpf == "Não cadastrado" and datanasc == "Não cadastrado" and idade == "Não cadastrado" and filiado == "Não cadastrado":
            print("Nenhum dado foi cadastrado")
        else:
            print("\nATUALIZAR DADOS")
            print("1- Nome Completo: ", nome)
            print("2- CPF: ", cpf)
            print("3- Ano de Nascimento: ", datanasc)
            print("4- Idade Atual: ", idade)
            print("5- Filiado: ", filiado)
            print("6- Atualizar dados novamente")
            i2 = input("Opção: ")
            if i2 == "1":
                print("Opção inválida")
                nome.append(input("Nome Completo: "))
                print("\nNome atualizado com sucesso\n\n")
            elif i2 == "2":
                cpf.append(input("cpf: "))
                print("\nCPF atualizado com sucesso\n\n")
            elif i2 == "3":
                datanasc.append( input("anonascimento: "))
                print("\nAno de Nascimento Atualizado com sucesso\n\n")
            elif i2 == "4":
                idade.append(input("idade: "))
                print("\nIdade atualizadA com sucesso\n\n")
            elif i2 == "5":
                filiado.append(input("filiado: "))
                print("\nFiliado atualizado com sucesso\n\n")
            elif i2 == "6":
                nome.append(input("Nome Completo: "))
                cpf.append(input("CPF: "))
                datanasc.append(input("Ano de Nascimento: "))
                idade.append(input("Idade: "))
                filiado.append(input("Filiado: "))
                print("\nDados de Pessoa Fisica Atualizados com Sucesso!\n\n")
            else:
                print("Opção inválida")
    if i =="5":
       print("Processo Encerrado")
       #NÃO CONSEGUIMOS IMPLEMENTAR A ESCOLHA DE CONFIRMAÇÃO
       
arqv2.write()

arqv2.append(nome)
arqv2.append(cpf)
arqv2.append(datanasc) 
arqv2.append(idade) 
arqv2.append(filiado)  


arqv2.close()