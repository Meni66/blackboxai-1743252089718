from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class UserTypes(models.TextChoices):
        ADMIN = 'ADMIN', _('Administrator')
        COLLECTOR = 'COLLECTOR', _('Collection Staff')
        USER = 'USER', _('Regular User')
    
    user_type = models.CharField(
        max_length=10,
        choices=UserTypes.choices,
        default=UserTypes.USER
    )
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class Report(models.Model):
    WASTE_TYPES = (
        ('ELECTRONICS', 'Electronic Devices'),
        ('BATTERIES', 'Batteries'),
        ('APPLIANCES', 'Appliances'),
    )
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SCHEDULED', 'Scheduled'),
        ('COLLECTED', 'Collected'),
    )
    COLLECTION_POINTS = (
        ('MAIN', 'Main Collection Center'),
        ('NORTH', 'Northside Drop-off'),
        ('EAST', 'Eastside Collection'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPES)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    collection_point = models.CharField(max_length=20, choices=COLLECTION_POINTS)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    image = models.ImageField(upload_to='report_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_waste_type_display()} report by {self.user.username}"
