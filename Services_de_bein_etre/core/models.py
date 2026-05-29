from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    duree = models.IntegerField()
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.nom


class RendezVous(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()

    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('confirme', 'Confirmé'),
            ('annule', 'Annulé')
        ],
        default='en_attente'
    )

    def __str__(self):
        return f"{self.client.username} - {self.service.nom}"