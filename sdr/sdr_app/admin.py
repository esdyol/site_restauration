from django.contrib import admin
from sdr_app.models import Client,reservation,Plat,Table,Menu
# Register your models here.
class client(admin.ModelAdmin): 
    list_display =('user','telephone','adresse')

class reservationlist(admin.ModelAdmin):
    liste_display = ('client','table','date','heure')

class tables(admin.ModelAdmin):
    list_display = ('numero','capacite','disponible') 
    
class platlist(admin.ModelAdmin):
    list_display = ('nom','description','prix','categories','image')
    
class menu(admin.ModelAdmin):
    list_display = ('plats','date')
    
    def plats(self,obj):
        return ",".join([str(item) for item in obj.related_items.all()])
    plats.short_description ="related items"
    
admin.site.register(Client,client)
admin.site.register(reservation,reservationlist)
admin.site.register(Plat,platlist)
admin.site.register(Table,tables)
admin.site.register(Menu,menu)