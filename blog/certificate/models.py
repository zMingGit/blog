from django.db import models


class CertificateManager(models.Manager):
    def invalid_certificate(self, login_id, pwd):
        return len(super(CertificateManager, self).filter(login_id=login_id,
                                                          pwd=pwd)) > 0


class Certificate(models.Model):
    login_id = models.CharField(max_length=50)
    pwd = models.CharField(max_length=32)
    objects = CertificateManager()
