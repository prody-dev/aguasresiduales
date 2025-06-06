from rest_framework import serializers
from .models import Receptor, Estado, Metodo, Servicio, Empresa, OrdenTrabajo, OrdenTrabajoServicio
from .models import SitioMuestreo, TipoDescarga, AguaResidualTratamiento, PuntoMuestreo, MaterialUso
from .models import Recipiente, PreservadorUtilizado, FrecuenciaMuestreo, TipoAgua, CuerpoReceptor
from .models import ProcedimientoMuestreo, PlanMuestreo, ProtocoloMuestreo #aqui termina la primera hoja del formato
from .models import PhMuestra, TemperaturaMuestra, ConductividadMuestra, TemperaturaAireMuestra
from .models import TiempoMuestra, VolumenMuestra, MuestraHojaCampo, HojaCampo #aqui termina la segunda hoja del formato
from .models import CroquisUbicacion, AguaResidualInforme #aqui termina la tercera hoja del formato
from .models import Preservador, Matriz, Clave, Contenedor, Parametro, Prioridad, Filtro, EstadoCustodia
from .models import CustodiaExterna, Muestra, PreservadorMuestra, RegistroCustodia

class ReceptorSerializer(serializers.ModelSerializer):
    nombrePila = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre es obligatorio.',
            'blank': 'El nombre no puede estar en blanco.',
            'max_length': 'El nombre no puede exceder los 50 caracteres.'
        }
    )
    apPaterno = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El apellido paterno es obligatorio.',
            'blank': 'El apellido paterno no puede estar en blanco.',
            'max_length': 'El apellido paterno no puede exceder los 50 caracteres.'
        }
    )
    apMaterno = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El apellido materno no puede exceder los 50 caracteres.'
        }
    )
    correo = serializers.EmailField(
        required=False,
        allow_blank=True,
        max_length=100,
        error_messages={
            'max_length': 'El correo no puede exceder los 100 caracteres.',
            'invalid': 'Ingrese un correo electronico valido.'
        }
    )
    celular = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=10,
        error_messages={
            'max_length': 'El numero de celular no puede exceder los 10 caracteres.',
            'invalid': 'Ingrese un numero de celular valido.'
        }
    )

    class Meta:
        model = Receptor
        fields = ('id', 'nombrePila', 'apPaterno', 'apMaterno', 'correo', 'celular')

    def validate_celular(self, value):
        if value and not value.isdigit():
            raise serializers.ValidationError("El numero de celular debe contener solo digitos.")
        return value
             
class EstadoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del estado es obligatorio.',
            'blank': 'El nombre del estado no puede estar en blanco.',
            'max_length': 'El nombre del estado no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = Estado
        fields = '__all__'
        
class MetodoSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        error_messages={
            'min_value': 'El numero debe ser un entero positivo.',
            'invalid': 'Ingrese un numero válido.'
        }
    )
    codigo = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El código es obligatorio.',
            'blank': 'El código no puede estar vacío.',
            'max_length': 'El código no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = Metodo
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        error_messages={
            'min_value': 'El numero debe ser un entero positivo.',
            'invalid': 'Ingrese un numero válido.'
        }
    )
    nombreServicio = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'El nombre del servicio es obligatorio.',
            'blank': 'El nombre del servicio no puede estar vacío.',
            'max_length': 'El nombre del servicio no puede exceder los 255 caracteres.'
        }
    )
    metodo = serializers.PrimaryKeyRelatedField(
        queryset=Metodo.objects.all(),
        error_messages={
            'required': 'El metodo es obligatorio.',
            'does_not_exist': 'El método especificado no existe.',
            'incorrect_type': 'El método debe ser un ID válido.'
        }
    )

    class Meta:
        model = Servicio
        fields = '__all__'
        
class EmpresaSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        error_messages={
            'min_value': 'El numero debe ser un entero positivo.',
            'invalid': 'Ingrese un numero válido.'
        }
    )
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'El nombre de la empresa es obligatorio.',
            'blank': 'El nombre de la empresa no puede estar vacío.',
            'max_length': 'El nombre de la empresa no puede exceder los 255 caracteres.'
        }
    )
    codigoPostal = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=10,
        error_messages={
            'required': 'El código postal es obligatorio.',
            'blank': 'El código postal no puede estar vacío.',
            'max_length': 'El código postal no puede exceder los 10 caracteres.'
        }
    )
    ciudad = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'La ciudad es obligatoria.',
            'blank': 'La ciudad no puede estar vacía.',
            'max_length': 'La ciudad no puede exceder los 255 caracteres.'
        }
    )
    estado = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'El estado es obligatorio.',
            'blank': 'El estado no puede estar vacío.',
            'max_length': 'El estado no puede exceder los 255 caracteres.'
        }
    )
    colonia = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'La colonia es obligatoria.',
            'blank': 'La colonia no puede estar vacía.',
            'max_length': 'La colonia no puede exceder los 255 caracteres.'
        }
    )
    numeroExterior = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=24,
        error_messages={
            'max_length': 'El numero exterior no puede exceder los 24 caracteres.'
        }
    )
    calle = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=255,
        error_messages={
            'required': 'La calle es obligatoria.',
            'blank': 'La calle no puede estar vacía.',
            'max_length': 'La calle no puede exceder los 255 caracteres.'
        }
    )
    contacto = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El contacto no puede exceder los 255 caracteres.'
        }
    )
    telefono = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=20,
        error_messages={
            'max_length': 'El teléfono no puede exceder los 20 caracteres.',
            'invalid': 'Ingrese un numero de teléfono válido.'
        }
    )

    def validate_telefono(self, value):
        if value and not all(char.isalnum() or char.isspace() or char in ['-', '(', ')', 'ext'] for char in value):
            raise serializers.ValidationError("El teléfono solo puede contener dígitos, letras, espacios y caracteres como '-', '(', ')', o 'ext'.")
        return value

    class Meta:
        model = Empresa
        fields = '__all__'
        
class OrdenTrabajoSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        error_messages={
            'min_value': 'El número debe ser un entero positivo.',
            'invalid': 'Ingrese un número válido.'
        }
    )
    codigo = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El código no puede exceder los 255 caracteres.'
        }
    )
    nombreUsuario = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El nombre de usuario no puede exceder los 255 caracteres.'
        }
    )
    estado = serializers.PrimaryKeyRelatedField(
        queryset=Estado.objects.all(),
        error_messages={
            'required': 'El estado es obligatorio.',
            'does_not_exist': 'El estado especificado no existe.',
            'incorrect_type': 'El estado debe ser un ID válido.'
        }
    )
    receptor = serializers.PrimaryKeyRelatedField(
        queryset=Receptor.objects.all(),
        error_messages={
            'required': 'El receptor es obligatorio.',
            'does_not_exist': 'El receptor especificado no existe.',
            'incorrect_type': 'El receptor debe ser un ID válido.'
        }
    )
    empresa = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        error_messages={
            'required': 'La empresa es obligatoria.', 
            'does_not_exist': 'La empresa especificada no existe.',
            'incorrect_type': 'La empresa debe ser un ID válido.'
        }
    )

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'

class OrdenTrabajoServicioSerializer(serializers.ModelSerializer):
    ordenTrabajo = serializers.PrimaryKeyRelatedField(
        queryset=OrdenTrabajo.objects.all(),
        error_messages={
            'required': 'La orden de trabajo es obligatoria.',
            'does_not_exist': 'La orden de trabajo especificada no existe.',
            'incorrect_type': 'La orden de trabajo debe ser un ID válido.'
        }
    )
    servicio = serializers.PrimaryKeyRelatedField(
        queryset=Servicio.objects.all(),
        error_messages={
            'required': 'El servicio es obligatorio.',
            'does_not_exist': 'El servicio especificado no existe.',
            'incorrect_type': 'El servicio debe ser un ID válido.'
        }
    )
    cantidad = serializers.IntegerField(
        required=True,
        min_value=1,
        error_messages={
            'required': 'La cantidad es obligatoria.',
            'min_value': 'La cantidad debe ser un entero positivo.',
            'invalid': 'Ingrese una cantidad válida.'
        }
    )
    descripcion = serializers.CharField(
        required=False,
        allow_blank=True,
        error_messages={
            'invalid': 'Ingrese una descripción válida.'
        }
    )

    class Meta:
        model = OrdenTrabajoServicio
        fields = '__all__'
        
