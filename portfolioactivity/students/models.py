from django.db import models

class Students(models.Model):
    # Define the fields for the Students model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    year = models.IntegerField()  # This field is like (1, 2, 3, 4)
    block = models.CharField(max_length=10)  #This field is like (Block A, B , C , E, etc.)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"