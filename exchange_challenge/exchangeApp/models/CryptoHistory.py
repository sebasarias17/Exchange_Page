from django.db import models
import uuid

class CryptoHistory(models.Model):
    history_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Relaciones con otros modelos (Foreign Keys)
    crypto = models.ForeignKey('Crypto', on_delete=models.CASCADE, related_name='cryptos_histories')  # Relación con el modelo Stock
    
    # Otros campos de la tabla stock history
    updated_at = models.DateTimeField(auto_now_add=True)