from django.http import HttpResponse


def simple_view(request):
    return HttpResponse('ok!')

def view_with_param(request, param):
    return HttpResponse('ok! {}'.format(param))