class SitioMuestreoSerializer(serializers.ModelSerializer):
    domicilio = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El domicilio no puede exceder los 255 caracteres.',
            'invalid': 'Ingrese un domicilio válido.'
        }
    )
    giroEmpresa = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El giro de la empresa no puede exceder los 255 caracteres.',
            'invalid': 'Ingrese un giro válido.'
        }
    )

    class Meta:
        model = SitioMuestreo
        fields = '__all__'
        
class TipoDescargaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del tipo de descarga es obligatorio.',
            'blank': 'El nombre del tipo de descarga no puede estar en blanco.',
            'max_length': 'El nombre del tipo de descarga no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = TipoDescarga
        fields = '__all__'
        
class AguaResidualTratamientoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del tratamiento es obligatorio.',
            'blank': 'El nombre del tratamiento no puede estar en blanco.',
            'max_length': 'El nombre del tratamiento no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = AguaResidualTratamiento
        fields = '__all__'
        
class PuntoMuestreoSerializer(serializers.ModelSerializer):
    identificacionPunto = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'La identificación del punto no puede exceder los 50 caracteres.',
            'invalid': 'Ingrese una identificación válida.'
        }
    )
    descripcionProceso = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'La descripción del proceso no puede exceder los 255 caracteres.',
            'invalid': 'Ingrese una descripción válida.'
        }
    )
    origenMuestra = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El origen de la muestra no puede exceder los 50 caracteres.',
            'invalid': 'Ingrese un origen válido.'
        }
    )
    aguaResidualOtro = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'Este campo no puede exceder los 50 caracteres.',
            'invalid': 'Ingrese un valor válido.'
        }
    )
    horasOperacion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'Las horas de operación no pueden exceder los 50 caracteres.',
            'invalid': 'Ingrese un valor válido.'
        }
    )
    horasDescarga = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'Las horas de descarga no pueden exceder los 50 caracteres.',
            'invalid': 'Ingrese un valor válido.'
        }
    )
    frecuenciaDescarga = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'La frecuencia de descarga no puede exceder los 50 caracteres.',
            'invalid': 'Ingrese un valor válido.'
        }
    )
    informacionProporcionada = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'La información proporcionada no puede exceder los 50 caracteres.',
            'invalid': 'Ingrese un valor válido.'
        }
    )
    aguaResidualTratamiento = serializers.PrimaryKeyRelatedField(
        queryset=AguaResidualTratamiento.objects.all(),
        required=False,
        allow_null=True,
        error_messages={
            'does_not_exist': 'El tratamiento seleccionado no existe.',
            'invalid': 'El tratamiento debe ser un ID válido.'
        }
    )
    tipoDescarga = serializers.PrimaryKeyRelatedField(
        queryset=TipoDescarga.objects.all(),
        required=False,
        allow_null=True,
        error_messages={
            'does_not_exist': 'El tipo de descarga seleccionado no existe.',
            'invalid': 'El tipo de descarga debe ser un ID válido.'
        }
    )

    class Meta:
        model = PuntoMuestreo
        fields = '__all__'
        
class MaterialUsoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del material es obligatorio.',
            'blank': 'El nombre del material no puede estar en blanco.',
            'max_length': 'El nombre del material no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = MaterialUso
        fields = '__all__'
        
class RecipienteSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del recipiente es obligatorio.',
            'blank': 'El nombre del recipiente no puede estar en blanco.',
            'max_length': 'El nombre del recipiente no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = Recipiente
        fields = '__all__'
        
class PreservadorUtilizadoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del preservador es obligatorio.',
            'blank': 'El nombre del preservador no puede estar en blanco.',
            'max_length': 'El nombre del preservador no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = PreservadorUtilizado
        fields = '__all__'
        
