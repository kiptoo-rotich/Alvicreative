from . import views
from django.urls import path

urlpatterns=[    
    path('', views.home,name='Home'),
    path('Our_approach/', views.approach,name='Approach'),
    path('Web_development/', views.web_development,name='web_development'),

]