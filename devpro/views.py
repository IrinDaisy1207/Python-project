from django.http import HttpResponse



def msg(request):
    return HttpResponse("Django framework")




