class Carro:
  def __init__(self, placa):
    self._placa = placa 
    self.estacionado = False 
  
  def estacionar(self):
    if self.estacionado == False:
      self.estacionado = True
  
  def sair_da_vaga(self):
    if self.estacionado == True:
      self.estacionado = False


class Moto(Carro):
  def __init__(self, placa):
    super().__init__(placa)
    self.estacionado = False 
  
  def estacionar(self):
    return super().estacionar()
  
  def sair_da_vaga(self):
    return super().sair_da_vaga()


class Estacionamento:
  def __init__(self):
    self.vagas_totais_carro = 0    
    self.vagas_totais_moto = 0
    self.moto_em_carro = 0

  def imprime_vagas_carro(self):
    print(self.vagas_totais_carro)
  
  def imprime_vagas_moto(self):
    print(self.vagas_totais_moto)

  def imprime_livre_carro(self):
    self.livre_carro = 25 - self.vagas_totais_carro
    print(self.livre_carro)
  
  def imprime_livre_moto(self):
    self.livre_moto = 25 - self.vagas_totais_moto
    print(self.livre_moto)

  def estado_estacionamento(self):
    print(f'O estacionamento está com {self.livre_carro} vagas livres para carros ou motos e {self.livre_moto} vagas livres para motos.')


class Vaga(Estacionamento, Carro):
  def __init__(self, id, tipo):
    Estacionamento.__init__(self)
    self._id = id 
    self.tipo = tipo 
    self.livre = True 
    self.placa = None 
  
  def ocupar(self, veiculo):
    if self.livre == True:
      self.livre = False 
      
      if isinstance(veiculo, Carro) and self.tipo == 'carro':
        if isinstance(estacionamento_p, Estacionamento):
          if estacionamento_p.vagas_totais_carro < 25:
            self.placa = veiculo._placa
            estacionamento_p.vagas_totais_carro += 1
            print(f'O veículo de placa {self.placa} estacionou na vaga {self._id}.')
          else:
            print('Estacionamento para carros lotado!')
      
      if isinstance(veiculo, Moto):
        if isinstance(estacionamento_p, Estacionamento):
          if estacionamento_p.vagas_totais_moto < 25:
            self.placa = veiculo._placa 
            estacionamento_p.vagas_totais_moto += 1
            print(f'O veículo de placa {self.placa} estacionou na vaga {self._id}.')
          elif estacionamento_p.vagas_totais_carro < 25:
            self.placa = veiculo._placa
            estacionamento_p.vagas_totais_carro += 1
            estacionamento_p.moto_em_carro += 1
            print(f'O veículo de placa {self.placa} estacionou na vaga {self._id}.')
          else:
            print('Estacionamento para carros e estacionamento para motos lotados!')
      
  def desocupar(self, veiculo):
    if self.livre == False:
      self.livre = True 

      if isinstance(estacionamento_p, Estacionamento):
        if isinstance(veiculo, Carro) and self.tipo == 'carro':
          estacionamento_p.vagas_totais_carro -= 1
          print(f'O veículo de placa {self.placa} desocupou a vaga {self._id}.')
          self.placa = None 
        elif isinstance(veiculo, Moto) and estacionamento_p.moto_em_carro != 0:
          estacionamento_p.vagas_totais_carro -= 1
          print(f'O veículo de placa {self.placa} desocupou a vaga {self._id}.')
          self.placa = None
          estacionamento_p.moto_em_carro['veiculo._placa'] = False 
        else:
          estacionamento_p.vagas_totais_moto -= 1
          print(f'O veículo de placa {self.placa} desocupou a vaga {self._id}.')
          self.placa = None


estacionamento_p = Estacionamento()

gol = Carro(1234)
bis = Moto(5678)
celta = Carro(1122)
suzuki = Moto(4455)

gol.estacionar()
bis.estacionar()
celta.estacionar()
suzuki.estacionar()

vaga1 = Vaga(1, 'carro')
vaga1.ocupar(gol)
vaga2 = Vaga(2, 'moto')
vaga2.ocupar(bis)
vaga3 = Vaga(3, 'carro')
vaga3.ocupar(celta)
vaga4 = Vaga(4, 'moto')
vaga4.ocupar(suzuki)

vaga1.desocupar(gol)
vaga2.desocupar(bis)
vaga3.desocupar(celta)
vaga4.desocupar(suzuki)

estacionamento_p.imprime_vagas_carro()
estacionamento_p.imprime_vagas_moto()
estacionamento_p.imprime_livre_carro()
estacionamento_p.imprime_livre_moto()
estacionamento_p.estado_estacionamento()