from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AnimalSerializer, NoteSerializer,CountrySerializer
from .models import Note,Country,AnimalList

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'

        },
        {
            'Endpoint':'/notes/id',
            'method': 'GET',
            'body':None,
            'description':'Return a single note object'
        

        }, 
        {
            'Endpoint':'/notes/create/',
            'method':'POST',
            'body':{'body':""},
            'description':'Create a new note with data in post request'
        },
        {
            'Endpoint':'/notes/id/update/',
            'method':'PUT',
            'body':{'body':""},
            'description': 'Update and existion note',
        },
        {
            'Endpoint':'/notes/id/delete/',
            'method':'DELETE',
            'body':None,
            'description':'Delete an existing note',


        },
        {
            'Endpoint':'/country-name/',
            'method':'GET',
            'body':None,
            'description':'See Country Name',
        },
        {
            'Endpoint':'/country-name/id/',
            'methord':'GET',
            'body':None,
            'description':'Return a single country name ID',
        },{
            'Endpoint':'/country-name/create',
            'method':'POST',
            'body':{"body":''},
            'description':'Add new country name',

        },{
            'Endpoint':'country-name/id/update',
            'method':'PUT',
            'body':{"body":""},
            'description':'Update current country name ID ',
        },{
            'Endpoint':'country-name/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Delete an excising country name',
        },{
            'Endpoint':'animal-list/',
            'method':'GET',
            'body':None,
            'description':'Here have list of animals Name'

        },
        {
            'Endpoint':'animal-list/id',
            'method':'GET',
            'body':None,
            'description':'Return a single animal name',
        }, 
        {
            'Endpoint':'animal-name/create',
            'method':'POST',
            'body':{
                "body":""
            },
            'description':'add new animal name'
        }, 
        {
            'Endpoint':'animal-name/id/update',
            'method':'PUT',
            'body':{
                "body":""
            },
            'description':'Update current animal name',
        }, 
        {
            'Endpoint':'animal-name/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Delete a single animal name',
        }


    ]


    return Response(routes)

# Note Api Start    
# Return list of notes
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)


# Return single note
@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many= False)

    return Response(serializer.data)

#create a note
@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

#update a note
@api_view(['PUT'])
def updateNote(request, pk):

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# delete Note    
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!!!')

# Note Api end


# Country Name Api Start
# Return list of Country name
@api_view(['GET'])
def getCountry(request):
    country = Country.objects.all()
    serializer = CountrySerializer(country,many=True)

    return Response(serializer.data)


# Return a single Country Name
@api_view(['GET'])
def getSingleCountry(request, pk):
    single_Country = Country.objects.get(id=pk)
    serializer = CountrySerializer(single_Country, many=False)
    return Response(serializer.data)    

#add a new Country name
@api_view(['POST'])
def addCountry(request):
    data = request.data
    country = Country.objects.create(
        body=data['body']
    )
    serializer =CountrySerializer(country,many=False)

    return Response(serializer.data)


#Update Existing country name

@api_view(['PUT'])
def updateCountry(request, pk):
    country = Country.objects.get(id=pk)
    serializer = CountrySerializer(country, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete a single country name
@api_view(['DELETE'])
def deleteCountry(request, pk):
    country = Country.objects.get(id=pk)
    country.delete()
    return Response('You delete a country name')


# Country Name Api end    


# List of animal Start

@api_view(['GET'])
def getAnimalList(request):
    animal_list = AnimalList.objects.all()
    serializer = AnimalSerializer(animal_list, many=True)

    return Response(serializer.data)


# get a single animal name from list
@api_view(['GET'])
def getAAnimal(request, pk):
    a_animal = AnimalList.objects.get(id=pk)
    serializer = AnimalSerializer(a_animal, many=False)
    return Response(serializer.data)

#add animal to list

@api_view(['POST'])
def addAnimalInList(request):
    data = request.data
    animalList = AnimalList.objects.create(
        body=data['body']
    )
    serializer = AnimalSerializer(animalList, many=False)
    return Response(serializer.data)

# update animal list
@api_view(['PUT'])
def updateAnAnimal(request, pk):
    animal = AnimalList.objects.get(id=pk)
    serializer = AnimalSerializer(animal, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#delete an animal from list 
@api_view(['DELETE'])

def deleteAnAnimal(request, pk):
    animal = AnimalList.objects.get(id=pk)
    animal.delete()

    return Response("Delete an animal from list")


