from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Header, Footer, List, You, Pric, Text, Image, Gamepad, Uchdi, Face, Feature
from .forms import ContactForm

# Create your views here.

def About(request):
    header = Header.objects.all()
    context = {
        'header': header
    }
    return render(request, 'about.html', context=context)

def Contact(request):
    footer = Footer.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    context = {
        'footer': footer,
        'form': form
    }
    return render(request, 'contact.html', context=context)

def Index(request):
    list = List.objects.all()
    you = You.objects.all()
    pric = Pric.objects.all()
    text = Text.objects.all()
    image = Image.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Formangiz qabul qilindi</h1>")
    context = {
        'list': list,
        'you': you,
        'pric': pric,
        'text': text,
        'image': image,
        'form': form
    }
    return render(request, 'index.html', context=context)

def Product(request):
    gamepad = Gamepad.objects.all()
    context = {
        'gamepad': gamepad
    }
    return render(request,  'product.html', context=context)

def Remot(request):
    uchdi = Uchdi.objects.all()
    context = {
        'uchdi': uchdi
    }
    return render(request, 'remot.html', context=context)

def Video(request):
    face = Face.objects.all()
    context = {
        'face': face
    }
    return render(request, 'video.html', context=context)

def featureDetail(requests, id):
    try:
        featuredetail = Feature.objects.get(id=id)
        context = {
            'featuredetail': featuredetail
        }
    except featuredetail.DoesNotExist:
        raise Http404("No product found")

    return render(requests, 'featureDetail.html', context=context)