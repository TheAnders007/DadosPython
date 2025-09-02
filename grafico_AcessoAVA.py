import pandas as pd #Importação da biblioteca Pandas
import matplotlib.pyplot as plt #Importação do módulo pyplot da biblioteca Matplotlib

df = pd.read_excel('planilha.xlsx') #Leitura das informações da planilha utilizando o Pandas e armazenando numa variável/DataFrame
df_acessoAVA = df.loc[:90, 'ENTROU NO AVA?'] #Criação de novo DataFrame que refere-se aos 91 primeiros dados da coluna 'ENTROU NO AVA?'

df_acessoAVA = df_acessoAVA.map({1: 'Sim', 0:'Não'}) #Transformação dos valores 1 e 0 em Sim e Não, respectivamente

contAVA = df_acessoAVA.value_counts() #Contagem dos valores do DataFrame

plt.figure(figsize=(6, 4)) #Criação de figura para o gráfico com dimensão de 6 polegadas por 4 polegadas
plt.bar(contAVA.index, contAVA.values, color=['green', 'red']) #Definição de características do gráfico: barras, valores do eixo X, altura e cores
plt.yticks(range(0, max(contAVA.values) + 10, 5)) #Define os valores mínimo e máximo e divisão do eixo Y

plt.title("Contagem de estudantes que acessaram o AVA") #Título do gráfico
plt.xlabel("Acessou o AVA?") #Label sobre eixo X
plt.ylabel("Número de Estudantes") #Label sobre eixo Y

plt.show() #Mostra o Gráfico
