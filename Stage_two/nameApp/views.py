from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET','POST'])
def person_list(request, format=None):


    if request.method == 'GET':
        
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    
    if request.method == 'POST':
        print(request.data)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT', 'DELETE'])
def person_detail(request, id, format=None):

    
    try:
        person =Person.objects.get(pk=id)
    except (ValueError, Person.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    
    if request.method == "GET":
        serializer =  PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
