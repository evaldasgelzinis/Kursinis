from django.db.models import *

class WorkPlace(Model):
    name = CharField(max_length=100)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SawBrand(Model): 
    workplace = ForeignKey(WorkPlace, on_delete=CASCADE)                                
    brand = TextField(max_length=100)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand

class Saw(Model):
    saw_brand = ForeignKey(SawBrand, on_delete=CASCADE)                                  
    name = TextField(max_length=100)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Meter(Model):
    PIRMA = 'PIRMA'
    ANTRA = 'ANTRA'
    TRECIA = 'TRECIA'
    PAMAINA_CHOICES = [
        (PIRMA, 'pirma'),
        (ANTRA, 'antra'),
        (TRECIA, 'trecia'),
    ]
    #laukeliai
    saw = ForeignKey(Saw, on_delete=CASCADE)                     
    metres = IntegerField(null=False)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)
    pamaina = CharField(
        choices=PAMAINA_CHOICES,
        default=PIRMA,
        max_length=100
    )

    def __str__(self):
        return self.saw.name


    

