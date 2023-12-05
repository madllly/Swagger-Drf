from django.db import models


class Car(models.Model):
    name = models.CharField("Car's name", max_length=30, default='None', blank=False, null=False)
    year = models.DateField("Year of issue", blank=False, null=False)
    color = models.CharField("Car's color", max_length=30, default='None', blank=False, null=False)
    vin_number = models.CharField("Car's vim", max_length=17, default='None', blank=False, null=False)
    owner = models.ForeignKey("Client", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.year}, {self.color}, {self.vin_number}'

    class Meta:
        verbose_name = "Client's car"
        verbose_name_plural = "Client's cars"


class Client(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    middle_name = models.CharField('Middle name', max_length=30, null=True)
    date_of_birth = models.DateField('Date of birth')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = "Client information"
        verbose_name_plural = "Client information"


class Worker(models.Model):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    middle_name = models.CharField('Middle name', max_length=30, null=True)
    job_title = models.CharField('Job title')
    date_of_birth = models.DateField('Date of birth')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        verbose_name = "Worker information"
        verbose_name_plural = "Worker information"


class ListOfWork(models.Model):
    work_name = models.CharField("Work's name")
    price = models.FloatField('Price')

    def __str__(self):
        return f'{self.work_name}, {self.price}'

    class Meta:
        verbose_name = "List of work"
        verbose_name_plural = "List of work"


class OrderList(models.Model):
    car = models.ForeignKey("Car", on_delete=models.PROTECT)
    worker = models.ForeignKey("Worker", on_delete=models.PROTECT)
    list_of_work = models.ForeignKey('ListOfWork', on_delete=models.PROTECT)
    data = models.DateField('Date')

    def __str__(self):
        return f'{self.car}, {self.data}'

    class Meta:
        verbose_name = "Order List"
        verbose_name_plural = "Order list"
