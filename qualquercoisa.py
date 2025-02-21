
def exibir_itens(listao):
    list = ["iphone", "ipad", "airpod"]
    list2 = ["macbook","apple watch"]
    listao = list + list2

    for item in listao:
        if len(item) > 4:
            print(item)

    print(listao)

def calculodetriangulo():
    alt = float(input("me dê a altura\n>>"))
    base = float(input("me dê a altura\n>>"))
    print("Area do triangulo:{:.2f}".format((alt*base)/2))

def cooltriangle():
    n = int(input("quantidade de rows:\n>>"))
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end ="")
        for j in range(i+1):
            print("*",end =" ")
        print()

def tronco_piramide():
    base_maior = float(input("Base maior:\n>>"))
    altura_maior = float(input("Altura maior\n>>:"))
    base_menor = float(input("Base menor\n>>"))
    altura_menor =float(input("Altura menor\n>>"))
    pira_menor = (base_menor*altura_menor)/3
    pira_maior = (base_maior*altura_maior)/3
    tronco = pira_maior - pira_menor
    if tronco < 0:
        print("Erro valor invalido")
    else:
        print("Tronco da piramide é igual a :", tronco)
    

if __name__ == '__main__':
    # calculodetriangulo()
    # exibir_itens()
    # cooltriangle()
    tronco_piramide()

    
