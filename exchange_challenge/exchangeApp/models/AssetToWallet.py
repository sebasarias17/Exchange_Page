from django.db import models



class AssetToWallet(models.Model):
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name='assets_to_wallet')  # Llave foránea a Wallet
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE,related_name='assets_to_wallet')  # Llave foránea a Asset

    class Meta:
        # Definir una llave compuesta utilizando wallet_id y asset_id
        unique_together = ('wallet', 'asset')

    def __str__(self):
        return f"{self.wallet} - {self.asset}"