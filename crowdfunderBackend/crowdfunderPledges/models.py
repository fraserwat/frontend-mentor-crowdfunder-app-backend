from django.db import models


class Pledge(models.Model):
    """
    All pledges to calculate amounts on frontend
    """

    id = models.AutoField(primary_key=True)
    reward = models.IntegerField()
    amount = models.FloatField()

    def __str__(self) -> str:
        return f"{self.id} [reward={self.reward}, amount={self.amount}]"
