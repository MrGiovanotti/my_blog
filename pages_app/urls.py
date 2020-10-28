from django.urls import path
from pages_app import views

urlpatterns = [path('page/<str:slug>', views.page, name = 'page'),
]
