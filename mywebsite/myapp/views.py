from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # context={
    #     "variable1":"harsh is good person",
    #     "variable2":"harsh is tall"
    # }
    # return render(request, 'index.html', context)

    #return HttpResponse("this is home page")
    

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("this is services page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is contact page")