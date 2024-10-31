from django.db import models


# Create your models here.
class Marksheets(models.Model):
    examination = models.CharField(max_length=50)
    center = models.CharField(max_length=70)
    semBranch = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    registrationNo = models.CharField(max_length=10)


class Marks(models.Model):
    # Theory Marks
    computer = models.IntegerField()
    physics = models.IntegerField()
    mathematics = models.IntegerField()
    electrical_Electronics = models.IntegerField()

    # Practical marks
    practical_Physics = models.IntegerField()
    practical_Eng = models.IntegerField()

    # Internal Marks
    internal_Computer = models.IntegerField()
    internal_Physics = models.IntegerField()
    internal_Maths = models.IntegerField()
    internal_Elect_Electronics = models.IntegerField()

    # Calculation
    subTotalComputer = models.IntegerField(default=True)
    subTotalPhysics = models.IntegerField(default=True)
    subTotalMathematics = models.IntegerField(default=True)
    subTotalElectrical = models.IntegerField(default=True)

    # sessional
    sessional = models.IntegerField(default=True)

    # Calculation
    total = models.IntegerField()
    result = models.CharField(max_length=5)
