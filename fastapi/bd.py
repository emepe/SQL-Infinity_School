
from sqlalchemy import create_engine,Column,Integer,Date,String,select
from sqlalchemy.orm import Session,declarative_base
from datetime import datetime

# rodovia
engine = create_engine("sqlite:///./usuarios.db")



Base = declarative_base()

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key = True, auto_increment=True)
    username = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(Date,default=datetime.now())

    class Config:
        orm_mode = True

def pegar_sessao():
    try:
        sessionLocal = Session(bind=engine)
        yield sessionLocal
    except:
        pass
    finally:
        sessionLocal.close()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)   
    print("\033[32mBanco de Dados Criado e tabelas migradas. Pronto Para Uso!\033[m")