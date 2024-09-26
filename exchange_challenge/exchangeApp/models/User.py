from django.db import models
import uuid

# Modelo para la tabla 'Users'
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.OneToOneField('Wallet', on_delete=models.CASCADE, related_name='users')
    
    # Otros campos de la tabla users
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True) 
    email = models.EmailField(max_length=50, unique=True)   
    password = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.username  # Para representar el objeto como el username en los admin y consultas

    class Meta:
        db_table = 'users' 