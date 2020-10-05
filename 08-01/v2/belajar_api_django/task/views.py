from django.http import JsonResponse

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

def index(req):
    data = Crud.objects.all() #query set

    simpan = [] #ibarat kaleng kosong untuk menyimpan data
    for e in data: #query list
        simpan.append({
            'nama':e.nama, # append untuk menambahkan data
            'motto':e.motto
        })
    return JsonResponse({
        'data': simpan #
    }, safe=False)