class FrecuenciaMuestreoSerializer(serializers.ModelSerializer):
    horaOperacion = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El campo "Hora de operación" es obligatorio.',
            'blank': 'La hora de operación no puede estar en blanco.',
            'max_length': 'La hora de operación no puede exceder los 50 caracteres.'
        }
    )
    numeroMuestrasSimples = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El número de muestras simples es obligatorio.',
            'blank': 'Este campo no puede estar en blanco.',
            'max_length': 'Este campo no puede exceder los 50 caracteres.'
        }
    )
    invervaloMinimo = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El intervalo mínimo es obligatorio.',
            'blank': 'El intervalo mínimo no puede estar en blanco.',
            'max_length': 'El intervalo mínimo no puede exceder los 50 caracteres.'
        }
    )
    invervaloMaximo = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El intervalo máximo es obligatorio.',
            'blank': 'El intervalo máximo no puede estar en blanco.',
            'max_length': 'El intervalo máximo no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = FrecuenciaMuestreo
        fields = '__all__'
        
class TipoAguaSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del tipo de agua es obligatorio.',
            'blank': 'El nombre del tipo de agua no puede estar en blanco.',
            'max_length': 'El nombre no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = TipoAgua
        fields = '__all__'
        
class CuerpoReceptorSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(
        required=True,
        allow_blank=False,
        max_length=50,
        error_messages={
            'required': 'El nombre del cuerpo receptor es obligatorio.',
            'blank': 'El nombre del cuerpo receptor no puede estar en blanco.',
            'max_length': 'El nombre del cuerpo receptor no puede exceder los 50 caracteres.'
        }
    )

    class Meta:
        model = CuerpoReceptor
        fields = '__all__'
        
class ProcedimientoMuestreoSerializer(serializers.ModelSerializer):
    parametroADeterminar = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El parámetro a determinar no puede exceder los 50 caracteres.'
        }
    )
    materialUso = serializers.PrimaryKeyRelatedField(
        queryset=MaterialUso.objects.all(),
        required=False,
        allow_null=True
    )
    recipiente = serializers.PrimaryKeyRelatedField(
        queryset=Recipiente.objects.all(),
        required=False,
        allow_null=True
    )
    preservadorUtilizado = serializers.PrimaryKeyRelatedField(
        queryset=PreservadorUtilizado.objects.all(),
        required=False,
        allow_null=True
    )
    tipoMuestreo = serializers.BooleanField(default=False)
    frecuenciaMuestreo = serializers.PrimaryKeyRelatedField(
        queryset=FrecuenciaMuestreo.objects.all(),
        required=False,
        allow_null=True
    )
    tipoAgua = serializers.PrimaryKeyRelatedField(
        queryset=TipoAgua.objects.all(),
        required=False,
        allow_null=True
    )
    tipoAguaOtro = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El campo "Tipo Agua Otro" no puede exceder los 50 caracteres.'
        }
    )
    cuerpoReceptor = serializers.PrimaryKeyRelatedField(
        queryset=CuerpoReceptor.objects.all(),
        required=False,
        allow_null=True
    )
    cuerpoReceptorOtro = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El campo "Cuerpo Receptor Otro" no puede exceder los 50 caracteres.'
        }
    )

    def validate(self, data):
        if data.get('tipoAgua') is None and not data.get('tipoAguaOtro'):
            raise serializers.ValidationError(
                "Debe especificar un tipo de agua o proporcionar un valor en 'Tipo Agua Otro'."
            )
        if data.get('cuerpoReceptor') is None and not data.get('cuerpoReceptorOtro'):
            raise serializers.ValidationError(
                "Debe especificar un cuerpo receptor o proporcionar un valor en 'Cuerpo Receptor Otro'."
            )
        return data

    class Meta:
        model = ProcedimientoMuestreo
        fields = '__all__'
        
