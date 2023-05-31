class Visitante:
    def __init__(self, editApartamento, editNombrecompleto, editCelular, editNombrevisitante, editVehiculo, editPlaca ):
        self.apartamento = editApartamento
        self.nombreCompleto = editNombrecompleto
        self.celular = editCelular
        self.nomVisitante = editNombrevisitante
        self.vehiculo2 = editVehiculo
        self.placa = editPlaca



    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.celular}"