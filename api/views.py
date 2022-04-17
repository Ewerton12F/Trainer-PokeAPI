from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets, status
from .serializers import *
from .models import *
import requests

# Create your views here.
""" 
# 4V ###########################################################################
class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class PokemonViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        trainer = Trainer.objects.get(id=params['pk'])
        serializer = TrainerSerializer(trainer, many=False)
        print(kwargs)
        return Response(serializer.data)
"""
     
# 5V ###########################################################################
class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    ############################### LIST TRAINER ###############################
    def get_queryset(self):
        """ 200 - OK
        [
            {
                "id": 3,
                "nickname": "ash",
                "first_name": "Ash",
                "last_name": "Kutchum",
                "team": "Team Valor",
                "pokemons_owned": 3
            }
        ]
        """

        """ 500 - Internal server error
        {
            "code": 0,
            "type": "string",
            "message": "string"
        }
        """
        trainer = Trainer.objects.all()
        return trainer
    ##############################/ LIST TRAINER /##############################

    ############################ GET TRAINER BY ID #############################
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        trainer = Trainer.objects.get(id=params['pk'])
        serializer = TrainerSerializer(trainer, many=False)
        return Response(serializer.data)
    ###########################/ GET TRAINER BY ID /############################

    ############################## CREATE TRAINER ##############################
    """ Creates a new trainer
        {
            "nickname": "ash",
            "first_name": "Ash",
            "last_name": "Kutchum",
            "email": "ash@pokemon.com",
            "password": "coxinha123",
            "team": "Team Valor"
        }
    """

    def create(self, request, *args, **kwargs):
        serializer = TrainerSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            """ 201	- Created
            {
                "id": 3,
                "nickname": "ash",
                "first_name": "Ash",
                "last_name": "Kutchum",
                "team": "Team Valor",
                "pokemons_owned": 3
            }
            """
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        """ 400 - Bad request
        {
            "code": 0,
            "type": "string",
            "message": "string"
        }
        """
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """ 500 - Internal server error
    {
        "code": 0,
        "type": "string",
        "message": "string"
    }
    """
    #############################/ CREATE TRAINER /#############################

    ############################## CREATE POKEMON ##############################
    @action(detail=True, methods=["GET"])
    def pokemons(self, request, id=None):

        # POKEAPI
        def pokeapi(name): 
            api = f'https://pokeapi.co/api/v2/pokemon/{name}'
            get_response = requests.get(api)
            pokemon = get_response.json()
            return pokemon
        
        pokemon_api_data = pokeapi(request.data['name'])
        print(pokemon_api_data)

        trainer = self.get_object()
        pokemons = Pokemon.objects.filter(trainer=trainer)
        serializer = PokemonSerializer(pokemons, many=True)
        return Response(serializer.data, status=200)
    #############################/ CREATE POKEMON /#############################


""" 
# 3V ###########################################################################
class PokemonViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    # LIST POKEMONS
    def get_queryset(self):
        pokemon = Pokemon.objects.all()
        return pokemon
    
    # POKEMON BY ID
    def retrieve(self, request, *args, **kwargs):
        pokemon = Pokemon.objects.get(id=kwargs['pk'])
        serializer = PokemonSerializer(pokemon, many=False)
        return Response(serializer.data)

    # CREATE POKEMON
    def create(self, request, *args, **kwargs):
        # POKEAPI
        def pokeapi(name): 
            api = f'https://pokeapi.co/api/v2/pokemon/{name}'
            get_response = requests.get(api)
            pokemon = get_response.json()
            return pokemon
        
        pokemon_api_data = pokeapi(request.data['name'])

        #print(pokemon_api_data)

        new_pokemon = Pokemon.objects.create(
            name = request.data['name'],
            base_experience = pokemon_api_data['base_experience'],
            height = pokemon_api_data['height'],
            is_default = pokemon_api_data['is_default'],
            order = pokemon_api_data['order'],
            weight = pokemon_api_data['weight'], 
        )

        new_pokemon.save()
        
        print(new_pokemon)
        
        serializer = PokemonSerializer(data=request.data, many=False)

        ''' 
            PokemonSerializer(
                data=<QueryDict: {
                    'csrfmiddlewaretoken': 
                        ['07beeqa6gMkMjpLfYzi4WY2VwYsOlw0W4MmPbNbaGvJJK4RAyAZHkgq1mPbpqCT7'],
                        'name': ['pikachu'], 
                        'base_experience': [''], 
                        'height': [''], 
                        'order': [''], 
                        'weight': [''], 
                        'trainer_id': ['1']}>):
            id = IntegerField(read_only=True)
            name = CharField(allow_blank=True, max_length=50, required=False)
            base_experience = IntegerField(required=False)
            height = IntegerField(required=False)
            is_default = BooleanField(required=False)
            order = IntegerField(required=False)
            weight = IntegerField(required=False)
            trainer_id = PrimaryKeyRelatedField(allow_null=True, queryset=Trainer.objects.all(), required=False)
        '''

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
################################################################################
"""

""" 
# 2V ###########################################################################
@api_view(['GET', 'POST'])
def trainer(request):
    if request.method == 'GET':
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def trainerId(request, pk):
    trainer = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(trainer, many=False)
    return Response(serializer.data)
################################################################################
"""
"""
# 1V ###########################################################################
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List Trainers':'/trainer/',
        'Create Trainer':'/trainer/',
        'Authentication':'/trainer/authenticate/',
        'Trainer by ID':'/trainer/<int:pk>/',
        'List Pokemons':'/trainer/<int:pk>/pokemon',
        'Create Pokemon':'/trainer/<int:pk>/pokemon',
        'Pokemon by ID':'/trainer/<int:pk>/pokemon/<int:pk>',
        'Deletes Pokemon':'/trainer/<int:pk>/pokemon/<int:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def trainerList(request):
    trainers = Trainer.objects.all()
    serializer = TrainerSerializer(trainers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def trainerCreate(request):
    serializer = TrainerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def trainerAuth(request):
    pass

@api_view(['GET'])
def trainerId(request, pk):
    trainers = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(trainers, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def pokemonList(request, pk):
    trainers = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(trainers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def pokemonCreate(request, pk):
    trainers = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(instance=trainers, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def pokemonId(request, pk):
    trainers = Trainer.objects.get(id=pk)
    serializer = TrainerSerializer(trainers, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def pokemonDelete(request, pk):
    trainers = Trainer.objects.get(id=pk)
    trainers.delete() 
################################################################################
"""