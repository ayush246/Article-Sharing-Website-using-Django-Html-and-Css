from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to="images/")
    icon=models.ImageField(upload_to="images/")
    votes_total=models.IntegerField(default=1)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)
    """stores id_number of the particular user , this property is 
    pointing towards a different model so key used is ForeignKey
    Delete cascasde is used so if a user deletes their account then
    the info related to that user is also deleted"""
    def summary(self):
        return self.body[:100]
    def __str__(self):
        return self.title