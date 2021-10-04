from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NumberSerializer


class MyAPIVIewEven(APIView):

    @staticmethod
    def get(request):
        query_params = request.query_params
        numbers = query_params.get('number', None)
        even_params = []
        if numbers is not None:
            for number in numbers.split(','):
                try:
                    even_params.append(int(number))
                except Exception:
                    return Response({'result': False})
        else:
            return Response({'result': False})
        if all([i % 2 == 0 for i in even_params]):
            return Response({'result': True})
        return Response({'result': False})

    @staticmethod
    def post(request):
        query_params = request.query_params
        numbers = query_params.get('numbers', None)
        even_numbers = []
        if numbers is not None:
            for number in numbers.split(','):
                try:
                    if int(number) % 2 == 0:
                        even_numbers.append(int(number))
                except Exception:
                    return Response({'result': 'Неверный формат данных'})
        return Response({'result': even_numbers})


class MyAPIVIewOdd(APIView):

    @staticmethod
    def get(request):
        query_params = request.query_params
        numbers = query_params.get('number', None)
        even_params = []
        if numbers is not None:
            for number in numbers.split(','):
                try:
                    even_params.append(int(number))
                except Exception:
                    return Response({'result': False})
        else:
            return Response({'result': False})
        if all([i % 2 != 0 for i in even_params]):
            return Response({'result': True})
        return Response({'result': False})

    @staticmethod
    def post(request):
        query_params = request.query_params
        numbers = query_params.get('numbers', None)
        even_numbers = []
        if numbers is not None:
            for number in numbers.split(','):
                try:
                    if int(number) % 2 != 0:
                        even_numbers.append(int(number))
                except Exception:
                    return Response({'result': 'Неверный формат данных'})
        return Response({'result': even_numbers})
