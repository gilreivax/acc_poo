class Pessoa:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento


class Professor (Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)   
        self.disciplinas = []
         
    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        

class Aluno (Pessoa):
    def __init__(self, nome, nascimento, tipo):
        super().__init__(nome, nascimento)
        self.tipo = tipo 
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0
        self.disciplinas = []
        
    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    
    def incluir_quantidade(self, quantidade):
        self.quantidade += quantidade
    
    def incluir_mau_feito(self, quantidade):
        self.quantidade += quantidade
    
    def get_triunfos (self):
        return self.__triunfos
    
    def get_mau_feitos(self):
        return self.__mau_feitos
    
    def set_casa (self, Casa):
        self.Casa = Casa
    

class Disciplina :
    def __init__(self, nome,  ementa):
        self.nome = nome
        self.ementa = ementa 
    
    
class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal 
        self.__diretor = None
        self.__monitor = None
    
    def get_diretor(self):
        return self.__diretor
    
    def get_monitor(self):
        return self.__monitor
    
    def set_diretor (self, Professor):
        self.__diretor = Professor
        
    def set_monitor (self, Aluno):
        self.__monitor = Aluno
    

class Escola:
    def __init__(self, nome):
        self.nome = nome 
        self.casas = []
        
    def incluir_casa (self, casa):
        self.casas.append(casa)
        

class Torneio(Casa):
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2 
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0
    
    def marcar_ponto(self, casa, quantidade):
        self.casa = casa
        self.quantidade += quantidade
    
    def get_pontos_casa1 (self):
        return self.__pontos_casa1
    
    def get_pontos_casa1 (self):
        return self.__pontos_casa2