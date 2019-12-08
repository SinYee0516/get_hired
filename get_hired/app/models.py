from django.db import models
from django.db.models import DateField


class User(models.Model):

    Name = models.CharField(max_length=255)
    Birthday = models.DateField()
    Contact_number = models.CharField(max_length=11)
    Address = models.CharField(max_length=255)
    Education = models.CharField(max_length=255)
    Skills = models.CharField(max_length=255)
    Username = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=255)
    Role = models.IntegerField()

    def __str__(self):
        return self.Name


class Job(models.Model):

    Title = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Open = models.DateField()
    Close = models.DateField()
    Salary = models.IntegerField()
    Categories = models.IntegerField()

    def __str__(self):
        return self.Title


class Company(models.Model):

    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


class Status(models.Model):

    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Company_ID = models.ForeignKey(Company, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Current_Status = models.CharField(max_length=255)

    def __str__(self):
        return self.Current_Status


class Saved(models.Model):

    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Company_ID = models.ForeignKey(Company, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Saved = models.IntegerField()

    def __int__(self):
        return self.Saved


class Message(models.Model):

    Job_ID = models.ForeignKey(Job, on_delete=models.CASCADE)
    Message = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)

    def __str__(self):
        return self.Title
