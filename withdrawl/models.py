from django.db import models

# Create your models here.
class Requests(models.Model):
    PlayerID = models.TextField()
    PaymentMethod = models.TextField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Transaction {self.id} by User {self.PlayerID}"