class Persistencia:
    listadoFacturas = []
    
    @classmethod
    def agregarFactura(self,objeto):
        self.listadoFacturas.append(objeto)
    
    @classmethod    
    def obtenerFacturas(self):
        return self.listadoFacturas
    
    