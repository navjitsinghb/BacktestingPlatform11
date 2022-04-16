from django.urls import path

from . import views
urlpatterns = [
    path('', views.build, name='build'),
    path('algos',views.myalgos, name="algos"),
    path('postalgo',views.postalgo, name="postalgo"),
    path('useralgos',views.useralgo, name="useralgos"),
    path('edit/<int:id>/',views.editalgo, name="editalgo")
]