from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from .serializers import CarSerializer



class CarListView(APIView):
    @staticmethod
    def get(request):
        data = Car.objects.all()
        serializer = CarSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)


class CarView(APIView):
    @staticmethod
    def get(request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car, context={'request': request}, many=False)
            return Response(serializer.data)
        except Car.DoesNotExist:
            return Response("Car does not exist")


class AddCarView(APIView):
    @staticmethod
    def post(request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Car added successfully")
        else:
            return Response(serializer.errors, status=400)


class UpdateCarView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            car = Car.objects.get(pk=pk)

        except Car.DoesNotExist:
            return Response("car does not exist")
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("car updated successfully")
        else:
            return Response(serializer.errors, status=400)


class DeleteCarView(APIView):
    @staticmethod
    def delete(request, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response("Car deleted successfully")
        except Car.DoesNotExist:
            return Response("car does not exist")




