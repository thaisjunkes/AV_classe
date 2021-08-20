import os
from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


class Paciente(db.Model):
    # definição do nome da tabela no banco
    __tablename__ = "pacientes"

    # atributos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    data_nascimento = db.Column(db.DateTime)
    CPF = db.Column(db.Text, nullable=False, unique=True)
    telefone = db.Column(db.Text)
    email = db.Column(db.Text)
    sexo = db.Column(db.Text)
    senha = db.Column(db.Text)
    # representação dos dados por meio de string
    def __repr__(self):
        return f"<Paciente {self.nome}>"

    # criação de método construtor para não precisar espeficar os atributos na instânciação das classes
    def __init__(self, nome:str, data_nascimento:str, CPF:str, telefone:str, email: str, sexo: str, senha:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.CPF = CPF
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.senha = senha

    # definição de método 
    # e retorno de dados em formato JSON
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "CPF": self.CPF,
            "telefone": self.telefone,
            "email": self.email,
            "sexo": self.sexo,
            "senha": self.senha
        }

class Exame(db.Model):
    __tablename__ = "exames"

    id_exame = db.Column(db.Integer, primary_key=True)
    nome_exame = db.Column(db.Text)
    data_exame = db.Column(db.DateTime)
    resultado= db.Column(db.Text)

    #relacionamento de composição entre Paciente e Exame
    id_paciente = db.Column(db.Integer, db.ForeignKey(Paciente.CPF), nullable=False)
    paciente = db.relationship("Paciente")

    def __init__(self, nome_exame:str, data_exame:date, paciente: Paciente):
        self.nome_exame = nome_exame
        self.data_exame = data_exame
        self.paciente = paciente

    def __repr__(self):
        return f"<Paciente {self.nome}>"

    def json(self):
        return {
            "id_exame": self.id_exame,
            "nome_exame": self.nome_exame,
            "data_exame": self.data_exame,
            "resultado": self.resultado,
            "id_paciente": self.id_paciente,
            "paciente": self.paciente.json()
        }


if __name__ == "__main__":
    
    # geração de objetos a partir das classes
    
    paciente1 = Paciente("Marcia da Silva", "24/12/1991", "222.333.444-10", "(47)99955-6611", "marciasilva@gmail.com", "Feminino", "minhasenhae")

    # passagem do objeto Paciente, para compor objeto Exame
    exame1 = Exame("Hemograma", "21/01/2020", paciente1)

    # retorno dos dados
    print(f"O exame {exame1.nome_exame} foi feito no dia {exame1.data_exame} no {exame1.paciente}")