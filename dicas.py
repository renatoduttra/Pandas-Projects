from ctypes.wintypes import PINT
from typing import Final
from matplotlib.pyplot import show
import pandas as pd
#openpyxl

venda = {'data' :['15/02/2021','16/02/2021'],
         'valor':[500, 300],
         'produto':['feijao','arroz'],
         'qtd':[50, 70]
        }

venda_df = pd.DataFrame(venda)
#print(venda_df)
#display(venda_df)

vendas_df = pd.read_excel("Vendas.xlsx")
#print(vendas_df.head(10))#exibe uma certa qtd de resultados
#print(vendas_df.shape)#resumo basico
#print(vendas_df.describe)#resumo aprimorado

#produtos = vendas_df['Produto']
produtos = vendas_df[['Produto', 'ID Loja']]#tabela com alguns atributos
#print(produtos)

#print(vendas_df.loc[1:5])#pega as linhas de df
vendas_nort = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping',["ID Loja", "Produto", "Quantidade"]]#filtrando por consição
#print(vendas_nort)

#print(vendas_df.loc[1,'Produto'])

vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05
#print(vendas_df)

vendas_df['Imposto'] = 0
#print(vendas_df)

vendas_dez_df = pd.read_excel("Vendas - Dez.xlsx")
#print(vendas_dez_df) 

vendas_df = vendas_df.append(vendas_dez_df)#anexar nova tabela
#print(vendas_df)

#vendas_df = vendas_df.drop("Imposto", axis=1)#apagar linha ou coluna

#vendas_df = vendas_df.dropna(how='all', axis=1)#exclui valores vazios 

#vendas_df = vendas_df.dropna()#exclui qualquer linha ou coluna se tiver um valor vazio

#vendas_df['Comissao'] = vendas_df['Comissao'].fillna(vendas_df['Comissao'].mean())#preenche valores vazios com o valor do fill

#vendas_df = vendas_df.ffill()#preencher com o ultimo valor

qtd_transacoes = vendas_df['ID Loja'].value_counts() # qtd de transacoes
#print(qtd_transacoes)

faturamento = vendas_df[['Produto','Valor Final']].groupby('Produto').sum() # agrupar
#print(faturamento)

gerentes_df = pd.read_excel('Gerentes.xlsx')
#print(gerentes_df)

vendas_df = vendas_df.merge(gerentes_df)#unir com novos dados de outras tabelas
#print(vendas_df)

#dicas de para abrir e salval aquivo XLSX
#pd.read_excel('Pasta1.xlsx', sheet_name='Planilha1', header=None, names=['col1', 'col2', 'col3'], index_col=None, usecols=['col1','col2', 'col3’])
#df.to_excel('teste.xlsx', sheet_name='Teste', na_rep='#N/A', header=True, index=False)