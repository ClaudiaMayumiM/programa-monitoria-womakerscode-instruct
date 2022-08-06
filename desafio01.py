class Carro:
  def __init__(self, cor, modelo):
    self.ligado = False
    self.cor = cor
    self.modelo = modelo
    self.velocidade = 0
  
  def ligar(self):
    if self.ligado == False:
      self.ligado = True
    else:
      return 
  
  def desligar(self):
    if self.ligado == True and self.velocidade == 0:
      self.ligado = False
    else:
      return 
  
  def acelerar(self):
    if self.velocidade < 200 and self.ligado == True:
      self.velocidade += 10
    else:
      return 
  
  def desacelerar(self):
    if self.velocidade > 0 and self.ligado == True:
      self.velocidade -= 10 
    else:
      return 
  


gol = Carro('vermelho', 'gol')

gol.ligar()
print(f'Ligando carro: {gol.ligado}')
gol.acelerar()
print(f'Acelerando - velocidade: {gol.velocidade}')
gol.acelerar()
print(f'Acelerando - velocidade: {gol.velocidade}')
gol.acelerar()
print(f'Acelerando - velocidade: {gol.velocidade}')
gol.desacelerar()
print(f'Desacelerando - velocidade: {gol.velocidade}')
gol.desacelerar()
print(f'Desacelerando - velocidade: {gol.velocidade}')
gol.desacelerar()
print(f'Desacelerando - velocidade: {gol.velocidade}')
gol.desligar()
print(f'Desligando carro {gol.ligado}')
