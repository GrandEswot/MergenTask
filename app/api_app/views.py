from rest_framework.response import Response
from rest_framework.views import APIView


class MyAPIVIewEven(APIView):

    def get(self, request):
        query_params = request.query_params
        numbers = query_params.get('number', None)
        even_params = []
        if numbers is not None:
            for number in numbers.split(','):
                even_params.append(int(number))
        else:
            return Response({'result': False})
        if all([i % 2 == 0 for i in even_params]):
            return Response({'result': True})
        return Response({'result': False})

    def post(self, request):
        any_data = request.data.get('numbers')
        result = []
        for number in any_data:
            if number % 2 == 0:
                result.append(number)
        return Response({"result": result})


class MyAPIVIewOdd(APIView):

    def get(self, request):
        query_params = request.query_params
        numbers = query_params.get('number', None)
        even_params = []
        if numbers is not None:
            for number in numbers.split(','):
                try:
                    even_params.append(int(number))
                except ValueError:
                    return Response('Введен некорректный тип данных')
        else:
            return Response({'result': False})
        if all([i % 2 != 0 for i in even_params]):
            return Response({'result': True})
        return Response({'result': False})

    def post(self, request):
        try:
            any_data = request.data.get('numbers')
            result = []
            for number in any_data:
                if number % 2 != 0:
                    result.append(number)
            return Response({"result": result})
        except:
            return Response("Введен неверный формат данных")
