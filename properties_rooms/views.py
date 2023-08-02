from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from .models import Property, Room
from users.models import CustomUser
from django.shortcuts import get_object_or_404


# Create your views here.

def model_data(property):
    property_data = {
        'id': property.id,
        'city': property.city,
        'address': property.address,
        'is_active': property.is_active,
        'owner': model_user_data(property.owner) if property.owner else None,
        'rooms': list(property.rooms.all().values()),
    }
    return property_data

def model_user_data(user):
         user_data = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'is_active': user.is_active,
                    'phone_number': user.phone_number, 
                    'contract': user.contract, 
                    'rent_payment_date': user.rent_payment_date, 
                    'debtor': user.debtor, 
                    'contract_end_date': user.contract_end_date, 
                    'plan_type':user.plan_type,
                }
         return user_data


class Properties(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id>0:
            try:
                 property = Property.objects.get(id=id)
                 property_data = model_data(property)
                 data = {'message':"success", 'property':property_data}
                 return JsonResponse(data, status = 200)
            except:
                 data = {'message':'Property not found'}
                 return JsonResponse(data, status=400)
        else:
            properties = Property.objects.all()
            properties_data = []
            for property in properties:
                 property_data = model_data(property)
                 properties_data.append(property_data)
            if len(properties_data)>0:
                 data = {'message':'success', 'properties': properties_data}
                 return JsonResponse(data, status = 200)
            else:
                 data = {'message':'Properties not found'}
                 return JsonResponse(data, status = 400)

    def post(self, request):
        try:
            jd = json.loads(request.body)
            property_address = jd.get('address')
            property_city = jd.get('city')
            property_owner_id = jd.get('owner')

            if Property.objects.filter(address = property_address):
                return JsonResponse({'message':'property exist'}, status = 400)
            
            owner = get_object_or_404(CustomUser, id=property_owner_id)
            property = Property.objects.create(city=property_city, address=property_address, owner=owner)
            property_data = model_data(property)
            data = {'message':'success', 'property':property_data}
            return JsonResponse(data, status=200)
        except KeyError:
            data = {'message':'owner not found'}
            return JsonResponse(data, status=400)
        

    def put(self,request,id):
        jd = json.loads(request.body)
        property = Property.objects.filter(id=id)

        if property.exists():
            property.update(**jd)
            updated_property = property.first()
            property_data = model_data(updated_property)
            data = {'message':'success', 'user': property_data}
            return JsonResponse(data, status=200)
        
        else:
            data={'message':'property not found'}
            return JsonResponse(data, status=400)