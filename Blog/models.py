from django.db import models

# Blog Model
class BlogModel (models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="Blog/media/images")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return  self.title
    



RATING = [
    ("⭐","⭐"),
    ("⭐⭐","⭐⭐"),
    ("⭐⭐⭐","⭐⭐⭐"),
    ("⭐⭐⭐⭐","⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"),
]

class ReviewModel (models.Model):
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    rating = models.CharField(choices=RATING,max_length=30,default="⭐⭐⭐⭐⭐")
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return  self.name
    


