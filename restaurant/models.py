from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    def __str__(self):
        return f'{self.Name}:{str(self.No_of_guests)}'
    def get_Book(self):
        return f'{self.Name}:{str(self.BookingDate)}'
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.SmallIntegerField()
    def get_item(self):
        return f'{self.title}:{str(self.price)}'
    def __str__(self):
        return f'{self.title} : {self.price}'
    


