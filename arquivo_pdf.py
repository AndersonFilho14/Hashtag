Para usar o pdf em python, se importa essas duas libs
import PyPDF2 as pyf
from pathlib import Path

# Ler um arquivo pdf
# pyf.PdfFileReader
# Mesclar arquivos
# pyf.PdfFileMerger
# Escrever no pdf
# pyf.PdfFileWriter

arquivo_pdf = pyf.PdfFileReader(Caminho do arquivo)
i= 1
for i in arquivo_pdf:
    arquivo_novo = pyf.PdfFileWriter()
    arquivo_novo.addPage(i)
    #salvar o arquivo
    with Path('nome_da_nova_pagina.pdf').open(mode='wb') as arquivo_final:
        arquivo_novo.write(arquivo_novo22)