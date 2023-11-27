from django.db import models
from apps.applications.models.category import ApplicationCategory
from apps.applications.models.status import ApplicationStatus


class Application(models.Model):
    applicant = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="applications",
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.SENT,
    )

    sent_date = models.DateTimeField(auto_now_add=True)
    check_date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        ApplicationCategory, on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"Applicantion: {self.id} / status: {self.status} / category: {self.category.title}"

    def update_status(self, new_status):
        if new_status in ApplicationStatus:
            self.status = new_status
        else:
            raise Exception("Invaid status!")
