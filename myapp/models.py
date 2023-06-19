from django.db import models

class Proyect(models.Model):
      name = models.CharField(max_length=50)
      def __str__(self):
          return self.name
      
      

class Tasks(models.Model):
      title = models.CharField(max_length=50)
      description: models.TextField()
      proyect = models.ForeignKey(Proyect, on_delete=models.CASCADE)
      
      def __str__(self):
          return self.title
      