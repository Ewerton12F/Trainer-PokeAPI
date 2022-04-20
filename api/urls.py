from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register('trainer', TrainerViewset, basename='trainer')
router.register('trainer/<int:pk>/pokemons', TrainerViewset, basename='pokemons')    
router.register('pokemon', PokemonViewset, basename='pokemon')
urlpatterns = router.urls


""" 
urlpatterns = [
    path('', include(c)),
#    path('trainer/', TrainerViewset.as_view({
#        'get': 'get_queryset',
#        'post': 'create',
#    })),
#    path('trainer/authenticate/', views.trainerAuth),
#    path('trainer/<int:pk>/', views.trainerId),
#    path('trainer/<int:pk>/pokemon/', views.pokemonList),
#    path('trainer/<int:pk>/pokemon/', views.pokemonCreate),
#    path('trainer/<int:pk>/pokemon/<int:pk>/', views.pokemonDelete),
]
 """