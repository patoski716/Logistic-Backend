from django.db import models

# Create your models here.

# Status = (
#     ('Parcel Has Been Received And It Is Ready For Shipping!', 'Parcel Has Been Received And It Is Ready For Shipping!'),
#     ('On Transit', 'On Transit'),
#     ('On Hold', 'On Hold'),
#     ('Shipped', 'Shipped'),
#     ('Package Arrived (On Clearance)', 'Package Arrived (On Clearance)'),
# )


class Timeline(models.Model):
    trackingid = models.CharField(max_length=10,null=True,default='')
    Date= models.DateField(null=False)
    Time= models.TimeField(null=False)
    Activity= models.CharField(max_length=200,null=False)
    Location= models.CharField(max_length=400,null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.trackingid


class Tracking(models.Model):
    trackingid = models.CharField(max_length=10,null=True, unique=True,default='')
    Estimated_Date_of_Departuer = models.DateField(null=False)
    Estimated_Date_of_Arrival = models.DateField(null=False)
    Sender_Name = models.CharField(max_length=400,null=False)
    Sender_Origin = models.CharField(max_length=200,null=False)
    From = models.CharField(max_length=400,null=False)
    To = models.CharField(max_length=400,null=False)
    Reciver_Name = models.CharField(max_length=400,null=False)
    Reciver_Email = models.EmailField(max_length=400,null=False)
    Reciver_Address = models.TextField(null=False)
    Reciver_Phone = models.CharField(max_length=200,null=False)
    Item_Description = models.CharField(max_length=200,null=False)
    Weight_And_Dimension = models.TextField(blank=True)
    timeline= models.ManyToManyField(Timeline,default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trackingid