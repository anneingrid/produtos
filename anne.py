produtos=open('produtos.txt','+r')
def trataArquivo(arq):
    conteudo=arq.read().splitlines()
    nova=[]
    for linha in conteudo:
        if ';' in linha:
            linha=linha.replace(';','')
        nova.append(linha.split('-'))
    return(nova)



def maiorValor(arq):
    lista=trataArquivo(arq)
    maior=0
    for item in lista:
        item[1]=float(item[1].replace(',','.'))        
        if item[1]>maior:
            maior=item[1]
    return(maior)
        
def menorValor(arq):
    lista=trataArquivo(arq)
    menor=1000
    for item in lista:
        item[1]=float(item[1].replace(',','.'))        
        if item[1]<menor:
            menor=item[1]
    return(menor)


def somaTotal(arq):
    lista=trataArquivo(arq)
    soma=0
    for item in lista:
        item[1]=float(item[1].replace(',','.'))        
        soma+=item[1]
    return(soma)

opcao = 0
while opcao!=4:
    if opcao == 1:
       print("O produto de maior valor ", maiorValor(produtos))
    elif opcao == 2:
        print("O produto de menor valor ", menorValor(produtos))
    elif opcao == 3:
      print("valor total dos produtos ", somaTotal(produtos))
    opcao = int(input("\n Escolha a opção desejada:"\
              "\n1. Encontrar o maior valor."\
              "\n2. Encontrar o menor valor."\
              "\n3. Total"\
              "\n4. Sair\n"))

    arq.close()
