from django.db import models

class KZzone(models.Model):
    city = models.CharField(max_length=100)
    zone = models.IntegerField()

    class Meta:
        verbose_name = 'KZ zone'

    def __str__(self):
        # return self.city
        return str(self.zone)


class RUSzone(models.Model):
    city = models.CharField(max_length=100)
    zone = models.IntegerField()

    class Meta:
        verbose_name = 'RUS zone'

    def __str__(self):
        return str(self.zone)

class TariffFromKZtoRUS(models.Model):
    from_zone = models.ForeignKey(KZzone, on_delete=models.CASCADE)
    to_zone = models.ForeignKey(RUSzone, on_delete=models.CASCADE)
    index = models.IntegerField()

    def __str__(self):
        return 'RUS '+ str(self.from_zone.zone) + ' - KZ ' + str(self.to_zone.zone)


class Calculator(models.Model):
    weight = models.CharField(max_length=100)
    index = models.IntegerField()
    cost = models.IntegerField()
