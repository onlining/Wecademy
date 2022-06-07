from django.db import models

class Order(TimeStampModel):
    user    = models.ForeignKey("users.User", on_delete=models.CASCADE)
    lecture = models.ForeignKey("lectures.Lecture", on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"