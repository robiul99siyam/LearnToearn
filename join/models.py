from django.db import models


AGE = [
    ('15-20','15-20'),
    ('21-30','21-30'),
    ('31-40','31-40'),
    ('40+','40+'),
]

GENDER = [
    ("Male","Male"),
    ("Famale","Famale"),
    ("Other","Other"),
]

STAUS = [
    ("Student","Student"),
    ("Job","Job"),
    ("Unemployed","Unemployed"),
    ("Other","Other"),
]

LAPTOB = [
    ("Yes","Yes"),
    ("No","No"),
]
class JoinModel (models.Model):


    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    address= models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.CharField(choices=AGE,max_length=30)
    gander = models.CharField(choices=GENDER,max_length=30)
    status = models.CharField(choices=STAUS,max_length=30)
    laptob = models.CharField(choices=LAPTOB,max_length=30)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return  self.name
    