class Pessoa:
    def __init__(self, nome="", idade="", sexo=""):
        self._nome      = nome
        self._idade     = idade
        self._sexo      = sexo

    def apresentar(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Sexo: {self._sexo}")


class Aluno(Pessoa):
    def __init__(self, nome="", idade="", sexo="",matricula=""):
        super().__init__(nome, idade, sexo)
        self._matricula     = matricula

    def apresentar(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Sexo: {self._sexo}")
        print(f"Matricula: {self._matricula}")


class Professor(Pessoa):
    def __init__(self, nome="", idade="", sexo="",disciplina=""):
        super().__init__(nome, idade, sexo)
        self._disciplina    = disciplina

    def apresentar(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Sexo: {self._sexo}")
        print(f"Disciplina: {self._disciplina}")


pe1     = Pessoa(nome="Isaque", idade= 18, sexo="Masculino")
alu1    = Aluno(nome="ILucas", idade= 22, sexo="Masculino", matricula= 2)
prof1   = Professor(nome="Laura", idade= 28, sexo="Feminino", disciplina= "Filosofia")


pe1.apresentar()
alu1.apresentar()
prof1.apresentar()
print()