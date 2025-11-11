from django.shortcuts import render 
from django.http import JsonResponse

from.models import Users 
from.serializers import userserializer  
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here. 
def get_element(request):
    return JsonResponse({'status':"error"})  
def get_users(request,id):
    u1=Users.objects.get(id=id)  
    # user_dict={} 
    # user_dict['name']=u1.name
    # user_dict['phone_number']=u1.phone_number 
    # user_dict['adress']=u1.adress 
    # user_dict['role']=u1.role 
    
    return JsonResponse({'userdetails':userserializer(u1).data})
@csrf_exempt
def create_users(request): 
    data=json.loads(request.body) 
    sr=userserializer(data=data) 
    if sr.is_valid(): 
        sr.save()  
        return JsonResponse(sr.data)
    else:
        return JsonResponse(sr.errors)
        
    return JsonResponse({'statsu':"not found"})  
@csrf_exempt
def update_users(request,id):
    u1=Users.objects.get(id=id) 
    data=json.loads(request.body) 
    partial=request.method=='PATCH' 
    update_data=userserializer(u1,data=data,partial=partial) 
    if update_data.is_valid(): 
        update_data.save()
        return JsonResponse(update_data.data)  
    return JsonResponse(update_data.errors)
    
        