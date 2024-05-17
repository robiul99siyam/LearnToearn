from django.db import models

class ContactModel (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return  self.name
    
