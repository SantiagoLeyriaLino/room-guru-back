from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Create your views here.
class Properties(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id>0:
            pass
        else:
            pass

    def post(self, request):
        pass

    def put(self,request,id):
        pass