#Juros compostos são uma boa forma de alavancar os investimentos. E para saber qual sera o montante final, temos que saber:

#1.   O capital investido (C)
#2.   A taxa juros, que é porcentagem cobrada em cima do capital, usaremos a taxa ao ano (i)
#3. O tempo, em meses, que o capital ficará aplicado (t)
#4. Os Juros do rendimento (J), calculado pela subtração do valor final do capital investido
#5. Montante final após o termino do investimento: M = C\*(1+i)^t


from math import pow

def composto(capital, juros, tempo):
    return capital * pow((1+juros), tempo)

def simples(capital, juros, tempo):
    return capital * juros * tempo

capital = float(input('Qual o capital de investimento? '))
juros = float(input('Qual o juros anual em porcentagem? (%) '))
tempo = int(input('Quantos meses terá o investimento? '))

juros = juros / 100
tempo = tempo / 12

valor_final_composto = composto (capital, juros, tempo)
print(f'O montante final será de: {valor_final_composto:.02f} R$')
print(f'Os Juros do rendimento foram de: {(valor_final_composto - capital):.02f} R$')


#Função para o cálculo do Juros simples.

# valor_final_simples = simples(capital, juros, tempo)
# print(f'O montante final será de: {(valor_final_simples + capital):.02f} R$')