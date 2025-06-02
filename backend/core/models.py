from django.db import models

class Receptor(models.Model):
    nombrePila = models.CharField(max_length=255)
    apPaterno = models.CharField(max_length=255)
    apMaterno = models.CharField(max_length=255)
    correo = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.nombrePila} {self.apPaterno} {self.apMaterno}"


class Estado(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Metodos(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    codigo = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        # Solo al crear, y si no se pasó número manualmente
        if self._state.adding and self.numero is None:
            ultimo = Metodos.objects.filter(organizacion=self.organizacion) \
                                  .aggregate(max_num=models.Max('numero'))['max_num']
            self.numero = (ultimo or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo
    
class Servicio(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    nombreServicio = models.CharField(max_length=255)
    metodos = models.ForeignKey(Metodos, on_delete=models.CASCADE)

    
    def save(self, *args, **kwargs):
        # Solo asignar número si es un nuevo objeto
        if self._state.adding and self.numero is None:
            ultimo_numero = Servicio.objects.filter(organizacion=self.organizacion).aggregate(
                ultimo=models.Max('numero'))['ultimo']
            self.numero = (ultimo_numero or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.organizacion.nombre} - {self.numero} - {self.nombreServicio} - ${self.precio}"

class Empresa(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(max_length=13)
    codigoPostal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    numeroExterior = models.CharField(max_length=24, null=True, blank=True)
    calle = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self._state.adding and self.numero is None:
            ultimo = Empresa.objects.filter(organizacion=self.organizacion).aggregate(max_num=models.Max('numero'))['max_num']
            self.numero = (ultimo or 0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class OrdenTrabajo(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    codigo = models.CharField(max_length=255, blank=True)
    nombreusuario = models.CharField(max_length=255, null=True, blank=True)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    receptor = models.ForeignKey('Receptor', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    servicio = models.ManyToManyField('Servicio', through='OrdenTrabajoServicio')

    def __str__(self):
        return f"OT {self.numero} – {self.codigo}"

class OrdenTrabajoServicio(models.Model):
    ordenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.cantidad} x {self.servicio.nombreServicio} en Orden {self.ordenTrabajo.id}"

#--------------- 1. Datos delk sitio de muestreo -------------
class SitioMuestreo(models.Model):
    #El nombre de la empresa, se puede obtener directamente de una consulta asi que puede no ser necesario aqui ⬇︎
    #nombreEmpresa = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255)
    giroEmpresa = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombreEmpresa

#------------- 2.- IDENTIFICACION DEL PUNTO DE MUESTREO -------------
class TipoDescarga(models.Model):
    nombre = models.CharField(max_length=50)
    #para la parte de Otro ⬇︎
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre if self.nombre else self.descripcion

class AguaResidualTratamientos(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre if self.nombre else "No especificado"

class PuntoMuestreo(models.Model):
    #son los ids que mas adelante iran en la cadena de custodia ⬇︎
    identificacionPunto = models.CharField(max_length=50)
    descripcionProceso = models.TextField(max_length=255, null=True, blank=True)
    origenMuestra = models.CharField(max_length=50, null=True, blank=True)
    aguaResidualOtros = models.CharField(max_length=50, null=True, blank=True)
    horasOpera = models.CharField(max_length=50, null=True, blank=True)
    horasDescarga = models.CharField(max_length=50, null=True, blank=True)
    frecuenciaDescarga = models.CharField(max_length=50, null=True, blank=True)
    #esto es para la parte de nombre completo y puesto/cargo, podria hacerse de otra forma ⬇︎
    informacionProporcionada = models.CharField(max_length=50, null=True, blank=True)
    aguaResidualTratamientos = models.ForeignKey(AguaResidualTratamientos, on_delete=models.CASCADE)
    tipoDescarga = models.ForeignKey(TipoDescarga, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.identificacionPunto


# #------------- 3.- PROCEDIMIENTO DE MUESTREO -------------
class MaterialUso(models.Model):
    # Siempre van todos seleccionados, podria no necesitarse este modelo ⬇︎
    nombre = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Recipiente(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.nombre

class PreservadorUtilizado(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class frecuenciaMuestreo(models.Model):
    horaOperacion = models.CharField(max_length=50, null=True, blank=True)
    # Se refiere a la cantidad minima de meustras que ya tiene la tabla ⬇︎
    numeroMuestrasSimples = models.CharField(max_length=50, null=True, blank=True)
    invervaloMinimo = models.CharField(max_length=50, null=True, blank=True)
    invervaloMaximo = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.horaOperacion} - {self.numeroMuestrasSimples} muestras - {self.invervaloMinimo} a {self.invervaloMaximo}"

class tipoAgua(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    #para la parte de Otro ⬇︎
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre if self.nombre else self.descripcion

    #Una descarga de agua residual siempre cae solo en 1 cuerpo receptor ⬇︎
class cuerpoReceptor(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    #para la parte de Otro ⬇︎
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nombre if self.nombre else self.descripcion

class ProcedimientoMuestreo(models.Model):
    # Aqui debera ir siempre la norma NOM-002-SEMARNAT-1996 COMPLETA + DQO ⬇︎
    ParametroADeterminar = models.CharField(max_length=50, null=True, blank=True)
    MaterialUso = models.ForeignKey(MaterialUso, on_delete=models.CASCADE)
    Recipiente = models.ForeignKey(Recipiente, on_delete=models.CASCADE)
    PreservadorUtilizado = models.ForeignKey(PreservadorUtilizado, on_delete=models.CASCADE)
    # True para puntual, False para compuesta ⬇︎, o podria ser una entidad para usar el id
    tipoMuestreo = models.BooleanField(default=False)  
    frecuenciaMuestreo = models.ForeignKey(frecuenciaMuestreo, on_delete=models.CASCADE)
    tipoAgua = models.ForeignKey(tipoAgua, on_delete=models.CASCADE)
    cuerpoReceptor = models.ForeignKey(cuerpoReceptor, on_delete=models.CASCADE)
    def __str__(self):
        return f"Procedimiento de Muestreo - Parametro: {self.ParametroADeterminar} - Tipo: {'Puntual' if self.tipoMuestreo else 'Compuesta'}"

# #------------- 4.- PLAN DE MUESTREO -------------
class PlanMuestreo(models.Model):
    inicial = models.CharField(max_length=50, null=True, blank=True)
    fechaInicial = models.DateField(null=True, blank=True)
    final = models.CharField(max_length=50, null=True, blank=True)
    fechaFinal = models.DateField(null=True, blank=True)
    observaciones = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"Plan de Muestreo - Inicial: {self.inicial} - Final: {self.final}"


# #------------- PRIMERA HOJA DEL FORMATO -------------
class ProtocoloMuestreo(models.Model):
    SitioMuestreo = models.ForeignKey(SitioMuestreo, on_delete=models.CASCADE)
    PuntoMuestreo = models.ForeignKey(PuntoMuestreo, on_delete=models.CASCADE)
    ProcedimientoMuestreo = models.ForeignKey(ProcedimientoMuestreo, on_delete=models.CASCADE)
    PlanMuestreo = models.ForeignKey(PlanMuestreo, on_delete=models.CASCADE)
    OrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Protocolo de Muestreo - OT: {self.OrdenTrabajo.codigo} - Punto: {self.PuntoMuestreo.identificacionPunto}"

## ------------- 5.- HOJA DE CAMPO -------------
class MuestraHojaCampo(models.Model):
    pass

class HojaCampo(models.Model):
    #podria no se necesaria por la relacion con ProtocoloMuestreo ⬇︎
    OrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    # Podria no ser necesario si se trae de una consulta
    nombreEmpresa = models.CharField(max_length=255)
    # es lo mismo que el atributo identificacionPunto del modelo PuntoMuestreo, podria no ser necesario ⬇︎
    idMuestra = models.CharField(max_length=50)
    #siempre va a ser la norma NOM-002-SEMARNAT-1996/NMX-AA-003-1980 asi que podria evitarse ⬇︎
    normaReferencia = models.CharField(max_length=50)
    # se refiere a si es Bajo techo o Intemperie/Cielo abierto ⬇︎
    condicionMuestreo = models.CharField(max_length=50)

##  ------------- CADENA DE CUSTODIA -------------
# class Preservador(models.Model):
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nombre

# class Matriz(models.Model):
#     codigo = models.CharField(max_length=20)
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.codigo + ' - ' + self.nombre

# class Clave(models.Model):
#     codigo = models.CharField(max_length=20)
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.codigo + ' - ' + self.nombre

# class Contenedor(models.Model):
#     codigo = models.CharField(max_length=20)
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.codigo + ' - ' + self.nombre
# class Parametro(models.Model):
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nombre

# class Prioridad(models.Model):
#     codigo = models.CharField(max_length=20)
#     descripcion = models.CharField(max_length=50)

#     def __str__(self):
#         return self.codigo + ' - ' + self.descripcion\
            
# #agregar tabla para idfiltro
# class Filtro(models.Model):
#     codigo = models.CharField(max_length=20)
#     descripcion = models.CharField(max_length=50, null=True, blank=True)

#     def __str__(self):
#         return self.codigo + ' - ' + self.descripcion

# class EstadoCustodia(models.Model):
#     descripcion = models.CharField(max_length=20)

#     def __str__(self):
#         return self.descripcion

# class CustodiaExterna(models.Model):
#     contacto = models.CharField(max_length=50)
#     puestoCargoContacto = models.CharField(max_length=50, null=True, blank=True)
#     celularContacto = models.CharField(max_length=50, null=True, blank=True)
#     correoContacto = models.EmailField(max_length=50, null=True, blank=True)
#     puntosMuestreoAutorizados = models.CharField(max_length=50)
#     modificacionOrdenTrabajo = models.BooleanField()
#     observacionesModificacion = models.TextField(max_length=120, null=True, blank=True)
#     asesoriaGestionAmbiental = models.BooleanField()
#     muestreoRequerido = models.CharField(max_length=50)
#     fechaFinal = models.DateField(null=True, blank=True)
#     horaFinal = models.TimeField(null=True, blank=True)
#     muestraCompuesta = models.BooleanField()
#     idMuestraCompuesta = models.CharField(max_length=50, null=True, blank=True)
#     muestraPuntual = models.BooleanField()
#     idMuestraPuntual = models.CharField(max_length=50, null=True, blank=True)
#     observaciones = models.TextField(max_length=325, null=True, blank=True)
#     estado = models.ForeignKey(EstadoCustodia, on_delete=models.CASCADE)
#     prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
#     receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
#     ordenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"CustodiaExterna - {self.contacto}"

# class Muestra(models.Model):
#     #nomenclaruta de la identificacion de campo
#     #nomenclatura-filtro-corrida-contenedor-numero de ducto
#     identificacionCampo = models.CharField(max_length=50)
#     fechaMuestreo = models.DateField()
#     horaMuestreo = models.TimeField()
#     volumenCantidad = models.CharField(max_length=50, null=True, blank=True)
#     numeroContenedor = models.CharField(max_length=50)
#     origenMuestra = models.CharField(max_length=50)
#     idLaboratorio = models.CharField(max_length=50, null=True, blank=True)
#     filtro = models.ForeignKey(Filtro, on_delete=models.CASCADE, null=True, blank=True)
#     preservador = models.ManyToManyField(Preservador, through='PreservadorMuestra')
#     matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
#     contenedor = models.ForeignKey(Contenedor, on_delete=models.CASCADE)
#     parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
#     custodiaExterna = models.ForeignKey(CustodiaExterna, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Muestra - {self.identificacionCampo}"
    
# class PreservadorMuestra(models.Model):
#     preservador = models.ForeignKey(Preservador, on_delete=models.CASCADE)
#     muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f"PreservadorMuestra - {self.preservador} - {self.muestra}"

# #mover a la app del laboratorio
# class RegistroCustodia(models.Model):
#     CustodiaExterna = models.ForeignKey(CustodiaExterna, on_delete=models.CASCADE)
#     entregadoPor = models.CharField(max_length=100)
#     fechaEntrega = models.DateField()
#     horaEntrega = models.TimeField()
#     recibidoPor = models.CharField(max_length=100)
#     fechaEecepcion = models.DateField()
#     horaRecepcion = models.TimeField()

#     def __str__(self):
#         return f"Registro de Custodia - Entregado por {self.entregadoPor} a {self.recibidoPor}"