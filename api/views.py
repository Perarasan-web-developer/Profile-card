from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project.models import kelvin
from .serializers import ProjetcSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {'GET':'/api/project'},
        {'GET':'/api/project/id'},
        {'POST':'/api/project/id/vote'},
        {'POST':'/api/project'}
    ]
    return Response(routes)


@api_view(['GET'])
def getproject(request):
    project=kelvin.objects.all()
    serializer=ProjetcSerializer(project,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getprojectid(request,pk):
    project=kelvin.objects.get(id=pk)
    serializer=ProjetcSerializer(project,many=False)
    return Response(serializer.data)