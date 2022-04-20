from rest_framework import serializers
from .models import *

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = [
            'id', 
            'name', 
            'base_experience', 
            'height', 
            'is_default', 
            'order', 
            'weight',
            'trainer_id'
        ]

class TrainerSerializer(serializers.ModelSerializer):
    pokemons = PokemonSerializer(many=True)

    class Meta:
        model = Trainer
        fields = [
            'id',
            'nickname', 
            'first_name', 
            'last_name', 
            'email', 
            'password',
            'team', 
            'pokemons_owned',
            'pokemons',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'email': {'write_only': True},
            'password': {'write_only': True},
            'pokemons_owned': {'read_only': True},
        }

    '''
    TRY TO CREATE A POKÉMON OBJECT
    '''

    def create(self, validated_data):
        pokemons = validated_data.pop('pokemons')
        trainer = Trainer.objects.create(**validated_data)
        for pokemon in pokemons:
            Pokemon.objects.create(**pokemon, trainer=trainer)
        return trainer
    """ 
    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id=choice["id"])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices:
            if choice.id not in keep_choices:
                choice.delete()

        return instance
     """