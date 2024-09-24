# Clase
class Empleados:
    #valores inicialiados en 0
    id_empleados = 0
    nombre = ""
    telefono = 0
    direccion = ""
    correo = ""
    turno = ""
    sueldo = 0
    
    #funcion mostrar datos
    def mostrar_datos(self):
        print(f"Id: {self.id_empleados}")
        print(f"Nombre: {self.nombre}")
        print(f"Telefono: {self.telefono}")
        print(f"Direccion: {self.direccion}")
        print(f"Correo: {self.correo}")
        print(f"Turno: {self.turno}")
        print(f"Sueldo: {self.sueldo}")
    
    #funcion, lista
    def lista_empleados(self):
        print("\nLos nombres de mis empleados son: ")
        nombre = ["Miriam","Alondra","Kevin","Melany","Adriel"]
        for x in nombre:
            print(x)
    
    #funcion, tupla
    def tupla_tel(self):
        print("\nLos numeros de mis empleados son: ")
        tel = (6563457890, 6562340980, 6561234093, 6564567648, 6562340946)
        for x in tel:
            print(x)
            
    #funcion, diccionario
    def diccionario_cliente(self):
        print("\nLista de clientes atendidos")
        cliente = {
            "Karen" : "Atendió Miriam",
            "Cristian" : "Atendio Adriel",
            "Paola" : "Atendió Alondra",
            "Zyanya" : "Atendió Melany",
            "Roberto" : "Atendió Kevin"
        }
        for x, z in cliente.items():
            print(x,z)
    
    #funcion pago
    def pago(self):
        print("\nYa se les pagó a los empleados")
    
    #funcion liquidacion 
    def liquidacion(self):
        print("\nSe liquidaron a dos empleados")
        
# creacion de objeto
datos = Empleados()
datos.id_empleados = 3456
datos.nombre = "Melany"
datos.telefono = 6563457890
datos.direccion = "Sta. Anastasia 1080, Praderas del Sur"
datos.correo = "melanychaires23@gmail.com"
datos.turno = "1er Turno"
datos.sueldo = 1500

#mostrar datos
print("Mostrando datos de empleado 1")
datos.mostrar_datos()

#llamando a las funciones
datos.lista_empleados()
datos.tupla_tel()
datos.diccionario_cliente()
datos.pago()
datos.liquidacion()