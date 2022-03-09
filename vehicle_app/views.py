from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleOrderSerializer
from datetime import datetime, timedelta
from .models import VehicleOrder


@api_view(['GET'])
def taskList(request):
	tasks = VehicleOrder.objects.exclude(date__lt= datetime.now()-timedelta(days=3))
	serializer = VehicleOrderSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = VehicleOrder.objects.get(id=pk)
	serializer = VehicleOrderSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = VehicleOrderSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data['id'])

@api_view(['POST'])
def taskUpdate(request, pk):
	task = VehicleOrder.objects.get(id=pk)
	serializer = VehicleOrderSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)