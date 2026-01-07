import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "in12345678",
    database = "escola"
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")
resultado = cursor.fetchone()
print(resultado)



# import mysql.connector as mysql

# db = mysql.connect(
#   host="localhost",
#   user="root",
#   port=3306,
#   password="in12345678",
#   database="escola"
# ) 

# # # cursor 
# # cursor = db.cursor()
# # nome = input("Digite seu nome: ")
# # cpf = input("Digite seu cpf: ")
# # cursor.execute(f"INSERT INTO aluno(nome,cpf) VALUES ('{nome}','{cpf}');")
# # db.commit()
# # # cursor.execute("SELECT * FROM aluno;")
# # resultado = cursor.fetchall()
# # print(resultado)
# =========================================================================================
# import mysql.connector as mysql
# from time import sleep
# import os 
# from tabulate import tabulate

# db = mysql.connect(
#   host="localhost",
#   user="root",
#   port=3306,
#   password="in12345678",
#   database="escola"
# ) 
# cursor = db.cursor()


# while True: 
#     print("="*30)
#     print("Cadastro de Alunos".center(30))
#     print("1 - Para listar alunos.")
#     print("2 - Para cadastrar aluno.")
#     print("3 - Para atualizar aluno.")
#     print("4 - Para deletar aluno.")
#     print("q - Sair.")
#     opcao = input("->")
#     if opcao == "1":
#         cursor.execute("SELECT * FROM aluno;")
#         resultado = cursor.fetchall()
#         print(resultado)
    
    
#     elif opcao == "2":
#         nome = input("Digite seu nome: ")
#         cpf = input("Digite seu cpf: ")
#         cursor.execute(f"INSERT INTO aluno(nome,cpf) VALUES('{nome}', '{cpf}')")
    
    
#     elif opcao == "3":
#         pass 

    
#     elif opcao == "4":
#         pass 


#     elif opcao == "q":
#         print("Finalizando")
#         break


# db.close()