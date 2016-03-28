from django.db import models


class VisitingDate(models.Model):

    def __str__(self):
        return '{}'.format(self.date)

    date = models.DateField(primary_key=True)


class VisitingIP(models.Model):

    def __str__(self):
        return self.ip_address

    ip_address = models.GenericIPAddressField(primary_key=True)


class Visitor(models.Model):

    def __str__(self):
            return 'IP: {} date: {}'.format(
                self.visiting_ip,
                self.visiting_date)

    visiting_ip = models.ForeignKey(VisitingIP)
    visiting_date = models.ForeignKey(VisitingDate)
