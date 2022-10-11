from django.db import models

class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    how_to_donate = models.CharField(max_length=255)

    def __str__(self) -> str:
        """Str repr of this object."""
        return self.title