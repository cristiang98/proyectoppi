class Residente:
    def __init__(self, editNombrecompleto, editCedula, editCelular, editCorreo, editApartamento,editVehiculo, editPlaca, editCelda):
        self.nombreCompleto = editNombrecompleto
        self.cedula = editCedula
        self.celular = editCelular
        self.correo = editCorreo
        self.apartamento = editApartamento
        self.vehiculo3 = editVehiculo
        self.placa = editPlaca
        self.celda = editCelda


    def __str__(self):
        return f"Nombre: {self.nombreCompleto} Documento: {self.cedula}"