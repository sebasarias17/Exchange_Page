from django.db import models
import uuid

class TransactionHistory(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    offer = models.OneToOneField('Offer', on_delete=models.CASCADE,related_name='transaction_histories')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    wallet_id_client = models.CharField(max_length=255, null=False)
    wallet_id_publisher = models.CharField(max_length=255, null=False)
    