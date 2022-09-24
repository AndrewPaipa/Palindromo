from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
import json


# Create your views here.
class Palindromo(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # get...
        cmessageGET = {'message':'success'}
        return JsonResponse(cmessageGET)

    def post(self, request):
        #post ...
        expresion = json.loads(request.body)
        print(expresion)
        cmessagePOST = {'message':'success'}
        return JsonResponse(cmessagePOST)