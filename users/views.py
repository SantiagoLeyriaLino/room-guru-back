from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
import json
from .models import CustomUser


def model_data(user):
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
                    'properties': list(user.properties.all().values()),
                    'transactions': list(user.transactions.all().values()),
                    'tasks': list(user.tasks.all().values()),
                    'messages': list(user.messages.all().values()),
                    'room': list(user.room.all().values())[0]
                }
         return user_data


class Users_views(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if id>0:
            try:
                user = CustomUser.objects.get(id=id)
                user_data = model_data(user)
                data = {'message': 'success', 'user': user_data}
                return JsonResponse(data, status=200)
            except CustomUser.DoesNotExist:
                data = {'message': 'user not found'}
                return JsonResponse(data, status=400)
            
        else:
            users = CustomUser.objects.all()
            users_data = []
            for user in users:
                user_data=model_data(user)
                users_data.append(user_data)
            if len(users_data)>0:
                data = {'message':'success', 'users':users_data}
                return JsonResponse(data, status=200)
            else:
                data = {'message':'users not found'}
                return JsonResponse(data, status=400)


    def post(self, request):
        jd = json.loads(request.body)
        password = jd.pop('password', None)
        username = jd.get('username')

        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'user exist'}, status=400)
        
        user = CustomUser.objects.create(**jd)

        if password:
            user.set_password(password)
            user.save()

        userData = model_data(user)
        data = {'message':'user created', 'user':userData}
        return JsonResponse(data, status=201)


    def put(self, request, id):
        jd = json.loads(request.body)
        user = CustomUser.objects.filter(id=id)

        if user.exists():
            user.update(**jd)
            updated_user = user.first()
            user_data = model_data(updated_user)
            data = {'message':'success', 'user': user_data}
            return JsonResponse(data, status=200)
        
        else:
            data={'message':'user not found'}
            return JsonResponse(data, status=400)
        

class User_Login(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
          jd = json.loads(request.body)
          username = jd.get('username')
          password = jd.get('password')

          user = authenticate(request, username=username, password=password)
          if user is not None:
              data_user = model_data(user)
              return JsonResponse({'message':'login success', 'user':data_user}, status=200)
          else:
            try:
              user = CustomUser.objects.get(username=username)
              data = {'message': 'Invalid password'}
            except:
              data = {'message': 'Invalid username'}
              
            return JsonResponse(data, status=400)