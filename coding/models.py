from django.db import models

# Create your models here.
class read(models.Model):
    id=models.IntegerField(default=1,primary_key=True)
    count=models.IntegerField(default=0)
    def increase(self):
        self.count += 1
        self.save(update_fields=['count'])