class PlanMuestreoSerializer(serializers.ModelSerializer):
    inicial = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El campo "Inicial" no puede exceder los 50 caracteres.'
        }
    )
    fechaInicial = serializers.DateField(
        required=False,
        allow_null=True,
        error_messages={
            'invalid': 'Ingrese una fecha inicial válida.'
        }
    )
    final = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El campo "Final" no puede exceder los 50 caracteres.'
        }
    )
    fechaFinal = serializers.DateField(
        required=False,
        allow_null=True,
        error_messages={
            'invalid': 'Ingrese una fecha final válida.'
        }
    )
    observacion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'La observación no puede exceder los 255 caracteres.'
        }
    )
    class Meta:
        model = PlanMuestreo
        fields = '__all__'

    def validate(self, data):
        fecha_inicial = data.get('fechaInicial')
        fecha_final = data.get('fechaFinal')

        if fecha_inicial and fecha_final:
            if fecha_final < fecha_inicial:
                raise serializers.ValidationError({
                    'fechaFinal': 'La fecha final no puede ser anterior a la fecha inicial.'
                })

        return data

class ProtocoloMuestreoSerializer(serializers.ModelSerializer):
    sitioMuestreo = serializers.PrimaryKeyRelatedField(
        queryset=SitioMuestreo.objects.all(),
        required=False,
        allow_null=True
    )
    puntoMuestreo = serializers.PrimaryKeyRelatedField(
        queryset=PuntoMuestreo.objects.all(),
        required=False,
        allow_null=True
    )
    procedimientoMuestreo = serializers.PrimaryKeyRelatedField(
        queryset=ProcedimientoMuestreo.objects.all(),
        required=False,
        allow_null=True
    )
    planMuestreo = serializers.PrimaryKeyRelatedField(
        queryset=PlanMuestreo.objects.all(),
        required=False,
        allow_null=True
    )
    aguaResidualInforme = serializers.PrimaryKeyRelatedField(
        queryset=AguaResidualInforme.objects.all(),
        required=True,
        error_messages={
            'required': 'El informe de agua residual es obligatorio.',
            'does_not_exist': 'El informe de agua residual especificado no existe.',
            'incorrect_type': 'Tipo incorrecto. Se esperaba un ID válido para el informe de agua residual.'
        }
    )

    class Meta:
        model = ProtocoloMuestreo
        fields = '__all__'
        
class PhMuestraSerializer(serializers.ModelSerializer):
    ph1 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de pH1 debe ser un número decimal válido.',
            'max_digits': 'El valor de pH1 excede el número máximo de dígitos permitidos.',
        }
    )
    ph2 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de pH2 debe ser un número decimal válido.',
            'max_digits': 'El valor de pH2 excede el número máximo de dígitos permitidos.',
        }
    )
    ph3 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de pH3 debe ser un número decimal válido.',
            'max_digits': 'El valor de pH3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = PhMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            value = data.get(f'ph{i}')
            if value is not None and (value < 0 or value >= 30):
                raise serializers.ValidationError({f'ph{i}': f'El valor de pH{i} debe estar entre 0 y 14.'})
        return data
        
class TemperaturaMuestraSerializer(serializers.ModelSerializer):
    temp1 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura 1 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura 1 excede el número máximo de dígitos permitidos.',
        }
    )
    temp2 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura 2 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura 2 excede el número máximo de dígitos permitidos.',
        }
    )
    temp3 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura 3 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura 3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = TemperaturaMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            valor = data.get(f'temp{i}')
            if valor is not None and (valor < -10 or valor > 100):
                raise serializers.ValidationError({
                    f'temp{i}': f'El valor de Temperatura {i} debe estar entre -10 y 100 grados Celsius.'
                })
        return data
        
class ConductividadMuestraSerializer(serializers.ModelSerializer):
    cond1 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Conductividad 1 debe ser un número decimal válido.',
            'max_digits': 'El valor de Conductividad 1 excede el número máximo de dígitos permitidos.',
        }
    )
    cond2 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Conductividad 2 debe ser un número decimal válido.',
            'max_digits': 'El valor de Conductividad 2 excede el número máximo de dígitos permitidos.',
        }
    )
    cond3 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Conductividad 3 debe ser un número decimal válido.',
            'max_digits': 'El valor de Conductividad 3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = ConductividadMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            valor = data.get(f'cond{i}')
            if valor is not None and (valor < 0 or valor > 100000):
                raise serializers.ValidationError({
                    f'cond{i}': f'El valor de Conductividad {i} debe estar entre 0 y 100,000 µS/cm.'
                })
        return data
        
