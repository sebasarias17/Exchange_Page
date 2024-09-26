from django.db import models
import uuid

class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE, related_name='stocks')
    
    # Otros campos de la tabla stock
    price = models.DecimalField(max_digits=10, decimal_places=4)
    volume = models.IntegerField()
    web_page = models.CharField(max_length=120, null=True)
    created_at = models.DateTimeField(auto_now_add=True)