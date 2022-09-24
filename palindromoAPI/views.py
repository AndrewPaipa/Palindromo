from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
import json
from .palindromoScr import funtionPalindromo

# Create your views here.
class Palindromo(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # get...
        cmessageGET = {'message':'GET success'}
        return JsonResponse(cmessageGET)

    def post(self, request):
        #post ...
        expression = json.loads(request.body)
        subStr = funtionPalindromo(expression['expresion'])
        if subStr == None:
            cmessagePOST = {'message':'POST success', 'cadena': expression['expresion'], 'palindromo mas largo':'No hay palindromos'}
        else:
            cmessagePOST = {'message':'POST success', 'cadena': expression['expresion'], 'palindromo mas largo':subStr}
        
        return JsonResponse(cmessagePOST)


class Index(View):

    def get(self, request):
        # get...
        cmessageGET = {'message':'success'}
        return JsonResponse(cmessageGET)