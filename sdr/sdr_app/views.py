from django.shortcuts import render,redirect
from django.http import HttpResponse
from sdr_app.models import Client,Table,Menu,reservation,Plat
from django.utils import timezone
from django.core.mail import send_mail
from sdr_app.forme import ClientForm,TableForm,ReservationForm,PlatForm,MenuForm,UserForm
from datetime import date
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
#from .forms import UserClientForm


# Create your views here.
def acceuil(request):
    plat_jour = Plat.objects.all()
    return render (request,
                   "accueil.html",
                   {"plats":plat_jour})

def menu(request):
     plats = plat.objects.all()
     return render(request,
                   "menu.html",
                   {'plats':plats})
def is_client(user):
    return hasattr(user, 'client') and user.client.role == 'client'

def is_admin(user):
    return user.is_superuser or user.is_staff or (hasattr(user, 'client') and user.client.role == 'admin')

def about(request):
    return HttpResponse("<h1>A propos </h1> <p> il n'y a rien a dire</p>")
# fonction pour créer ,modifier,mettre à jour et supprimer les clients 
def client(request):
    band= Client.objects.all()
    return render(request,
                  "client_list.html",
                  {"band":band})

def client_detail(request,id1):
    bande=Client.objects.all()
    band = next((b for b in bande if b.id==id1),None)
    
    if band is None:
        return render(request,'404.html',status=404)
    return render(request,
                  'client_detail.html',
                  {'band':band})

def client_create(request):
    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('client-detail',band.id)
    
    else:
        form = ClientForm()
        
    return render(request,
                  'client_form.html',
                  {'form':form})

def client_update(request,ide):
    band = Client.objects.get(id=ide)
    
    if request.method == 'POST':
        form = ClientForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            
            return redirect('client-detail',band.id)
        
    else :
        form = ClientForm(instance=band)
    return render(request,
                  'client_update.html',
                  {'form':form})

def client_delete(request,ide):
    band = Client.objects.get(id=ide)
    
    if request.method == 'POST':
        band.delete()
        return redirect('client-detail')
    
    return render(request,
                  'client_confirm_delete.html',
                  {'band':band})

# fonction pour créer ,modifier,mettre à jour et supprimer les reservations

def reservation_list(request):
    reserver= reservation.objects.all()
    return render(request,
                  "reservation_list.html",
                  {"reserver":reserver})

def reservation_detail(request,ide):
    bande = reservation.objects.all()
    band = next((b for b in bande if b.id==ide),None)
    
    if band is None:
        return render(request,'404.html',status=404)
    return render(request,
                  'reservation_detail.html',
                  {'band':band})

def reservation_update(request,ide):
    band =reservation.objects.get(id=ide)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            
            return redirect('reservation-liste')
        
    else :
        form = ReservationForm(instance=band)
    return render(request,
                  'reservation_update.html',
                  {'form':form})

def reservation_delete(request,ide):
    band = reservation.objects.get(id=ide)
    
    if request.method == 'POST':
        band.delete()
        return redirect('reservation-liste')
    
    return render(request,
                  'reservation_confirm_delete.html',
                  {'band':band})

# fonction pour créer ,modifier,mettre à jour et supprimer les plats

def plat(request):
    plats= Plat.objects.all()
    return render(request,
                  "plat_list.html",
                  {"plats":plats})

def plat_detail(request,ide):
    bande=Plat.objects.all()
    band = next((b for b in bande if b.id==ide),None)
    
    if band is None:
        return render(request,'404.html',status=404)
    return render(request,
                  'plat_detail.html',
                  {'band':band})

def plat_create(request):
    if request.method =='POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('plat-detail',band.id)
    
    else:
        form = PlatForm()
        
    return render(request,
                  'plat_form.html',
                  {'form':form})

def plat_update(request,ide):
    band = Plat.objects.get(id=ide)
    
    if request.method == 'POST':
        form = PlatForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            
            return redirect('plat-liste')
        
    else :
        form = PlatForm(instance=band)
    return render(request,
                  'plat_update.html',
                  {'form':form})

def plat_delete(request,ide):
    band = Plat.objects.get(id=ide)
    
    if request.method == 'POST':
        band.delete()
        return redirect('plat-liste')
    
    return render(request,
                  'plat_confirm_delete.html',
                  {'band':band})

