from django.http import JsonResponse

def print(request):
    html = [
        {
            'name' : 'Josefine',
            'moto' : 'The universe has a beginning, but no end'},
        {
            'name' : 'Christina',
            'moto' : 'You can run away, but that\'ll just make it worse!'}
    ]
    

    return JsonResponse({'html' : html})
