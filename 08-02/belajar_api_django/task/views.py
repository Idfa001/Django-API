from django.http import HttpResponse, JsonResponse
import json
from django.forms.models import model_to_dict
from .models import Crud


# untuk HttpResponse

# def index (req):
#     html = "apa aja bileh",;
#     return HttpResponse(html)


# untuk JsonResponse

def index(req):
    data = Crud.objects.all()  # query set

    simpan = []  # ibarat kaleng kosong untuk menyimpan data
    for e in data:  # query list
        simpan.append(model_to_dict(e))
    return JsonResponse({
        'data': simpan
    }, safe=False)


def create(req):
    if req.method == 'POST': #untuk mengecek post atau tidak
        data_byte = req.body #menyimpan req.body ke bentuk byte
        data_string = str(data_byte, 'utf-8') #merubah req.body ke data string
        data = json.loads(data_string)# mengirim data string dalam bentuk Json

        crud = Crud.objects.create(nama=data['nama'], motto=data['motto'])#create data
        return JsonResponse({
            'data': model_to_dict(crud),# model_to_dict berfungsi untuk mengubah model ke dalam dictionary
            }) 

def delete(req, id):
    if req.method == 'DELETE':
        crud = Crud.objects.filter(pk=id).delete()
    return JsonResponse({
        'msg':'data has ben delete'
    })

def detail(req, id):
    if req.method == 'GET':
        crud = Crud.objects.filter(pk=id).first()
        return JsonResponse({
            'data': model_to_dict(crud),
        })
def update(req, id):
    if req.method == 'PUT':

        data_byte = req.body #menyimpan req.body ke bentuk byte
        data_string = str(data_byte, 'utf-8') #merubah req.body ke data string
        data = json.loads(data_string)# mengirim data string dalam bentuk Json

        crud = Crud.objects.filter(pk=id).update(nama=data['nama'], motto=data['motto'])
        crud = Crud.objects.filter(pk=id).first()

        return JsonResponse({
            'data': model_to_dict(crud),# model_to_dict berfungsi untuk mengubah model ke dalam dictionary
            }) 
        


