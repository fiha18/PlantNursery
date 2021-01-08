from django.db import models


# Create your models here.
class Plants(models.Model):
    plant_name = models.CharField(max_length=40, unique=True)
    origin = models.CharField(max_length=20)

    def upload_image(self, filename):
        path = 'Nursery/photos/{}'.format(filename)
        return path

    Image = models.ImageField(upload_to=upload_image, null=False, blank=False)

    def __str__(self):
        return self.plant_name


# User Many to Many Relationship between Plants and Nursery
class Nursery(models.Model):
    name = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20, null= False, blank= False,default='password123')
    location = models.CharField(max_length=40)
    Plant_name = models.ManyToManyField(Plants, through='NurseryPlant')

    def __str__(self):
        return self.name


class NurseryPlant(models.Model):
    nursery_name = models.ForeignKey(Nursery, on_delete=models.CASCADE)
    plant_name = models.ForeignKey(Plants, on_delete=models.CASCADE)
    price = models.IntegerField(null= False, blank= False)



# User Many to Many Relationship between Plants and User
class Users(models.Model):
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, null= False, blank= False, default='password123')
    age = models.IntegerField(default=18)
    plant_name = models.ManyToManyField(Plants, through='UserPlant')

    def __str__(self):
        return "User: {} {}".format(self.first_name, self.last_name)


class UserPlant(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    nursery_name = models.ForeignKey(Nursery, on_delete=models.CASCADE)
    plant_name = models.ForeignKey(Plants, on_delete=models.CASCADE)
