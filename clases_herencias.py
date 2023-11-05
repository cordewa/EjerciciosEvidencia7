class Curso:
    def __init__(self, fecha_inicio, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado, categoria):
        self.fecha_inicio = fecha_inicio
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado
        self.categoria = categoria
        self.clases = []

#Creando conjunto de clases:
class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.url_drive = url_drive

# Creando clase por docente
class Docente:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

# Creando clase por un Usuario Final. En el estado permanece Inactivo hasta validar el correo
class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave = clave
        self.estado = "Inactivo"  

# Creando clase para Administrador
class Administrador:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email

# cCarrito de Compras
class CarritoCompras:
    def __init__(self, usuario):
        self.usuario = usuario
        self.items = []

    def agregar_item(self, curso):
        self.items.append(curso)

    def calcular_total(self):
        total = 0
        for curso in self.items:
            total += curso.costo
        return total

# Creando Clase para Medio de Pago
class MedioPago:
    def __init__(self, tipo):
        self.tipo = tipo

# Creando Clase para Compra
class Compra:
    def __init__(self, fecha, usuario, total, medio_pago):
        self.fecha = fecha
        self.usuario = usuario
        self.total = total
        self.medio_pago = medio_pago

# Creando Clase para Pago con Tarjeta
class Tarjeta:
    def __init__(self, numero, nombre, fecha_vencimiento, cvv):
        self.numero = numero
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento
        self.cvv = cvv

# Creando Clase para Pago con Transferencia Bancaria
class TransferenciaBancaria:
    def __init__(self, banco, numero_cuenta):
        self.banco = banco
        self.numero_cuenta = numero_cuenta
        


#EJERCICIO DE HERENCIA
class Usuario:
    def __init__(self, nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.estado = "Inactivo"  

# Creando Clase Docente Siendo herencia de usuario
class Docente(Usuario):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(nombre, apellido, dni, direccion, fecha_nacimiento, localidad, codigo_postal, provincia, telefono_celular, email)
        self.cursos = []  

# Creando Clase para Compra
class Compra:
    def __init__(self, id_compra, id_carrito_compra, id_medios_pago, id_usuario, fecha, monto_total):
        self.id_compra = id_compra
        self.id_carrito_compra = id_carrito_compra
        self.id_medios_pago = id_medios_pago
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.monto_total = monto_total

# Creando Clase para info de contacto 
class MediosContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

class TiposMedioContacto(MediosContacto):
    WhatsApp = 1
    CorreoElectronico = 2
    CallCenter = 3
    ReferidoInterno = 4