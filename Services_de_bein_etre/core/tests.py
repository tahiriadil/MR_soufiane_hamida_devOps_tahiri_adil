from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Service, RendezVous
import datetime


class ServiceModelTest(TestCase):

    def setUp(self):
        self.service = Service.objects.create(
            nom="Massage",
            description="Massage relaxant",
            prix=150.00,
            duree=60
        )

    def test_service_creation(self):
        """Test que le service est créé correctement"""
        self.assertEqual(self.service.nom, "Massage")
        self.assertEqual(self.service.prix, 150.00)
        self.assertEqual(self.service.duree, 60)

    def test_service_str(self):
        """Test la représentation string du service"""
        self.assertEqual(str(self.service), "Massage")


class ServiceViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.service = Service.objects.create(
            nom="Spa",
            description="Soin spa",
            prix=200.00,
            duree=90
        )

    def test_home_page(self):
        """Test que la page accueil répond 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_service_list_page(self):
        """Test que la liste des services répond 200"""
        response = self.client.get(reverse('service_list'))
        self.assertEqual(response.status_code, 200)

    def test_service_detail_page(self):
        """Test que le détail d'un service répond 200"""
        response = self.client.get(reverse('service_detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 200)


class RendezVousModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.service = Service.objects.create(
            nom="Relaxation",
            description="Séance relaxation",
            prix=100.00,
            duree=45
        )
        self.rdv = RendezVous.objects.create(
            client=self.user,
            service=self.service,
            date=datetime.date.today() + datetime.timedelta(days=1),
            heure=datetime.time(10, 0),
            statut='en_attente'
        )

    def test_rdv_creation(self):
        """Test que le rendez-vous est créé correctement"""
        self.assertEqual(self.rdv.statut, 'en_attente')
        self.assertEqual(self.rdv.client.username, 'testuser')

    def test_rdv_str(self):
        """Test la représentation string du rendez-vous"""
        self.assertEqual(str(self.rdv), "testuser - Relaxation")


class AuthTest(TestCase):

    def test_register_page(self):
        """Test que la page register répond 200"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Test que la page login répond 200"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)