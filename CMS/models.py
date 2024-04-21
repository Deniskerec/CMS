from django.db import models


#1 ... need to migrate to push it python manage.py makemigrations
#2 ... now push the migration into the database python manage.py migrate
class Records(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    month = models.IntegerField()
    year = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=False)
    amount = models.IntegerField()
    amount_in_cents = models.FloatField()
    net_in_cents = models.FloatField()
    km_food_in_cents = models.FloatField()
    ljublana_trips = models.IntegerField()
    est_trips = models.IntegerField()

    def __str__(self):
        return f"Record {self.id} created at {self.created_at} month {self.month} year {self.year} amount {self.amount}"
