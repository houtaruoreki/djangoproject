from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Animal
from .serializers import AnimalSerializer


class AnimalView(APIView):
    @staticmethod
    def get(request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
            serializer = AnimalSerializer(animal, context={'request': request}, many=False)
            return Response(serializer.data, status=200)
        except Animal.DoesNotExist:
            return Response('Animal does not exist', status=404)


class AnimalListView(APIView):
    @staticmethod
    def get(request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, context={'request': request}, many=True)
        return Response(serializer.data)


class AddAnimalView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Animal added successfully!')
        else:
            return Response(serializer.errors, status=400)


class UpdateAnimalView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response({"error": "Animal not found"})

        serializer = AnimalSerializer(animal, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "successful", "new data": serializer.data})
        return Response(serializer.errors, )


class DeleteAnimalView(APIView):
    @staticmethod
    def delete(request, pk):
        try:
            animal = Animal.objects.get(pk=pk)
            animal.delete()
            return Response('Animal deleted successfully!')
        except Animal.DoesNotExist:
            return Response('animal does not exist')