class TemperaturaAireMuestraSerializer(serializers.ModelSerializer):
    tempAire1 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura Aire 1 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura Aire 1 excede el número máximo de dígitos permitidos.',
        }
    )
    tempAire2 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura Aire 2 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura Aire 2 excede el número máximo de dígitos permitidos.',
        }
    )
    tempAire3 = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Temperatura Aire 3 debe ser un número decimal válido.',
            'max_digits': 'El valor de Temperatura Aire 3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = TemperaturaAireMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            valor = data.get(f'tempAire{i}')
            if valor is not None and (valor < -20 or valor > 60):
                raise serializers.ValidationError({
                    f'tempAire{i}': f'El valor de Temperatura Aire {i} debe estar entre -20 y 60 °C.'
                })
        return data
        
class TiempoMuestraSerializer(serializers.ModelSerializer):
    tiempo1 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Tiempo 1 debe ser un número decimal válido.',
            'max_digits': 'El valor de Tiempo 1 excede el número máximo de dígitos permitidos.',
        }
    )
    tiempo2 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Tiempo 2 debe ser un número decimal válido.',
            'max_digits': 'El valor de Tiempo 2 excede el número máximo de dígitos permitidos.',
        }
    )
    tiempo3 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Tiempo 3 debe ser un número decimal válido.',
            'max_digits': 'El valor de Tiempo 3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = TiempoMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            valor = data.get(f'tiempo{i}')
            if valor is not None and (valor < 0 or valor > 86400):
                raise serializers.ValidationError({
                    f'tiempo{i}': f'El tiempo {i} debe estar entre 0 y 86,400 segundos (24 horas).'
                })
        return data
        
class VolumenMuestraSerializer(serializers.ModelSerializer):
    volumen1 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Volumen 1 debe ser un número decimal válido.',
            'max_digits': 'El valor de Volumen 1 excede el número máximo de dígitos permitidos.',
        }
    )
    volumen2 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Volumen 2 debe ser un número decimal válido.',
            'max_digits': 'El valor de Volumen 2 excede el número máximo de dígitos permitidos.',
        }
    )
    volumen3 = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        error_messages={
            'invalid': 'El valor de Volumen 3 debe ser un número decimal válido.',
            'max_digits': 'El valor de Volumen 3 excede el número máximo de dígitos permitidos.',
        }
    )

    class Meta:
        model = VolumenMuestra
        fields = '__all__'

    def validate(self, data):
        for i in range(1, 4):
            valor = data.get(f'volumen{i}')
            if valor is not None and (valor < 0 or valor > 10000):
                raise serializers.ValidationError({
                    f'volumen{i}': f'El volumen {i} debe estar entre 0 y 10,000 ml.'
                })
        return data
        
class MuestraHojaCampoSerializer(serializers.ModelSerializer):
    numero = serializers.IntegerField(
        required=False,
        allow_null=True,
        min_value=1,
        error_messages={
            'invalid': 'El número debe ser un entero válido.',
            'min_value': 'El número debe ser mayor a 0.',
        }
    )
    hora = serializers.TimeField(
        required=False,
        allow_null=True,
        error_messages={
            'invalid': 'La hora debe tener el formato HH:MM:SS.',
        }
    )
    color = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El color no puede exceder los 50 caracteres.',
        }
    )
    olor = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=50,
        error_messages={
            'max_length': 'El olor no puede exceder los 50 caracteres.',
        }
    )
    condicion = serializers.ChoiceField(
        choices=MuestraHojaCampo._meta.get_field('condicion').choices,
        required=False,
        allow_null=True,
        error_messages={
            'invalid_choice': 'La condición seleccionada no es válida.',
        }
    )

    class Meta:
        model = MuestraHojaCampo
        fields = '__all__'

    def validate(self, data):
        # Validación cruzada opcional: si hay ph, debe haber temperatura y viceversa
        if data.get('ph') and not data.get('temperatura'):
            raise serializers.ValidationError({
                'temperatura': 'Debe registrar la temperatura si se registra el pH.'
            })
        if data.get('temperatura') and not data.get('ph'):
            raise serializers.ValidationError({
                'ph': 'Debe registrar el pH si se registra la temperatura.'
            })
        return data
        
