import graphene
from graphene_django import DjangoObjectType

from .models import Salal


class SalalType(DjangoObjectType):
    class Meta:
        model = Salal


class Query(graphene.ObjectType):
    salgql = graphene.List(SalalType)

    def resolve_salgql(self, info, **kwargs):
        return Salal.objects.all()

#create
class CreateSalal(graphene.Mutation):
    id = graphene.Int()
    album = graphene.String()
    artist = graphene.String()
    song = graphene.String()

    class Arguments:
        album = graphene.String()
        artist = graphene.String()
        song = graphene.String()

    def mutate(self, info, album, artist, song):
        salal = Salal(album=album, artist=artist, song=song)
        salal.save()

        return CreateSalal(
            id=salal.id,
            album=salal.album,
            artist=salal.artist,
            song=salal.song,
        )


#4
class Mutation(graphene.ObjectType):
    create_salal = CreateSalal.Field()