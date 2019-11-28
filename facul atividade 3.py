dados =["zero"] #lista de dados
maior = 0
menor = 999999999999999
media = 0
acidentes = 0
while True:
    choice = input( "Digite 1 para cadastrar, outra tecla para comparar: ")
    if choice == "1" :
            while choice == "1":
                print("Digite o código da cidade")
                cidade = input()
                dados.append(cidade)
                print("Digite o número de veículos de passeio da cidade código:", cidade)
                veiculos = input()
                dados.append(veiculos)
                print("Digite o número de acidentes de trânsito com vitimas na cidade código: ", cidade)
                vitimas = input()
                dados.append(vitimas)
                choice = input("Digite 1 para continuar cadastrando e 2 para finalizar o cadastro ")                

    else:
        
        
        for n in range(int(len(dados)/3)):
            if maior < int(dados[(n*3)-1]):
                maior = int(dados[(n*3)-1])
            if menor > int(dados[(n*3)-1]):
                menor = int(dados[(n*3)-1])            
            media = media + int(dados[(n*3)-2])
            print(float(media))
            if int(dados[(n*3)-1]) < 2000:
                acidentes = acidentes + int(dados[(n*3)-1])
       
        print("Maior indíce de acidentes é ", maior)
        print("Menor indíce de acidentes é ", menor)
        print("Média de veículos nas cidades juntas", media/(n+1))
        print("Média de acidentes nas cidades com menos de 2000 veículos é de ", acidentes/(n+1))
