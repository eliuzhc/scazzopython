class Traino:
  codice =1
  def __init__(self, nome, cognome):
    self.nome=nome
    self.cognome=cognome
    Traino.codice+=1
  def __add__ (self, other):
    nome_sommato =self.nome+ other.nome
    cognome_sommato=self.cognome+other.cognome
    return Traino(nome_sommato,cognome_sommato)
  def __str__(self):
    return 'nome:'+self.nome+'\ncognome:'+self.cognome+'\n'
    

c=Traino('davide','trainax')
b=Traino('DAVIDE','TRAINAX')

d=c+b
print (d)