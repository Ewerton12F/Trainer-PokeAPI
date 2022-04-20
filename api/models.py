from re import T
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
    
class Trainer(models.Model):  
    '''
    Trainer:
        type: object
        properties:
            id:
                type: integer
                format: int64
                readOnly: true
                example: 3
            nickname:
                type: string
                example: ash
            first_name:
                type: string
                example: Ash
            last_name:
                type: string
                example: Kutchum
            email:
                type: string
                writeOnly: true
                example: ash@pokemon.com
            password:
                type: string
                writeOnly: true
                example: coxinha123
            team:
                type: string
                enum:
                - Team Valor
                - Team Instinct
                - Team Mystic
            pokemons_owned:
                type: integer
                format: int64
                readOnly: true
                example: 3
    '''

    TEAM_CHOICES = (
        ('V', 'Team Valor'), 
        ('I', 'Team Instinct'), 
        ('M', 'Team Mystic'),
    )
    
    id = models.BigAutoField(primary_key=True, editable=False)
    nickname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    team = models.CharField(max_length=1, choices=TEAM_CHOICES, default='')
    pokemons_owned = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        ordering=['id']
        verbose_name=_('Trainer')
        verbose_name_plural=_('Trainers')


    '''
    TRY TO CREATE AN POKEMON OBJECT
    '''
    @property
    def pokemons(self):
        return self.pokemon_set.all()

class Pokemon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, default='')
    base_experience = models.IntegerField(default=0, blank=True)
    height = models.IntegerField(default=0, blank=True)
    is_default = models.BooleanField(default=True, blank=True)
    order = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0, blank=True)
    
    trainer_id = models.ForeignKey(
        Trainer, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = _('Pokemon')
        verbose_name_plural = _('Pokemons')

    '''
    Pokemon:
        type: object
        properties:
            id:
                type: integer
                format: int64
                example: 12
            name:
                type: string
                example: butterfree
            base_experience:
                type: integer
                format: int64
                example: 179
            height:
                type: integer
                format: int64
                example: 11
            is_default:
                type: boolean
                example: true
            order:
                type: integer
                format: int64
                example: 16
            weight:
                type: integer
                format: int64
                example: 320
            abilities:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_abilities'
            forms:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_forms'
            game_indices:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_game_indices'
            held_items:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_held_items'
            location_area_encounters:
                type: string
                example: https://pokeapi.co/api/v2/pokemon/12/encounters
            moves:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_moves'
            species:
                $ref: '#/components/schemas/Pokemon_species'
            sprities:
                $ref: '#/components/schemas/Pokemon_sprities'
            stats:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_stats'
            types:
                type: array
                items:
                    $ref: '#/components/schemas/Pokemon_types'
        description: Pokemon data provided by [pokemon REST api](https://pokeapi.co/docs/v2#pokemon).
    '''