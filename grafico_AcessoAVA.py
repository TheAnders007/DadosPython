import pandas as pd #Importação da biblioteca Pandas
import matplotlib.pyplot as plt #Importação do módulo pyplot da biblioteca Matplotlib

df = pd.read_excel('planilha.xlsx') #Leitura das informações da planilha utilizando o Pandas e armazenando numa variável/DataFrame
df_acessoAVA = df.loc[df['GRUPO'] == '1', ['DESISTIU?', 'ENTROU NO AVA?']] #Recorte das informações das colunas 'DESISTIU' e 'ENTROU NO AVA?' onde o grupo seja igual a 1

#Transformação dos valores 1 e 0 em Sim e Não, respectivamente
df_acessoAVA['DESISTIU?'] = df_acessoAVA['DESISTIU?'].map({1: 'Sim', 0:'Não'})
df_acessoAVA['ENTROU NO AVA?'] = df_acessoAVA['ENTROU NO AVA?'].map({1: 'Sim', 0: 'Não'})

#Contagem dos valores do DataFrame
contDes = df_acessoAVA['DESISTIU?'].value_counts()
contAVA = df_acessoAVA['ENTROU NO AVA?'].value_counts()

plt.figure(figsize=(6, 4)) #Criação de figura para o gráfico com dimensão de 6 polegadas por 4 polegadas
plt.bar(['Acessou', 'Ainda Não Acessou', 'Desistentes'], [contAVA.get('Sim', 0), contAVA.get('Não', 0), contDes.get('Sim', 0)], color=['green', 'red', 'black']) #Definição de características do gráfico: barras, valores do eixo X, altura e cores
plt.yticks(range(0, max([contAVA.get('Sim', 0), contAVA.get('Não', 0)]) + 10, 5)) #Define os valores mínimo e máximo e divisão do eixo Y

plt.title("Contagem de estudantes que acessaram o AVA") #Título do gráfico
plt.xlabel("Acessou o AVA?") #Label sobre eixo X
plt.ylabel("Número de Estudantes") #Label sobre eixo Y

plt.show() #Mostra o Gráfico
