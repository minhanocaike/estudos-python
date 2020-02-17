##
#
# @ Author Caike Minhano Campos
# @ File Algoritmo para calular o polinômio de Taylor de ordem 1 para funções do tipo raiz quadrada de x
# Para valores próximos de x no intervalo -----------
#
##

######################################################################### 
#                                                                       #
#  Declaração da variáveis necessárias para implementação do algoritmo  #
#                                                                       # 
#########################################################################

# Variável x que será inputada pelo usuário
x = float(input("Digite o valor da variavel a ser aproximada:\n"))

# Variável que irá receber o valor aproximado de x para base de aproximacação
x0 = int(x)

# Print do valor aproximado de X
print("Valor para X0 = {}".format(x0))

######################################################################### 
#                                                                       #
#          Funções para calcular a f(x), f'(x) e T(x) onde:             #    
#                                                                       #
#                         f'(x) é a derivada;                           #
#       T(x) é a função que descreve a reta tangente ao ponto X0        #
#                                                                       # 
#########################################################################

# Função para calcular a raiz quadrada, melhoria para eliminar o modulo math e otimizar o codigo
def raizQuadrada(variableX):
    for i in range(int(x/2),0,-1):
        if((variableX/i) == i):
            return i

# Atribui o valor da raiz de X0 à variável raiz
raiz = raizQuadrada(x0)

# Função de F(x)
def calculaFuncaoX():
    #print("Raiz de X0 = {}".format(math.sqrt(variableX0)));
    return raiz

# Função de F'(X)
def calculaDerivadaX():
    #print("Deriva de X0 = {}".format((1/(2 * math.sqrt(variableX0)))));
    return float(1/(2 * raiz))

##
# Função para calcular a reta Tangente de x, T(x)
# Polinomio com o seguinte modelo T(x) = f(x) + f'(x)*(X-X0)
##
def calculaRetaTangenteX(variableX0, variableX):
    return float(calculaFuncaoX() + (calculaDerivadaX() * (variableX-variableX0)))


# Atribui o valor de retorno da função da reta tangente e imprimi na tela
resultAproximacao = float(calculaRetaTangenteX(x0,x))
print("Valor aproximado = {}" .format(resultAproximacao))

######################################################################### 
#                                                                       #
#          Cálculo da estimativa de erro E(x) = f(x) - T(x)             #    
#                                                                       #
#                 f(x) é a função que define a curva;                   #
#       T(x) é a função que descreve a reta tangente ao ponto X0        #
#                                                                       # 
#########################################################################

##
# Função para calcular o quadrado da da diferença dos dois pontos
##
def estimativaErro(variableX0,variableX): #TODO
    return 0

# Atribui o valor de retorno da função de calculo da estimativa de erro e imprimi na tela
resultEstimativaErro = estimativaErro(x0,x) #TODO
print("Valor aproximado = {}" .format(resultEstimativaErro)) #TODO

