Uma venv é um ambiente virtual de desenvolvimento, para utilizada, vc baixa o virtualenv usando,
'pip install virtualenv'

--- PARA UTILIZAR USA ---
    Para fazer sua venv, usa no terminal 
    'virtual venv' 
    depois vc percorre ate a área de 'activate' para inicialo . (usando 'v[tab]' + 's[tab]'+ 'a[tab]')
    '.\venv\Scripts\activate'

    Se já existe libs sendo usadas vc deve fazer o 'requirements.txt',colocar as libs intaladas e suas versões
    depois ir na venv e fazer 
    'pip install -r requirements.txt'

    se não existe vc vai instalando ao longo do codigo 

    para desativar a venv, usa o deactivate
    'deactivate'

--------------------------------------------

Agora para fazer a fazer uma venv ter um python diferente, 
    Devesse saber qual a versão a ser utilizada do python e onde esta seu executavel,
        Como fazer : Indo na versão desejada, abra o prompt do seu python,
        import as bibliotecas 'import os' e 'import sys'
        depois de importa. Roda o codigo 'os.path.dirname(sys.executable)', depois disso ele retornara 'C:\\Users\\anderson.filho\\AppData\\Local\\Programs\\Python\\Python312'.
        No terminal da venv que vc quer, usa o codigo 
        'virtualenv venv --python="C:\Users\anderson.filho\AppData\Local\Programs\Python\Python312\python.exe "'
          Lembrando de colocar o '\python.exe' no final, e deixar uma unica contrabarra
        Depois que fez todos os processos, dar o activate
        
    

