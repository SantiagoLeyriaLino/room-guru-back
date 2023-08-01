from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.contrib.auth import authenticate
import json
from .models import CustomUser


class Users_views(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get(self, request, id=0):

        if id>0:
            userList = list(CustomUser.objects.filter(id=id).values())
            if len(userList)>0:
                user = userList[0]
                data = {"message":"success", "user":user}
                return JsonResponse(data, status=200)
            else:
                data = {"message":"user not found"}
                return JsonResponse(data, status=400)
            
        else:
            users = list(CustomUser.objects.values())
            if len(users)>0:
                data = {"message":"success", "users":users}
                return JsonResponse(data, status=200)
            else:
                data = {"message":"users not found"}
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

        userData = model_to_dict(user)
        data = {'message':'user created', 'user':userData}
        return JsonResponse(data, status=201)


    def put(self, request, id):
        jd = json.loads(request.body)
        user = CustomUser.objects.filter(id=id)

        if user.exists():
            user.update(**jd)
            updated_user = user.first()
            user_data = model_to_dict(updated_user)
            user_data.pop('password', None)
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
              data_user = model_to_dict(user)
              data_user.pop('password')
              return JsonResponse({'message':'login success', 'user':data_user}, status=200)
          else:
            try:
              user = CustomUser.objects.get(username=username)
              data = {'message': 'Invalid password'}
            except:
              data = {'message': 'Invalid username'}
              
            return JsonResponse(data, status=400)