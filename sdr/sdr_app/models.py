from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    role_choice = [
        ('client','Client'),
        ('admin','administrateur'),
    ]
    role = models.CharField(max_length=10, choices=role_choice,default='client')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='client')
    telephone = models.CharField(max_length=15,default="")
    adresse = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return f" client: {self.user.first_name} ,{self.telephone} , {self.adresse}"
class Table(models.Model):
    numero = models.PositiveIntegerField(default=1,unique=True)
    capacite = models.PositiveIntegerField(default=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Table {self.numero} Capacité :{self.capacite}"

class Plat(models.Model):
    CATEGORIES = [
        ('entree','Entrée'),
        ('plat','plat principal'),
        ('dessert','Dessert')
        ]
    nom = models.CharField(max_length = 100)
    description = models.TextField(default="")
    prix = models.DecimalField(max_digits=6,decimal_places=2)
    categories = models.CharField(max_length=10,choices=CATEGORIES)
    image = models.ImageField(upload_to='images',blank=True,null=True)
    
    def __str__(self):
        return self.nom
    
class Menu(models.Model):
    plats = models.ManyToManyField(Plat,related_name='Menus',default=True)
    date = models.DateField(default=True)
    
    def __str__(self):
        return f"Menu du {self.date}"
    
    
class reservation(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='reservation',null=True)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL,null=True,blank=True,related_name='reservation')
    date = models.DateField()
    heure = models.TimeField()
    nombre_personne =models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        
        client_nom = self.client.user.username if self.client and self.client.user else "Client inconnu"
        date = self.date.strftime("%Y-%m-%d") if self.date else "date inconnue"
        heure = self.heure.strftime("%H:%M") if self.heure else "heure inconnue"
        table_num = self.table.numero if self.table else "non assignée"

        return f"Réservation de {client_nom} pour le {date} à {heure}, table {table_num}"

    