class Factura:
    def __init__(self) -> None:
        self.idfactura = None
        self.fechafactura = None        
        self.montofactura = None
        self.impuestofactura = None 
        self.nombreCliente = None        
        self.estadoFactura = None
    
    def calculaImpuesto(self):
        self.impuestofactura = self.montofactura * 0.13
        return self.impuestofactura