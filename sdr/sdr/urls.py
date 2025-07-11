"""
URL configuration for sdr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from sdr_app.views import reservation_delete,reservation_update, reservation_detail,reservation_list ,client_detail,acceuil,reserver,register,deconnexion,connexion,dashboard_admin
from sdr_app.views import plat,plat_detail,plat_create,plat_delete,plat_update,about,client,client_delete,client_update,client_create,table,table_detail,table_create,table_delete,table_update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about),

#les urls pour les clients

    path('client/',client,name='client'),
    path('client/<int:id1>/',client_detail,name="client-detail"),
    path('client/add/',client_create,name="client-create"),
    path('client/<int:ide>/change/',client_update,name="client-update"),
    path('client/<int:ide>/delete/',client_delete,name="client-delete"),

    path('acceuil/',acceuil,name="acceuil"),
    path('reserver/',reserver,name="reserver"),
    path('register/',register,name='register'),
    path('connexion/',connexion,name="login"),
    path('logout/',deconnexion,name="logout"),
    path('dashboard/', dashboard_admin, name='dashboard'),

    #les urls pour les reservations

    path('reservation/',reservation_list,name='reservation-liste'),
    path('reservation/<int:ide>/',reservation_detail,name="reservation-detail"),
    path('reservation/<int:ide>/change/',reservation_update,name="reservation-update"),
    path('reservation/<int:ide>/delete/',reservation_delete,name="reservation-delete"),

    #les urls pour les plats

    path('plat/',plat,name='plat-liste'),
    path('plat/<int:ide>/',plat_detail,name="plat-detail"),
    path('plat/<int:ide>/change/',plat_update,name="plat-update"),
    path('plat/<int:ide>/delete/',plat_delete,name="plat-delete"),
    path('plat/add/',plat_create,name="plat-create"),

    #les urls pour les tables

    path('table/',table,name='table-liste'),
    path('table/<int:ide>/',table_detail,name="table-detail"),
    path('table/<int:ide>/change/',table_update,name="table-update"),
    path('tablet/<int:ide>/delete/',table_delete,name="table-delete"),
    path('table/add/',table_create,name="table-create"),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
