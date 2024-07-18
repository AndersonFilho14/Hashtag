import yagmail
 
#Para enviar emails, deve ser usado o padrão yagmail.SMTP, para que o email autorize que vc mande
#passando o email e senha e atribuindo a uma variavel pra que seja possivel mandar as mensagens 
usuario = yagmail.SMTP('---@ufrpe.br','senha')


#Para mandar a mensagem, basta informa em ordem o email que vai receber,o Assunto e o conteudo do email
usuario.send(to='email',subject='assunto',contents='Conteudo do email')
usuario.send('--@gmail.com','Texte de automação','Quero ficar rico')


#para mandae email com arquivo usa o attachments
usuario.send(to='email',subject='assunto',contents='Conteudo do email',attachments='arquivo')

#Caso queira mandar pra mais de uma pessoa, coloca barra 
usuario.send(to=['-@gmail.com','--@gmail.com'],subject='assunto',contents='larita + 2')

#Se quiser mandar uma copia, bota cc. Se for copia oculta bota bcc
usuario.send(to='email',cc='email diferente',subject='assunto',contents='Conteudo do email')
