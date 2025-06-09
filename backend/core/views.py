from django.shortcuts import render
from rest_framework import viewsets, status

from .models import Receptor, Estado, Metodo, Servicio, Empresa, OrdenTrabajo, OrdenTrabajoServicio
from .models import OrdenTrabajoServicio, SitioMuestreo, TipoDescarga, AguaResidualTratamiento
from .models import PuntoMuestreo, MaterialUso, Recipiente, PreservadorUtilizado, FrecuenciaMuestreo
from .models import TipoAgua, CuerpoReceptor, ProcedimientoMuestreo, PlanMuestreo, ProtocoloMuestreo
from .models import PhMuestra, TemperaturaMuestra, ConductividadMuestra, TemperaturaAireMuestra
from .models import VolumenMuestra, MuestraHojaCampo, HojaCampo, CroquisUbicacion, AguaResidualInforme
from .models import Preservador, Matriz, Clave, Contenedor, Parametro, Prioridad, Filtro
from .models import EstadoCustodia, CustodiaExterna, Muestra, PreservadorMuestra, RegistroCustodia

from .serializers import ReceptorSerializer, EstadoSerializer, MetodoSerializer, ServicioSerializer
from .serializers import EmpresaSerializer, OrdenTrabajoSerializer, OrdenTrabajoServicioSerializer
from .serializers import SitioMuestreoSerializer, TipoDescargaSerializer, AguaResidualTratamientoSerializer
from .serializers import PuntoMuestreoSerializer, MaterialUsoSerializer, RecipienteSerializer
from .serializers import PreservadorUtilizadoSerializer, FrecuenciaMuestreoSerializer, TipoAguaSerializer
from .serializers import CuerpoReceptorSerializer, ProcedimientoMuestreoSerializer, PlanMuestreoSerializer
from .serializers import ProtocoloMuestreoSerializer, PhMuestraSerializer, TemperaturaMuestraSerializer
from .serializers import ConductividadMuestraSerializer, TemperaturaAireMuestraSerializer
from .serializers import VolumenMuestraSerializer, MuestraHojaCampoSerializer, HojaCampoSerializer
from .serializers import CroquisUbicacionSerializer, AguaResidualInformeSerializer, PreservadorSerializer
from .serializers import MatrizSerializer, ClaveSerializer, ContenedorSerializer, ParametroSerializer
from .serializers import PrioridadSerializer, FiltroSerializer, EstadoCustodiaSerializer
from .serializers import CustodiaExternaSerializer, MuestraSerializer, PreservadorMuestraSerializer
from .serializers import RegistroCustodiaSerializer

class ReceptorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer
    
class EstadoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
class MetodoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Metodo.objects.all()
    serializer_class = MetodoSerializer
    
class ServicioViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    
class EmpresaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    
class OrdenTrabajoServicioViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = OrdenTrabajoServicio.objects.all()
    serializer_class = OrdenTrabajoServicioSerializer
    
class SitioMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = SitioMuestreo.objects.all()
    serializer_class = SitioMuestreoSerializer
    
class TipoDescargaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = TipoDescarga.objects.all()
    serializer_class = TipoDescargaSerializer
    
class AguaResidualTratamientoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = AguaResidualTratamiento.objects.all()
    serializer_class = AguaResidualTratamientoSerializer
    
class PuntoMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = PuntoMuestreo.objects.all()
    serializer_class = PuntoMuestreoSerializer
    
class MaterialUsoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = MaterialUso.objects.all()
    serializer_class = MaterialUsoSerializer
    
class RecipienteViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Recipiente.objects.all()
    serializer_class = RecipienteSerializer
    
class PreservadorUtilizadoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = PreservadorUtilizado.objects.all()
    serializer_class = PreservadorUtilizadoSerializer
    
class FrecuenciaMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = FrecuenciaMuestreo.objects.all()
    serializer_class = FrecuenciaMuestreoSerializer
    
class TipoAguaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = TipoAgua.objects.all()
    serializer_class = TipoAguaSerializer
    
class CuerpoReceptorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = CuerpoReceptor.objects.all()
    serializer_class = CuerpoReceptorSerializer
    
class ProcedimientoMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = ProcedimientoMuestreo.objects.all()
    serializer_class = ProcedimientoMuestreoSerializer
    
class PlanMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = PlanMuestreo.objects.all()
    serializer_class = PlanMuestreoSerializer
    
class ProtocoloMuestreoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = ProtocoloMuestreo.objects.all()
    serializer_class = ProtocoloMuestreoSerializer
    
class PhMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = PhMuestra.objects.all()
    serializer_class = PhMuestraSerializer
    
class TemperaturaMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = TemperaturaMuestra.objects.all()
    serializer_class = TemperaturaMuestraSerializer
    
class ConductividadMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = ConductividadMuestra.objects.all()
    serializer_class = ConductividadMuestraSerializer
    
class TemperaturaAireMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = TemperaturaAireMuestra.objects.all()
    serializer_class = TemperaturaAireMuestraSerializer
    
class VolumenMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = VolumenMuestra.objects.all()
    serializer_class = VolumenMuestraSerializer
    
class MuestraHojaCampoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = MuestraHojaCampo.objects.all()
    serializer_class = MuestraHojaCampoSerializer
    
class HojaCampoViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = HojaCampo.objects.all()
    serializer_class = HojaCampoSerializer
    
class CroquisUbicacionViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = CroquisUbicacion.objects.all()
    serializer_class = CroquisUbicacionSerializer
    
class AguaResidualInformeViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = AguaResidualInforme.objects.all()
    serializer_class = AguaResidualInformeSerializer
    
class PreservadorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Preservador.objects.all()
    serializer_class = PreservadorSerializer
    
class MatrizViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Matriz.objects.all()
    serializer_class = MatrizSerializer
    
class ClaveViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer
    
class ContenedorViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Contenedor.objects.all()
    serializer_class = ContenedorSerializer
    
class ParametroViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer
    
class PrioridadViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Prioridad.objects.all()
    serializer_class = PrioridadSerializer
    
class FiltroViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Filtro.objects.all()
    serializer_class = FiltroSerializer
    
class EstadoCustodiaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = EstadoCustodia.objects.all()
    serializer_class = EstadoCustodiaSerializer
    
class CustodiaExternaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = CustodiaExterna.objects.all()
    serializer_class = CustodiaExternaSerializer
    
class MuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Muestra.objects.all()
    serializer_class = MuestraSerializer
    
class PreservadorMuestraViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = PreservadorMuestra.objects.all()
    serializer_class = PreservadorMuestraSerializer
    
class RegistroCustodiaViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = RegistroCustodia.objects.all()
    serializer_class = RegistroCustodiaSerializer
    