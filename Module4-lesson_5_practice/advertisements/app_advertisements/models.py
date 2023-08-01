from django.db import models


class Project(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        verbose_name='ID'
    )

    title = models.CharField(
        max_length=100,
        verbose_name='Name'
    )

    description = models.TextField(
        verbose_name="description"
    )

    prise = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Price'
    )

    auction = models.BooleanField(
        default=False,
        verbose_name='auction'
    )

    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of publication'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of update'
    )

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id}, title={self.title}, price={self.prise})'

    class Meta:
        db_table = 'advertisements'
