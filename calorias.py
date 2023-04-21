frutas = ['banana', 50, 'potassio', 'goiaba', 59, 'fibras']

def procurar(nomeDaFruta):
        for i in range(len(frutas)):
            if frutas[i] == nomeDaFruta:
                print("Nome: " + str(frutas[i]))
                i = i + 1
                print("Calorias/100g: " + str(frutas[i]))
                i = i + 1
                print("Principal nutriente: " + str(frutas[i]))
                return True

def percorrer():
        print(frutas)
                
def cadastrar(nome, calorias, nutriente):
        frutas.append(nome)
        frutas.append(calorias)
        frutas.append(nutriente)
        percorrer()
        
while True:
    nomeDaFruta = str(input('Pesquisar fruta: '))          
    if procurar(nomeDaFruta) != True:
        calorias = int(input('Digite a quantidade de calorias a cada 100g: '))
        nutriente = str(input('Qual principal nutriente? '))
        cadastrar(nomeDaFruta, calorias, nutriente)



 















      
""""
elif frutas[i] != name:
            cadastro = str(input('Deseja cadastrar?  '))
            frutas.append(cadastro)
            calorias = int(input('Quantas calorias ha em 100g?  '))
            frutas.append(calorias)
            nutriente = str(input('Digite o principal nutriente da ' + cadastro))
            frutas.append(nutriente)
            print(cadastro)
            print(calorias)
            print(nutriente)
            break
"""