class HojaCampoSerializer(serializers.ModelSerializer):
    idMuestra = serializers.CharField(
        required=True,
        max_length=50,
        allow_blank=False,
        error_messages={
            'required': 'El ID de la muestra es obligatorio.',
            'blank': 'El ID de la muestra no puede estar en blanco.',
            'max_length': 'El ID de la muestra no puede exceder los 50 caracteres.'
        }
    )
    normaReferencia = serializers.CharField(
        required=True,
        max_length=50,
        allow_blank=False,
        error_messages={
            'required': 'La norma de referencia es obligatoria.',
            'blank': 'La norma de referencia no puede estar en blanco.',
            'max_length': 'La norma no puede exceder los 50 caracteres.'
        }
    )
    condicionMuestreo = serializers.BooleanField(
        required=True,
        error_messages={
            'invalid': 'El valor para la condición de muestreo debe ser verdadero o falso.',
        }
    )
    fechaMuestreo = serializers.DateField(
        required=True,
        error_messages={
            'required': 'La fecha de muestreo es obligatoria.',
            'invalid': 'Ingrese una fecha válida con el formato YYYY-MM-DD.'
        }
    )
    observacion = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'La observación no puede exceder los 255 caracteres.'
        }
    )
    muestreador = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El nombre del muestreador no puede exceder los 255 caracteres.'
        }
    )
    supervisor = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El nombre del supervisor no puede exceder los 255 caracteres.'
        }
    )

    class Meta:
        model = HojaCampo
        fields = '__all__'
        
class CroquisUbicacionSerializer(serializers.ModelSerializer):
    domicilio = serializers.CharField(
        required=True,
        max_length=255,
        allow_blank=False,
        error_messages={
            'required': 'El domicilio es obligatorio.',
            'blank': 'El domicilio no puede estar en blanco.',
            'max_length': 'El domicilio no puede exceder los 255 caracteres.'
        }
    )
    comentario = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
        error_messages={
            'max_length': 'El comentario no puede exceder los 255 caracteres.'
        }
    )
    croquis = serializers.ImageField(
        required=False,
        allow_null=True,
        error_messages={
            'invalid': 'El archivo del croquis debe ser una imagen válida.'
        }
    )

    class Meta:
        model = CroquisUbicacion
        fields = '__all__'
        
class AguaResidualInformeSerializer(serializers.ModelSerializer):
    OrdenTrabajo = serializers.PrimaryKeyRelatedField(
        queryset=OrdenTrabajo.objects.all(),
        error_messages={
            'required': 'El campo Orden de Trabajo es obligatorio.',
            'does_not_exist': 'La Orden de Trabajo especificada no existe.',
            'incorrect_type': 'El valor proporcionado no es válido para una Orden de Trabajo.'
        }
    )
    CroquisUbicacion = serializers.PrimaryKeyRelatedField(
        queryset=CroquisUbicacion.objects.all(),
        error_messages={
            'required': 'El campo Croquis de Ubicación es obligatorio.',
            'does_not_exist': 'El Croquis de Ubicación especificado no existe.',
            'incorrect_type': 'El valor proporcionado no es válido para un Croquis de Ubicación.'
        }
    )

    class Meta:
        model = AguaResidualInforme
        fields = '__all__'
        
class PreservadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preservador
        fields = '__all__'
        
class MatrizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriz
        fields = '__all__'
        
class ClaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clave
        fields = '__all__'
        
class ContenedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenedor
        fields = '__all__'
        
class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = '__all__'
        
class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prioridad
        fields = '__all__'
        
class FiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filtro
        fields = '__all__'
        
class EstadoCustodiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCustodia
        fields = '__all__'
        
class CustodiaExternaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustodiaExterna
        fields = '__all__'
        
class MuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muestra
        fields = '__all__'
        
class PreservadorMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreservadorMuestra
        fields = '__all__'
        
class RegistroCustodiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCustodia
        fields = '__all__'