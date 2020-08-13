palavras_reservadas = ["while", "do"]
operadores =["<", "=", "+"]
terminador = [";"]
identificadores = ['i', 'j']
numeros = [0,1,2,3,4,5,6,7,8,9]

################################### Entrada ##################################
codigo = ["while i<100 do i = i + j;"]
##############################Variaveis de saida##############################
saida = []
tabela_de_simbolo = []
##############################################################################
def buscaSimbolo(verificador):
    if verificador in tabela_de_simbolo:
        return tabela_de_simbolo.index(verificador) + 1
    else:
        tabela_de_simbolo.append(verificador)
        return tabela_de_simbolo.index(verificador) + 1

def escaner(linha,numLinha):
    verificador = ''
    for i in range(len(linha)):
        if linha[i] == ' ' or linha[i] == ';' or linha[i] in operadores:
            #verifica as palavras reservadas
            if verificador in palavras_reservadas:
                saida.append( {"token":verificador, "identificador":"Palavra reservada", "tamanho": len(verificador),
                "posicao":( numLinha, i-(len(verificador)) )})

            #verifica os operadores
            elif verificador in operadores:
                saida.append( {"token":verificador, "identificador":"Operador", "tamanho": len(verificador),
                "posicao":( numLinha, i-(len(verificador)) )})
            #verifica os identificadores/costante
            elif verificador in identificadores:
                saida.append( {"token":verificador, "identificador":['identificador',buscaSimbolo(verificador)],"tamanho": len(verificador),
                    "posicao":( numLinha, i-(len(verificador)) )})

            else:
                try:
                    verificador = int(verificador)
                    saida.append( {"token":verificador, "identificador":['Constante',buscaSimbolo(verificador)],"tamanho": len(str(verificador)),
                "posicao":( numLinha, i-(len(str(verificador))) )})
                except:
                    if verificador != '':
                        return [400,{'error': 'linha: {}, coluna: {}'.format(numLinha, i-(len(verificador)))}]

            #limpa o verificador
            verificador = ''
        else:
            verificador += linha[i]

        if linha[i] in operadores:
            saida.append( {"token":linha[i], "identificador":"Operador", "tamanho": len(linha[i]),
                "posicao":( numLinha, i )})
    if  linha[-1] == ';':
        saida.append( {"token":linha[-1], "identificador":"Terminador", "tamanho": len(linha[-1]),
                "posicao":( numLinha, i )})
    return [200,{'error':None}]

def main(cod):
    tbSimb = {}
    for i in cod:
        x = escaner(i, codigo.index(i))
        if x[0] == 400:
            return x[1]
    for x in range(len(tabela_de_simbolo)):
        tbSimb[x+1] = tabela_de_simbolo[x]

    return {'Tab_token':saida, 'Tab_simb':tbSimb}

################################inicio da execucao############################
print(main(codigo))