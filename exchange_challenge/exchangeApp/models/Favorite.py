from django.db import models
import uuid

class Favorite(models.Model):
    favorite_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Relaciones con otros modelos (Foreign Keys)
    user = models.ForeignKey('User', on_delete=models.CASCADE,related_name='favorites')  # Relación con el modelo User
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='favorites')  # Relación con el modelo Asset
    
    # Otros campos de la tabla 'Favorites'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favorite {self.favorite_id} for User {self.user}"

    class Meta:
        db_table = 'favorites'  # Especificar el nombre de la tabla en la base de datos