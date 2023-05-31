class Visitante:
    def __init__(self, editApartamento, editNombrecompleto, editCelular, editNombrevisitante, editVehiculo, editPlaca, editFecha, editHora ):
        self.apartamento = editApartamento
        self.nombreCompleto = editNombrecompleto
        self.celular = editCelular
        self.nomVisitante = editNombrevisitante
        self.vehiculo2 = editVehiculo
        self.placa = editPlaca
        self.fecha = editFecha
        self.hora = editHora



    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.celular}"