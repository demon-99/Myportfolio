from django.db import models

class Projects(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=100)
    link=models.CharField(max_length=1000,default="")
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    image = models.ImageField(upload_to='proj/images', default="")

    def __str__(self):
        return self.title + " by " + self.author
