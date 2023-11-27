from datetime import datetime
from django.db import models


class ApplicationPeriod(models.Model):
    title = models.CharField(
        verbose_name="Period name",
        max_length=255
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def has_valid_duration(self):
        current_date = datetime.now().date()
        return self.start_date <= current_date <= self.end_date

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Application Period"
        verbose_name_plural = "Application Periods"
