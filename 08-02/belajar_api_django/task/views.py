from django.http import JsonResponse
from . import models
def index(req):
    data = models.Crud.objects.all() 

    simpan = [] #ibarat kaleng kosong untuk menyimpan data
    for e in data: #query list
        simpan.append({
            'nama':e.nama, # append untuk menambahkan data
            'motto':e.motto
        })
    return JsonResponse({
        'data': simpan #
    }, safe=False)



    # def print(request):
#     html = [
#         {
#             'name' : 'Josefine',
#             'moto' : 'The universe has a beginning, but no end'},
#         {
#             'name' : 'Christina',
#             'moto' : 'You can run away, but that\'ll just make it worse!'}
#     ]
    

#     return JsonResponse({'html' : html})
