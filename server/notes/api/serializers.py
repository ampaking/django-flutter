from rest_framework.serializers import ModelSerializer

from .models import Note,Country

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'



class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
