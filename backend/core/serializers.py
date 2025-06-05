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
    class Meta:
        model = SitioMuestreo
        fields = '__all__'
        
class TipoDescargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDescarga
        fields = '__all__'
        
class AguaResidualTratamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AguaResidualTratamiento
        fields = '__all__'
        
class PuntoMuestreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoMuestreo
        fields = '__all__'
        
class MaterialUsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialUso
        fields = '__all__'
        
class RecipienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipiente
        fields = '__all__'
        
class PreservadorUtilizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreservadorUtilizado
        fields = '__all__'
        
class FrecuenciaMuestreoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = FrecuenciaMuestreo
        fields = '__all__'
        
class TipoAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAgua
        fields = '__all__'
        
class CuerpoReceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuerpoReceptor
        fields = '__all__'
        
class ProcedimientoMuestreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedimientoMuestreo
        fields = '__all__'
        
class PlanMuestreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMuestreo
        fields = '__all__'

class ProtocoloMuestreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtocoloMuestreo
        fields = '__all__'
        
class PhMuestraSerializer(serializers.ModelSerializer): 
    class Meta:
        model = PhMuestra
        fields = '__all__'
        
class TemperaturaMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaMuestra
        fields = '__all__'
        
class ConductividadMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConductividadMuestra
        fields = '__all__'
        
class TemperaturaAireMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaAireMuestra
        fields = '__all__'
        
class TiempoMuestraSerializer(serializers.ModelSerializer): 
    class Meta:
        model = TiempoMuestra
        fields = '__all__'
        
class VolumenMuestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolumenMuestra
        fields = '__all__'
        
class MuestraHojaCampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuestraHojaCampo
        fields = '__all__'
        
class HojaCampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HojaCampo
        fields = '__all__'
        
class CroquisUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CroquisUbicacion
        fields = '__all__'
        
class AguaResidualInformeSerializer(serializers.ModelSerializer):
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