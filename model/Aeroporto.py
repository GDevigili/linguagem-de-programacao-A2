
class Aeroporto:
    def __init__(self, nome, cidade, estado, pais, centroide):
        self._nome = nome
        self._cidade = cidade
        self._estado = estado
        self._pais = pais
        self._centroide = centroide    
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def setNome(self, nome):
        self._nome = nome
        
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def setCidade(self, cidade):
        self._cidade = cidade
    
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def setEstado(self, estado):
        self._estado = estado
    
    @property
    def pais(self):
        return self._pais
    
    @pais.setter
    def setPais(self, pais):
        self._pais = pais
    
    @property
    def centroide(self):
        return self._centroide
    
    @centroide.setter
    def setCentroide(self, centroide):
        self._centroide = centroide
    