# fonction pour créer ,modifier,mettre à jour et supprimer les tables
@login_required
@user_passes_test(is_admin)
def table(request):
    tables= Table.objects.all()
    return render(request,
                  "table_list.html",
                  {"tables":tables})

@login_required
@user_passes_test(is_admin)
def table_detail(request,ide):
    bande=Table.objects.all()
    band = next((b for b in bande if b.id==ide),None)
    
    if band is None:
        return render(request,'404.html',status=404)
    return render(request,
                  'table_detail.html',
                  {'band':band})

@login_required
@user_passes_test(is_admin)
def table_create(request):
    if request.method =='POST':
        form = TableForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('table-detail',band.id)
    
    else:
        form = TableForm()
        
    return render(request,
                  'table_form.html',
                  {'form':form})

@login_required
@user_passes_test(is_admin)
def table_update(request,ide):
    band = Table.objects.get(id=ide)
    
    if request.method == 'POST':
        form = TableForm(request.POST,instance=band)
        if form.is_valid():
            form.save()
            
            return redirect('table-liste')
        
    else :
        form = TableForm(instance=band)
    return render(request,
                  'table_update.html',
                  {'form':form})

@login_required
@user_passes_test(is_admin)
def table_delete(request,ide):
    band = Table.objects.get(id=ide)
    
    if request.method == 'POST':
        band.delete()
        return redirect('table-liste')
    
    return render(request,
                  'table_confirm_delete.html',
                  {'band':band})

# fonction pour s'inscrire
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            Client.objects.create(user=user, role='client')
            messages.success(request,"votre compte a ete bien créer")
            return redirect('login')
        
    return render(request,
                  'register.html',
                  {'form':form}
                  )

# fonction pour se connecter
def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if is_admin(user):
                return redirect('dashboard')
            elif is_client(user):
                return redirect('acceuil')
            else:
                logout(request)
                messages.error(request,"utilisateur inconnu.")
        else :
            messages.error(request,"erreur d'autentification")
            
    return render(request,
                  'login.html')

# fonction pour se deconnecter
@login_required # l' utilisateur doit se connecter d'abord
def deconnexion(request):
    logout(request)
    messages.info(request,"vous avez été déconnecté.")
    return redirect('login')

# fonction pour faire une reservation
@login_required
@user_passes_test(is_client)
def reserver(request):
    if request.method=='POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            heure = form.cleaned_data["heure"]
            nombre_personne = form.cleaned_data["nombre_personne"]

            if date < timezone.localdate():
                messages.error(request,"La date doit etre dans le future.\n")
                return redirect('reserver')
            
            nb_table_total = Table.objects.count()
            nb_table_occupe = reservation.objects.filter(date=date,heure=heure).count()
            if nb_table_occupe >= nb_table_total:
                messages.error(request,"Aucune table n'est disponble à cette date et heure.\n")
                return redirect("reserver")
            
            tables_occupees = reservation.objects.filter(date=date,heure=heure).values_list('table__id',flat=True)
            tables_libre = Table.objects.exclude(id__in = tables_occupees).first()

            if not tables_libre:
                messages.error(request,"Plus de table disponible.")
                return redirect("reserver")
            
            form = form.save(commit=False)
            form.client = Client.objects.get(user=request.user)
            form.table = tables_libre
            form.save()
            messages.success(request,"Reservation enregistrée.")
            return redirect("acceuil")
    else:
        form = ReservationForm()
    return render(request,
                  'reservation1.html',
                  {'form':form}
                  )

# fonction pour voir le dashbord
@login_required
@user_passes_test(is_admin)
def dashboard_admin(request):
    total_reservations_today = reservation.objects.filter(date=timezone.localdate()).count()
    total_clients = Client.objects.count()
    total_plats = Plat.objects.count()
    reservations_recentes = reservation.objects.order_by('-date', '-heure')[:5]
    liste_client = Client.objects.all()
    liste_table = Table.objects.all()
    liste_reservations = reservation.objects.all()

    # Exemple simple : les plats les plus commandés (si tu as un compteur ou modèle de commande)
    plats_populaires = Plat.objects.all()[:5]  # à adapter selon ton système

    return render(request, 'dashboard.html', {
        'total_reservations_today': total_reservations_today,
        'total_clients': total_clients,
        'total_plats': total_plats,
        'reservations_recentes': reservations_recentes,
        'plats_populaires': plats_populaires,
        'liste_client':liste_client,
        'liste_table':liste_table,
        'liste_reservations':liste_reservations
    })

