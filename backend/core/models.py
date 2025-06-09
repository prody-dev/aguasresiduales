from django.db import models

class Receptor(models.Model):
    nombrePila = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=50)
    apMaterno = models.CharField(max_length=50)
    correo = models.EmailField(blank=True, null=True)
    celular = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.nombrePila} {self.apPaterno} {self.apMaterno}"

class Estado(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Metodo(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    codigo = models.CharField(max_length=50)

class Servicio(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    nombreServicio = models.CharField(max_length=255)
    metodo = models.ForeignKey(Metodo, on_delete=models.CASCADE)

class Empresa(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=255)
    codigoPostal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    numeroExterior = models.CharField(max_length=24, null=True, blank=True)
    calle = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)

class OrdenTrabajo(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    codigo = models.CharField(max_length=255, blank=True)
    nombreUsuario = models.CharField(max_length=255, null=True, blank=True)
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

#--------------- 1. Datos del sitio de muestreo -------------
class SitioMuestreo(models.Model):
    #El nombre de la empresa, se puede obtener directamente de una consulta asi que puede no ser necesario aqui ⬇︎
    #nombreEmpresa = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, null=True, blank=True)
    giroEmpresa = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.domicilio if self.domicilio else "Sitio de Muestreo sin Domicilio"

#------------- 2.- IDENTIFICACION DEL PUNTO DE MUESTREO -------------
class TipoDescarga(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class AguaResidualTratamiento(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre if self.nombre else "No especificado"

class PuntoMuestreo(models.Model):
    #son los ids que mas adelante iran en la cadena de custodia ⬇︎
    identificacionPunto = models.CharField(max_length=50, null=True, blank=True)
    descripcionProceso = models.TextField(max_length=255, null=True, blank=True)
    origenMuestra = models.CharField(max_length=50, null=True, blank=True)
    aguaResidualOtro = models.CharField(max_length=50, null=True, blank=True)
    horasOperacion = models.CharField(max_length=50, null=True, blank=True)
    horasDescarga = models.CharField(max_length=50, null=True, blank=True)
    frecuenciaDescarga = models.CharField(max_length=50, null=True, blank=True)
    #esto es para la parte de nombre completo y puesto/cargo, podria hacerse de otra forma ⬇︎
    informacionProporcionada = models.CharField(max_length=50, null=True, blank=True)
    aguaResidualTratamiento = models.ForeignKey(AguaResidualTratamiento, on_delete=models.CASCADE, null=True, blank=True)
    tipoDescarga = models.ForeignKey(TipoDescarga, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.identificacionPunto

# #------------- 3.- PROCEDIMIENTO DE MUESTREO -------------
class MaterialUso(models.Model):
    # Siempre van todos seleccionados, podria no necesitarse este modelo ⬇︎
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Recipiente(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class PreservadorUtilizado(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class FrecuenciaMuestreo(models.Model):
    horaOperacion = models.CharField(max_length=50)
    # Se refiere a la cantidad minima de meustras que ya tiene la tabla ⬇︎
    numeroMuestrasSimples = models.CharField(max_length=50)
    invervaloMinimo = models.CharField(max_length=50)
    invervaloMaximo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.horaOperacion} - {self.numeroMuestrasSimples} muestras - {self.invervaloMinimo} a {self.invervaloMaximo}"

class TipoAgua(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

    #Una descarga de agua residual siempre cae solo en 1 cuerpo receptor ⬇︎
    
class CuerpoReceptor(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class ProcedimientoMuestreo(models.Model):
    # Aqui debera ir siempre la norma NOM-002-SEMARNAT-1996 COMPLETA + DQO ⬇︎
    parametroADeterminar = models.CharField(max_length=50, null=True, blank=True)
    materialUso = models.ForeignKey(MaterialUso, on_delete=models.CASCADE, null=True, blank=True)
    recipiente = models.ForeignKey(Recipiente, on_delete=models.CASCADE, null=True, blank=True)
    preservadorUtilizado = models.ForeignKey(PreservadorUtilizado, on_delete=models.CASCADE, null=True, blank=True)
    # True para puntual, False para compuesta ⬇︎, o podria ser una entidad para usar el id
    tipoMuestreo = models.BooleanField(default=False)  
    frecuenciaMuestreo = models.ForeignKey(FrecuenciaMuestreo, on_delete=models.CASCADE, null=True, blank=True)
    tipoAgua = models.ForeignKey(TipoAgua, on_delete=models.CASCADE, null=True, blank=True)
    tipoAguaOtro = models.CharField(max_length=50, null=True, blank=True)
    cuerpoReceptor = models.ForeignKey(CuerpoReceptor, on_delete=models.CASCADE, null=True, blank=True)
    cuerpoReceptorOtro = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f"Procedimiento de Muestreo - Parametro: {self.parametroADeterminar} - Tipo: {'Puntual' if self.tipoMuestreo else 'Compuesta'}"

# #------------- 4.- PLAN DE MUESTREO -------------
class PlanMuestreo(models.Model):
    inicial = models.CharField(max_length=50, null=True, blank=True)
    fechaInicial = models.DateField(null=True, blank=True)
    final = models.CharField(max_length=50, null=True, blank=True)
    fechaFinal = models.DateField(null=True, blank=True)
    observacion = models.TextField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"Plan de Muestreo - Inicial: {self.inicial} - Final: {self.final}"

# #------------- PRIMERA HOJA DEL FORMATO -------------
class ProtocoloMuestreo(models.Model):
    sitioMuestreo = models.ForeignKey(SitioMuestreo, on_delete=models.CASCADE, null=True, blank=True)
    puntoMuestreo = models.ForeignKey(PuntoMuestreo, on_delete=models.CASCADE, null=True, blank=True)
    procedimientoMuestreo = models.ForeignKey(ProcedimientoMuestreo, on_delete=models.CASCADE, null=True, blank=True)
    planMuestreo = models.ForeignKey(PlanMuestreo, on_delete=models.CASCADE, null=True, blank=True)
    aguaResidualInforme = models.ForeignKey('AguaResidualInforme', on_delete=models.CASCADE)
 
    def __str__(self):
        return f"Protocolo de Muestreo - OT: {self.AguaResidualInforme.OrdenTrabajo.codigo} - Punto: {self.PuntoMuestreo.identificacionPunto}"

## ------------- 5.- HOJA DE CAMPO -------------
class PhMuestra(models.Model):
    ph1 = models.DecimalField(max_digits=5, decimal_places=2)
    ph2 = models.DecimalField(max_digits=5, decimal_places=2)
    ph3 = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        ph_values = [self.ph1, self.ph2, self.ph3]
        
class TemperaturaMuestra(models.Model):
    temp1 = models.DecimalField(max_digits=5, decimal_places=2)
    temp2 = models.DecimalField(max_digits=5, decimal_places=2)
    temp3 = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        temp_values = [self.temp1, self.temp2, self.temp3]
        
class ConductividadMuestra(models.Model):
    cond1 = models.DecimalField(max_digits=10, decimal_places=2)
    cond2 = models.DecimalField(max_digits=10, decimal_places=2)
    cond3 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        cond_values = [self.cond1, self.cond2, self.cond3]
        
class TemperaturaAireMuestra(models.Model):
    tempAire1 = models.DecimalField(max_digits=5, decimal_places=2)
    tempAire2 = models.DecimalField(max_digits=5, decimal_places=2)
    tempAire3 = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        tempAire_values = [self.tempAire1, self.tempAire2, self.tempAire3]
        
class TiempoMuestra(models.Model):
    tiempo1 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo2 = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo3 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        tiempo_values = [self.tiempo1, self.tiempo2, self.tiempo3]
        
class VolumenMuestra(models.Model):
    volumen1 = models.DecimalField(max_digits=10, decimal_places=2)
    volumen2 = models.DecimalField(max_digits=10, decimal_places=2)
    volumen3 = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        volumen_values = [self.volumen1, self.volumen2, self.volumen3]

condiciones_choices = [
    ('soleado', 'Soleado'),
    ('nublado', 'Nublado'),
    ('medio_nublado', '1/2 Nublado'),
]

class MuestraHojaCampo(models.Model):
    numero = models.PositiveIntegerField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    ph = models.ForeignKey(PhMuestra, on_delete=models.CASCADE, null=True, blank=True)
    temperatura = models.ForeignKey(TemperaturaMuestra, on_delete=models.CASCADE, null=True, blank=True)
    conductividad = models.ForeignKey(ConductividadMuestra, on_delete=models.CASCADE, null=True, blank=True)
    # False para Ausente y True para Presente ⬇︎
    materiaFlotante = models.BooleanField(default=False)
    temperaturaAire = models.ForeignKey(TemperaturaAireMuestra, on_delete=models.CASCADE, null=True, blank=True)
    tiempoMuestra = models.ForeignKey(TiempoMuestra, on_delete=models.CASCADE, null=True, blank=True)
    volumenMuestra = models.ForeignKey(VolumenMuestra, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    olor = models.CharField(max_length=50, null=True, blank=True)
    # True para Si y False para No ⬇︎
    solido = models.BooleanField(default=False)
    # True para Si y False para No ⬇︎
    lluvia = models.BooleanField(default=False)
    condicion = models.CharField(max_length=50, choices=condiciones_choices, null=True, blank=True)
    
class HojaCampo(models.Model):
    # es lo mismo que el atributo identificacionPunto del modelo PuntoMuestreo, podria no ser necesario ⬇︎
    idMuestra = models.CharField(max_length=50)
    #siempre va a ser la norma NOM-002-SEMARNAT-1996/NMX-AA-003-1980 asi que podria evitarse ⬇︎
    normaReferencia = models.CharField(max_length=50)# debe ser un modelo
    # se refiere a si es Bajo techo o Intemperie/Cielo abierto ⬇︎
    condicionMuestreo = models.BooleanField(max_length=50)
    fechaMuestreo = models.DateField()
    muestraHojaCampo = models.ForeignKey(MuestraHojaCampo, on_delete=models.CASCADE, null=True, blank=True)
    observacion = models.TextField(max_length=255, null=True, blank=True)
    # Podria no ser necesario si se trae de una consulta ⬇︎
    muestreador = models.CharField(max_length=255, null=True, blank=True)
    supervisor = models.CharField(max_length=255, null=True, blank=True)
    aguaResidualInforme = models.ForeignKey('AguaResidualInforme', on_delete=models.CASCADE) 
                                                                           
## ------------- 6.- CROQUIS DE UBICACION -------------

class CroquisUbicacion(models.Model):
    # Podria no ser necesario si se trae de una consulta ⬇︎
    domicilio = models.CharField(max_length=255)
    croquis = models.ImageField(upload_to='croquis/', null=True, blank=True)
    comentario = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Croquis Id {self.id} - Domicilio: {self.domicilio}"
    
# ------------------- INFORME --------------------

class AguaResidualInforme(models.Model):
    OrdenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)
    CroquisUbicacion = models.ForeignKey(CroquisUbicacion, on_delete=models.CASCADE)

#  ------------- CADENA DE CUSTODIA -------------
class Preservador(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Matriz(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre

class Clave(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre

class Contenedor(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo + ' - ' + self.nombre
    
class Parametro(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo + ' - ' + self.descripcion
            
#agregar tabla para idfiltro
class Filtro(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.codigo + ' - ' + self.descripcion

class EstadoCustodia(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class CustodiaExterna(models.Model):
    contacto = models.CharField(max_length=50)
    puestoCargoContacto = models.CharField(max_length=50, null=True, blank=True)
    celularContacto = models.CharField(max_length=50, null=True, blank=True)
    correoContacto = models.EmailField(max_length=50, null=True, blank=True)
    puntosMuestreoAutorizados = models.CharField(max_length=50)
    modificacionOrdenTrabajo = models.BooleanField()
    observacionesModificacion = models.TextField(max_length=120, null=True, blank=True)
    asesoriaGestionAmbiental = models.BooleanField()
    muestreoRequerido = models.CharField(max_length=50)
    fechaFinal = models.DateField(null=True, blank=True)
    horaFinal = models.TimeField(null=True, blank=True)
    muestraCompuesta = models.BooleanField()
    idMuestraCompuesta = models.CharField(max_length=50, null=True, blank=True)
    muestraPuntual = models.BooleanField()
    idMuestraPuntual = models.CharField(max_length=50, null=True, blank=True)
    observaciones = models.TextField(max_length=325, null=True, blank=True)
    estado = models.ForeignKey(EstadoCustodia, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    ordenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return f"CustodiaExterna - {self.contacto}"

class Muestra(models.Model):
    #nomenclaruta de la identificacion de campo
    #nomenclatura-filtro-corrida-contenedor-numero de ducto
    identificacionCampo = models.CharField(max_length=50)
    fechaMuestreo = models.DateField()
    horaMuestreo = models.TimeField()
    volumenCantidad = models.CharField(max_length=50, null=True, blank=True)
    numeroContenedor = models.CharField(max_length=50)
    origenMuestra = models.CharField(max_length=50)
    idLaboratorio = models.CharField(max_length=50, null=True, blank=True)
    filtro = models.ForeignKey(Filtro, on_delete=models.CASCADE, null=True, blank=True)
    preservador = models.ManyToManyField(Preservador, through='PreservadorMuestra')
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    contenedor = models.ForeignKey(Contenedor, on_delete=models.CASCADE)
    parametro = models.ForeignKey(Parametro, on_delete=models.CASCADE)
    custodiaExterna = models.ForeignKey(CustodiaExterna, on_delete=models.CASCADE)

    def __str__(self):
        return f"Muestra - {self.identificacionCampo}"
    
class PreservadorMuestra(models.Model):
    preservador = models.ForeignKey(Preservador, on_delete=models.CASCADE)
    muestra = models.ForeignKey(Muestra, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"PreservadorMuestra - {self.preservador} - {self.muestra}"

#mover a la app del laboratorio
class RegistroCustodia(models.Model):
    custodiaExterna = models.ForeignKey(CustodiaExterna, on_delete=models.CASCADE)
    entregadoPor = models.CharField(max_length=100)
    fechaEntrega = models.DateField()
    horaEntrega = models.TimeField()
    recibidoPor = models.CharField(max_length=100)
    fechaEecepcion = models.DateField()
    horaRecepcion = models.TimeField()

    def __str__(self):
        return f"Registro de Custodia - Entregado por {self.entregadoPor} a {self.recibidoPor}"