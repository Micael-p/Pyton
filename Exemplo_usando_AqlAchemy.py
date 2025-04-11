from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conectando a um banco de dados SQLite em memoria
engine = create_engine('sqlite:///:memory:', echo=True)

#Criação da base declarativa
Base = declarative_base()

#Definição da classe (modelo) Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Usuario(id={self.id}, nome={self.nome}, idade={self.idade})"
    
# Criação das tabelas no banco de dados
Base.metadata.create_all(engine)

# Criação de uma sessão
Session = sessionmaker(bind=engine)
session = Session()

#Interção de dados
usuario1 = Usuario(nome='Micael', idade=21)
usuario2 = Usuario(nome='Pessoa', idade=12)
usuario3 = Usuario(nome='Da', idade=2)
usuario4 = Usuario(nome='Silva', idade=1)
session.add(usuario1)
session.add(usuario2)
session.add(usuario3)
session.add(usuario4)

#Commit das alterações
session.commit()

# Consulta de dados
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)
