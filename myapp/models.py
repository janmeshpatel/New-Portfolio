from django.db import models

# Create your models here.

class Home(models.Model):
    Name = models.CharField(max_length=200, default='')
    Surname = models.CharField(max_length=200, default='')

    Overview = models.CharField(max_length=200, default='')
    Twitter = models.CharField(max_length=200, default='')
    Facebook = models.CharField(max_length=200, default='')
    Instagram = models.CharField(max_length=200, default='')
    Linkedin = models.CharField(max_length=200, default='')
    Github = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Personal_Information(models.Model):
    Name = "Personal Information"
    Image = models.ImageField(upload_to='media',default='')
    DOB = models.CharField(max_length=200, default='')
    Age = models.CharField(max_length=200, default='')
    Website = models.CharField(max_length=200, default='')
    Education = models.CharField(max_length=200, default='')
    Phone = models.CharField(max_length=200, default='')
    Email = models.CharField(max_length=200, default='')
    City = models.CharField(max_length=200, default='')
    Freelance = models.CharField(max_length=200, default='')

    Nationality = models.CharField(max_length=200, default='')
    Gender = models.CharField(max_length=200, default='')
    Status = models.CharField(max_length=200, default='')
    Language = models.CharField(max_length=200, default='')
    Hobbies = models.CharField(max_length=200, default='')


    HappyClient = models.CharField(max_length=200, default='')
    Project = models.CharField(max_length=200, default='')
    GithubRepo = models.CharField(max_length=200, default='')
    Certificates = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Skill(models.Model):
    sid = models.CharField(max_length=200, default='')
    Name = models.CharField(max_length=200, default='')
    Percent = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Interest(models.Model):
    Name = models.CharField(max_length=200, default='')
    Classname = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Testimonials(models.Model):
    Name = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to='media',default='')
    Description = models.CharField(max_length=200, default='')
    Title = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Profile(models.Model):
    Name = models.CharField(max_length=200, default='')
    Description = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Education(models.Model):
    Name = models.CharField(max_length=200, default='')
    Year = models.CharField(max_length=200, default='')
    College = models.CharField(max_length=200, default='')
    Board = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Career(models.Model):
    Name = models.CharField(max_length=200, default='')
    Project_Name = models.CharField(max_length=200, default='')
    Tools = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Category(models.Model):
    Name = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Project(models.Model):
    Name = models.CharField(max_length=200, default='')
    Category = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to='media',default='')
    Gif2 = models.ImageField(upload_to='media',default='')
    Gif3 = models.ImageField(upload_to='media',default='')
    Gif4 = models.ImageField(upload_to='media',default='')
    Project_Date = models.CharField(max_length=200, default='')
    Project_Url = models.CharField(max_length=200, default='')
    Description = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name

class Temp(models.Model):
    Name = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.Name



