from django.db import models
import uuid

class Crypto(models.Model):
    crypto_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE, related_name='cryptos')
    
    # Otros campos de la tabla stock
    price = models.DecimalField(max_digits=10, decimal_places=4)
    web_page = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(auto_now_add=True)