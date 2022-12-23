from django.contrib import admin
from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home page'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('battery/', views.battery, name='battery'),
    path('folder/', views.service, name='folder'),
    path('contact/', views.contact, name='contact'),
    path('explore/', views.explore, name='explore'),

]