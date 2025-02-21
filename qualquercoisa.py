
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
    

if __name__ == '__main__':
    # calculodetriangulo()
    # exibir_itens()
    cooltriangle()
    

    
