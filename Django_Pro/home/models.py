from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)    
    password = models.CharField(max_length=100)

#Only making model class doesn't mean table is created, we have deal 
#with migrations command(its generates sql query ) and we run migrate
# cmd to execute query



#DELETED DATA 
class DeletedUser(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)    
    password = models.CharField(max_length=100)



#Lets register model class in admin.py(not necessary in this case)

#Try To make Deleted Record page:
#class DeletedRecord(models.Model):
#    model_name = models.CharField(max_length=100)
#    record_id = models.PositiveIntegerField()
#    deleted_at = models.DateTimeField(auto_now_add=True)

#    def __str__(self):
#        return f"{self.model_name} (ID: {self.record_id})"