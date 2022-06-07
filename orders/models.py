from django.db   import models

from cors.models import TimeStampedModel

class Order(TimeStampedModel):
    user    = models.ForeignKey("users.User", on_delete=models.CASCADE)
    lecture = models.ForeignKey("lectures.Lecture", on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"