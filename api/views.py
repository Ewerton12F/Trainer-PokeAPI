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
# 4V /##########################################################################
"""

# 5V ###########################################################################
class TrainerViewset(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    ############################### LIST TRAINER ###############################
    '''
    SUCCESS
    '''
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
        trainer = Trainer.objects.all()
        return trainer
    """ 500 - Internal server error
    {
        "code": 0,
        "type": "string",
        "message": "string"
    }
    """
    ##############################/ LIST TRAINER /##############################

    ############################ GET TRAINER BY ID #############################
    '''
    SUCCESS
    '''
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        trainer = Trainer.objects.get(id=params['pk'])
        serializer = TrainerSerializer(trainer, many=False)
        return Response(serializer.data)
    ###########################/ GET TRAINER BY ID /############################

    ############################## CREATE TRAINER ##############################
    '''
    SUCCESS
    '''
    def create(self, request, *args, **kwargs):
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
    @action(detail=True, methods=["POST"])
    def pokemons(self, request, id=None):

        # POKEAPI ##############################################################
        '''
        SUCCESS
        '''
        def pokeapi(name): 
            api = f'https://pokeapi.co/api/v2/pokemon/{name}'
            get_response = requests.get(api)
            pokemon = get_response.json()
            return pokemon
        # POKEAPI /#############################################################
        pokemon_api_data = pokeapi(request.data['name'])
        print(pokemon_api_data)

        # CREATE POKEMON + SAVING + RESPONSE ###################################
        '''
        ERROR:
        IT COULDN'T CREATE A INSTANCE OF POKÉMON OBJECT
        '''
        trainer = self.get_object()
        pokemons = Pokemon.objects.filter(trainer=trainer)
        serializer = PokemonSerializer(pokemons, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # CREATE POKEMON + SAVING + RESPONSE /##################################
    #############################/ CREATE POKEMON /#############################

# 5V /##########################################################################

# 3V ###########################################################################
class PokemonViewset(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    # LIST POKEMONS
    '''
    SUCCESS
    '''
    def get_queryset(self):
        pokemon = Pokemon.objects.all()
        return pokemon
    
    # POKEMON BY ID
    '''
    SUCCESS
    '''
    def retrieve(self, request, *args, **kwargs):
        pokemon = Pokemon.objects.get(id=kwargs['pk'])
        serializer = PokemonSerializer(pokemon, many=False)
        return Response(serializer.data)

    # CREATE POKEMON
    '''
    SUCCESS
    '''
    def create(self, request, *args, **kwargs):

        # POKEAPI ##############################################################
        '''
        SUCCESS
        '''
        def pokeapi(name): 
            api = f'https://pokeapi.co/api/v2/pokemon/{name}'
            get_response = requests.get(api)
            pokemon = get_response.json()
            return pokemon
        # POKEAPI /#############################################################
        
        # POKEAPI CONSOLE PRINT /###############################################
        '''
        SUCCESS
        '''
        pokemon_api_data = pokeapi(request.data['name'])
        
        print(f"---Pokemon: {request.data['name']}")
        print(f"---Base Experience: {pokemon_api_data['base_experience']}")
        print(f"---Height: {pokemon_api_data['height']}")
        print(f"---Is default: {pokemon_api_data['is_default']}")
        print(f"---Order: {pokemon_api_data['order']}")
        print(f"---Weight: {pokemon_api_data['weight']}")
        # POKEAPI CONSOLE PRINT /###############################################

        # POKEAPI OBJECT CONSTRUCTION /#########################################
        '''
        ERROR:
        IT COULDN'T CREATE AN OBJECT
        '''
        new_pokemon = Pokemon.objects.create(
            name = request.data['name'],
            base_experience = pokemon_api_data['base_experience'],
            height = pokemon_api_data['height'],
            is_default = pokemon_api_data['is_default'],
            order = pokemon_api_data['order'],
            weight = pokemon_api_data['weight'], 
        )
        new_pokemon.save()
        # POKEAPI OBJECT CONSTRUCTION /#########################################
        
        # SERIALIZE ############################################################
        '''
        ERROR:
        IT COULDN'T SERIALIZE
        '''
        serializer = PokemonSerializer(new_pokemon, many=False)
        # SERIALIZE /###########################################################

        # SAVING + RESPONSE ####################################################
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # SAVING + RESPONSE /###################################################
# 3V /##########################################################################

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
# 2V /##########################################################################
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
# 1V /##########################################################################
"""