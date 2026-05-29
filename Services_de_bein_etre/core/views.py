from django.shortcuts import render, redirect, get_object_or_404
from .models import Service, RendezVous
from .forms import RendezVousForm, RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count

#methode pour faire la retage a la page home.html
def home(request):
    return render(request, 'core/home.html')


def service_list(request):

    services = Service.objects.all()

    paginator = Paginator(services, 6)
    page = request.GET.get('page')
    services = paginator.get_page(page)

    return render(request, 'core/service_list.html', {'services': services})




def service_detail(request, id):

    service = get_object_or_404(Service, id=id)

    return render(request, 'core/service_detail.html', {'service': service})





#fonction pour recupiree la list des rendez-vous si lutilisateur est login
@login_required
def rdv_list(request):

    rendezvous = RendezVous.objects.filter(client=request.user)
    paginator = Paginator(rendezvous, 5)
    page = request.GET.get('page')
    rendezvous = paginator.get_page(page)

    return render(request, 'core/rdv_list.html', {'rendezvous': rendezvous})

#une fonction pour réservé un rendez-vous si lutilisateur est login
@login_required
def rdv_create(request):

    if request.method == "POST":

        form = RendezVousForm(request.POST)

        if form.is_valid():

            rdv = form.save(commit=False)
            rdv.client = request.user
            rdv.save()
            messages.success(request, "Rendez-vous réservé avec succès")

            return redirect('rdv_list')

    else:
        form = RendezVousForm()

    return render(request, 'core/rdv_create.html', {'form': form})

#methode pour modifié un rendez-vous
@login_required
def rdv_update(request, id):

    rdv = get_object_or_404(RendezVous, id=id, client=request.user)

    if request.method == "POST":

        form = RendezVousForm(request.POST, instance=rdv)

        if form.is_valid():
            form.save()
            messages.success(request, "Rendez-vous modifié")
            return redirect('rdv_list')

    else:
        form = RendezVousForm(instance=rdv)

    return render(request, 'core/rdv_update.html', {'form': form})

#methode pour supprimé un rendez-vous
@login_required
def rdv_delete(request, id):

    rdv = get_object_or_404(RendezVous, id=id, client=request.user)

    if request.method == "POST":
        rdv.delete()
        messages.success(request, "Rendez-vous supprimé")
        return redirect('rdv_list')

    return render(request, 'core/rdv_delete.html', {'rdv': rdv})

#methode pour enregistrez a partire de la form RegisterForm
def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})




def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            error = "Username ou mot de passe incorrect"

            return render(request, 'core/login.html', {'error': error})

    return render(request, 'core/login.html')






def logout_view(request):

    logout(request)

    return redirect('home')




#methode pour mentrez les statistique des informations
def dashboard(request):

    total_services = Service.objects.count()
    total_users = User.objects.count()
    total_rdv = RendezVous.objects.count()

    stats = RendezVous.objects.values('statut').annotate(total=Count('statut'))

    labels = []
    data = []

    for s in stats:
        labels.append(s['statut'])
        data.append(s['total'])

    context = {
        'total_services': total_services,
        'total_users': total_users,
        'total_rdv': total_rdv,
        'labels': labels,
        'data': data,
    }

    return render(request, 'core/dashboard.html', context)
