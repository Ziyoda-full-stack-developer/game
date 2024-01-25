from django.urls import path
from .views import About, Contact, Index, Product, Remot, Video, featureDetail

urlpatterns = [
    path('about/',    About,     name="about"),
    path('contact/',  Contact,   name="contact"),
    path('index/',    Index,     name="index"),
    path('product/',  Product,   name="product"),
    path('remot/',    Remot,     name="remot"),
    path('video/',    Video,     name="video"),
    path('<int:id>/', featureDetail, name='featureDetail')
]