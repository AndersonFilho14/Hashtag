import pandas as pd
import pathlib
#Armazenando dados
email = pd.read_excel(r'C:\Users\anderson.filho\Downloads\Projeto AutomacaoIndicadores\Bases de Dados\Emails.xlsx')
lojas = pd.read_csv(r'C:\Users\anderson.filho\Downloads\Projeto AutomacaoIndicadores\Bases de Dados\Lojas.csv', encoding='ISO-8859-1', sep=';')
vendas = pd.read_excel(r'C:\Users\anderson.filho\Downloads\Projeto AutomacaoIndicadores\Bases de Dados\Vendas.xlsx')

#Colocando a coluna 'ID Loja' em vendas
vendas = vendas.merge(lojas, on='ID Loja')
print(vendas)
#Criando um arquivo com cada Shopping
dicionario_loja = {}
for i in lojas['Loja']:
    dicionario_loja[i] = vendas.loc[vendas['Loja']==i,:]

#Filtrando a data das pastas
dia_indicador = vendas['Data'].max()
#Ver se a pasta já existe 
caminho = pathlib.Path(r'C:\Users\anderson.filho\Desktop\Curso python\Hashtag\aula_24\Backup Arquivos Lojas')
arquivos_pasta = caminho.iterdir()
list_nome = [i.name for i in arquivos_pasta]

#Criar um arquivo com o nome da loja
for i in dicionario_loja:
    if i not in list_nome:
       novaP = caminho / i
       novaP.mkdir()
    nomeArq ='{}_{}_{}.xlsx'.format(dia_indicador.month,dia_indicador.day,i)
    print(nomeArq)
    local_arquivo = caminho/i/nomeArq
    
    dicionario_loja[i].to_excel(local_arquivo)

#Calcular o primeiro indicador da loja 
vendas_loja = dicionario_loja['Bourbon Shopping SP']
vendas_loja_dia = vendas_loja.loc[vendas_loja['Data']==dia_indicador,:]
#faturamento 
faturamento_ano= vendas_loja['Valor Final'].sum()
print(faturamento_ano)
faturamento_dia =vendas_loja_dia['Valor Unitário'].sum() 
print(faturamento_dia)

#diversidade de produtos 
qtd_produtosAnos = len(vendas_loja['Produto'].unique())
print(qtd_produtosAnos)
qtd_produtosDia = len(vendas_loja_dia['Produto'].unique())
print(qtd_produtosDia)

#Ticket medio e Ticket dia
valor_venda = vendas_loja.groupby('Código Venda' ).sum()

ticketMedioAno = valor_venda['Valor Final'].mena()
print(ticketMedioAno)