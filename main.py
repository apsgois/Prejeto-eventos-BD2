from helper.WriteAJson import writeAJson
from db.eventoDB import EventoDAO
import json

evento = EventoDAO()

class Pessoa(object):
    def __init__(self, nome):
        self.nome = nome

#Quem vai dar a palestra no evento:
class Palestrante(Pessoa):
    def __init__(self, especialidade, nome):
        Pessoa.__init__(self, nome)
        self.especialidade = especialidade

    def to_string(self):
        writeAJson(self.__dict__, "Palestrante")
        return {"nome": self.nome, "especialidade": self.especialidade}

#Quem vai ao evento:
class Usuario(Pessoa):
    def __init__(self, idade: int, sexo: str, telefone: int, nome: str):
        super().__init__(nome)
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone


    def to_string(self):
        writeAJson(self.__dict__, "usuario")
        return {'Idade': self.idade, 'sexo': self.sexo, 'telefone': self.telefone, 'nome': self.nome}


class Palestra:
    def __init__(self, assunto):
        self.palestrante: Palestrante = None
        self.usuarios: list = []
        self.assunto = assunto


    def getListaPresenca(self) -> list:
        lista = []
        for usuario in self.usuarios:
            lista.append(usuario.to_string())
        print(lista)
        return lista

def default():
    print('Valor incorreto')


if __name__ == "__main__":
    while True:
        print('''
                      MENU:

                      [1] - Cadastrar nova palestra
                      [2] - Ver  palestras cadastradas
                      [3] - Atualizar palestras 
                      [4] - Deletar palestra
                      [5] - Sair
                  ''')
        x = input('Digite a opção desejada: ')
        match x:
            case '1':
                assuntoDaAula = input('Entre com o assunto da palestra:')
                palestra = Palestra(assuntoDaAula)
                #p1 = Palestrante('Banco de dados', 'Renzo')
                nome = input('Entre com o nome do palestrante: ')
                especialidade = input('Qual a especialidade: ')
                p1 = Palestrante(especialidade, nome)
                palestra.palestrante = p1
                q_usuario = input('Quantos usuarios tem na palestra? ')
                for q_usuarios in range(int(q_usuario)):
                    nome = input('Digite o nome do usuario: ')
                    idade = int(input('Digite a idade: '))
                    sexo = input('Digite o sexo: ')
                    telefone = int(input('Digite o telefone: '))
                    usuario = Usuario(idade, sexo, telefone, nome)
                    palestra.usuarios.append(usuario)

                print(palestra.getListaPresenca())
                evento.create_aula(palestra)
                print('Palestra cadastrada com sucesso!')

            case '2':
                assunto = input('Digite o assunto da palestra que deseja ver:')
                ler = evento.read(assunto)
                print('Ver em assunto.json')
                writeAJson(ler, 'assunto')

            case '3':
                assunto_antigo = input('Digite o assunto da palestra que deseja atualizar:')
                assunto_novo = input('Digite o novo assunto :')
                assunto = evento.update(assunto_antigo, assunto_novo)
                print('Assunto atualizado com sucesso!')

            case '4':
                assunto = input('Digite a palestra que deseja deletar:')
                evento.delete(assunto)
                print('Palestra deletada com sucesso!')
            case '5':
                break

            case _:
                default()
