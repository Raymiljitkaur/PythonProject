from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here for Books


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    bookauthor = models.CharField(max_length=200)
    bookprice = models.IntegerField()

    def __str__(self):
        return self.bookname
    class Meta:
      db_table = "books"
    
class Patron(models.Model):
    patronfname = models.CharField(max_length=200)
    patronlname = models.CharField(max_length=200)
    patronemail = models.EmailField(max_length=70, blank=True)
    patronphone = models.CharField(max_length=12)
    patronaddress = models.CharField(max_length=200)

    def __str__(self):
        return self.patronfname
    class Meta:
      db_table = "patrons"


# model for category

class Category(models.Model):
    categoryname = models.CharField(max_length=200)
    categorydescription = models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname
    class Meta:
      db_table = "categories"
   


class Issuebook(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    patron = models.ForeignKey(Patron,on_delete=models.CASCADE)
    issuedate = models.DateField(default=datetime.now(), blank=True)
    expirydate = models.DateField()

    def __unicode__(self):
        return "Issued to: " + self.patron

    class Meta:
      db_table = "issuedbooks"

    # model for Publisher
class Publisher(models.Model):
        publisherfname = models.CharField(max_length=200)
        publisherlname = models.CharField(max_length=200)
        publisheremail = models.EmailField(max_length=70, blank=True)
        publisherphone = models.CharField(max_length=12)


        def __str__(self):
            return   self.publisherfname

        class Meta:
            db_table = "publishers"