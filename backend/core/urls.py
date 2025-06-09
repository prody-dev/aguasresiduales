from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReceptorViewSet, EstadoViewSet, MetodoViewSet, ServicioViewSet, EmpresaViewSet
from .views import OrdenTrabajoViewSet, OrdenTrabajoServicioViewSet, SitioMuestreoViewSet, TipoDescargaViewSet
from .views import AguaResidualTratamientoViewSet, PuntoMuestreoViewSet, MaterialUsoViewSet, RecipienteViewSet
from .views import PreservadorUtilizadoViewSet, FrecuenciaMuestreoViewSet, TipoAguaViewSet, CuerpoReceptorViewSet
from .views import ProcedimientoMuestreoViewSet, PlanMuestreoViewSet, ProtocoloMuestreoViewSet, PhMuestraViewSet
from .views import TemperaturaMuestraViewSet, ConductividadMuestraViewSet, TemperaturaAireMuestraViewSet, VolumenMuestraViewSet
from .views import MuestraHojaCampoViewSet, HojaCampoViewSet, CroquisUbicacionViewSet, AguaResidualInformeViewSet
from .views import PreservadorViewSet, MatrizViewSet, ClaveViewSet, ContenedorViewSet, ParametroViewSet, PrioridadViewSet
from .views import FiltroViewSet, EstadoCustodiaViewSet, CustodiaExternaViewSet, MuestraViewSet, PreservadorMuestraViewSet
from .views import RegistroCustodiaViewSet

router = DefaultRouter()

router.register(r'receptor', ReceptorViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'metodo', MetodoViewSet)
router.register(r'servicio', ServicioViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'ordentrabajo', OrdenTrabajoViewSet)
router.register(r'ordentrabajoservicio', OrdenTrabajoServicioViewSet)
router.register(r'sitiomuestreo', SitioMuestreoViewSet)
router.register(r'tipodescarga', TipoDescargaViewSet)
router.register(r'aguaresidualtratamiento', AguaResidualTratamientoViewSet)
router.register(r'puntomuestreo', PuntoMuestreoViewSet)
router.register(r'materialuso', MaterialUsoViewSet)
router.register(r'recipiente', RecipienteViewSet)
router.register(r'preservadorutilizado', PreservadorUtilizadoViewSet)
router.register(r'frecuenciamuestreo', FrecuenciaMuestreoViewSet)
router.register(r'tipoagua', TipoAguaViewSet)
router.register(r'cuerporeceptor', CuerpoReceptorViewSet)
router.register(r'procedimientomuestreo', ProcedimientoMuestreoViewSet)
router.register(r'planmuestreo', PlanMuestreoViewSet)
router.register(r'protocolomuestreo', ProtocoloMuestreoViewSet)
router.register(r'phmuestra', PhMuestraViewSet)
router.register(r'temperaturamuestra', TemperaturaMuestraViewSet)
router.register(r'conductividadmuestra', ConductividadMuestraViewSet)
router.register(r'temperaturaairemuestra', TemperaturaAireMuestraViewSet)
router.register(r'volumenmuestra', VolumenMuestraViewSet)
router.register(r'muestrahojacampo', MuestraHojaCampoViewSet)
router.register(r'hojacampo', HojaCampoViewSet)
router.register(r'croquisubicacion', CroquisUbicacionViewSet)
router.register(r'aguaresidualinforme', AguaResidualInformeViewSet)
router.register(r'preservador', PreservadorViewSet)
router.register(r'matriz', MatrizViewSet)
router.register(r'clave', ClaveViewSet)
router.register(r'contenedor', ContenedorViewSet)
router.register(r'parametro', ParametroViewSet)
router.register(r'prioridad', PrioridadViewSet)
router.register(r'filtro', FiltroViewSet)
router.register(r'estadocustodia', EstadoCustodiaViewSet)
router.register(r'custodiaexterna', CustodiaExternaViewSet)
router.register(r'muestra', MuestraViewSet)
router.register(r'preservadormuestra', PreservadorMuestraViewSet)
router.register(r'registrocustodia', RegistroCustodiaViewSet)

urlpatterns = [
    path('', include(router.urls))
]