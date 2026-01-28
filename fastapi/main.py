# USUARIOS

from fastapi import FastAPI

# 36.0.0.136/usuarios
# 36.0.0.136/produtos

# gabrieldev.com / DNS
# URL uniforme Resource Locator
# localizador de recurso único
from pydantic import BaseModel,EmailStr

class UsuarioIn(BaseModel):
    username:str
    email:EmailStr
    password:str

lista_usuarios = []

app = FastAPI()

@app.get("/usuarios")
def pegar_todos_usuarios():
    return lista_usuarios

@app.get("/usuarios/{id}")
def pegar_usuario_pelo_d(id:int):
    return lista_usuarios[id]

@app.post("/usuarios")
def adicionar_novo_usuario(usuario:UsuarioIn):
    lista_usuarios.append(usuario)
    return "Usuário cadastrado com sucesso!"