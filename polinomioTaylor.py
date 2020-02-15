##
# @ Author Caike Minhano Campos
# @File Algoritmo para calular o polinômio de Taylor de ordem 1 
# #

import math;

######################################################################### 
#                                                                       #
#  Declaração da variaves necessárias para implementação do algoritmo   #
#                                                                       # 
#########################################################################


# Variável x que será inputada pelo usuário
x = float(input("Digite o valor da variavel a ser aproximada:\n"));

# Variável que irá receber o valor aproximado de x para base de aproximacação
x0 = int(x);

# Print do valor aproximado de X
print("Valor para X0 = {}" .format(x0));

# Função para calcular a raiz quadrada
def raizQuadrada(x):
    pass;

# Função de F(x)
def calculaFuncaoX(variableX0):
    #print("Raiz de X0 = {}".format(math.sqrt(variableX0)));
    return math.sqrt(variableX0); 

# Função de F'(X)
def calculaDerivadaX(variableX0):
    #print("Deriva de X0 = {}".format((1/(2 * math.sqrt(variableX0)))));
    return float(1/(2 * math.sqrt(variableX0)));

# Função para calcular a reta Tangente de x, T(x)
def calculaRetaTangenteX(variableX0, variableX):
    return float(calculaFuncaoX(variableX0) + (calculaDerivadaX(variableX0) * (variableX-variableX0)));

print("Valor aproximado = {}" .format(float(calculaRetaTangenteX(x0,x))));


