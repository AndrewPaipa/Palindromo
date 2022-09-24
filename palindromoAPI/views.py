from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
import json
from .palindromoScr import funtionPalindromo

# Create your views here.

# Clase palindromo


class Palindromo(View):

    #Decorador para omitir token csrf

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Metodo get de /palindromo/

    def get(self, request):
        # get...
        cmessageGET = {'message':'GET success'}
        return JsonResponse(cmessageGET)

    #Metodo post de /palindromo/

    def post(self, request):
        #post ...
        expression = json.loads(request.body)
        subStr = funtionPalindromo(expression['expresion'])
        if subStr == None:
            cmessagePOST = {'message':'POST success', 'cadena': expression['expresion'], 'palindromo mas largo':'No hay palindromos'}
        else:
            cmessagePOST = {'message':'POST success', 'cadena': expression['expresion'], 'palindromo mas largo':subStr}
        
        return JsonResponse(cmessagePOST)

    #Metodo put de /palindromo/

    def put(self, request):
        # put...
        cmessagePUT = {'message':'PUT success'}
        return JsonResponse(cmessagePUT)
    
    #Metodo delete de /palindromo/

    def delete(self, request):
        # delete...
        cmessageDELETE = {'message':'DELETE success'}
        return JsonResponse(cmessageDELETE)



class Index(View):

    #Metodo get de /

    def get(self, request):
        # get...
        cmessageGET = {'message':'success'}
        return JsonResponse(cmessageGET)