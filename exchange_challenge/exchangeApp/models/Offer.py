from django.db import models
import uuid

class Offer(models.Model):
    offer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Relaciones con otros modelos (Foreign Keys)
    publisher = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='offers')  # Relación con el modelo Wallet
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='offers')  # Relación con el modelo Asset

    # Campos específicos de la tabla 'Offer'
    OFFER_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    order_type = models.CharField(max_length=4, choices=OFFER_TYPES, default='buy')  # Enumeración para tipo de oferta
    price = models.DecimalField(max_digits=10, decimal_places=4)  # Campo para el precio con precisión decimal
    