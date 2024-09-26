from django.db import models
import uuid

class Wallet(models.Model):
    wallet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Relaciones con otros modelos (Foreign Keys)
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='users')  # Relación con el modelo User

    # Otros campos de la tabla 'Wallets'
    balance = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    updated_at = models.DateTimeField(auto_now=True)  # Fecha y hora de actualización automática

    def __str__(self):
        return f"Wallet {self.wallet_id} for User {self.user}"

    class Meta:
        db_table = 'wallets' 