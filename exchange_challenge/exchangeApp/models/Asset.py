from django.db import models
import uuid


class Asset(models.Model):
    asset_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    crypto = models.OneToOneField('Crypto', on_delete=models.CASCADE, related_name='assets') 
    stock = models.OneToOneField('Stock', on_delete=models.CASCADE, related_name='assets')
    
    # Otros campos de la tabla assets
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.name  # Para representar el objeto con el name

    class Meta:
        db_table = 'assets'