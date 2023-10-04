'''
determine em 2 variaveis.
senha e email

mas já contenha anteriormente um email e uma senha cadastrado.

depois solicite ao usuario uma senha e email . utilize laço repetição e condição para veririficar se email e senha estão corretos.

enquanto não digitar senha e email certos , continue num Loop.
'''

#encaminhar resposta via link gitHub
#

key_email_cadastrado = '123'
email_cadastrado = 'italo@test.com'

verific_email = input('\n Digite o email cadastrado para acesso: \n')
while verific_email != email_cadastrado:
    print('\n >>> ATENÇÂO: Email não cadastrado. Tente de novo! <<< \n')
    verific_email = input('\n Digite o email cadastrado para acesso: \n')
    if verific_email == email_cadastrado:
           verific_key = input('\n Digite senha cadastrada para acesso: \n')             
           if verific_key != key_email_cadastrado:
                while verific_key != key_email_cadastrado:
                    print('\n Acesso Negado! Verifique a senha e tente novamente... \n')
                    verific_key = input('\n Digite senha cadastrada para acesso: \n')
print('\n\n Acesso autorizado! \n\n')               
           
                


