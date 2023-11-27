from django.db import models


class ApplicationStatus(models.TextChoices):
    SENT = "sent"
    APPROVED = "approved"
    REJECTED = "rejected"
    NEED_CORRECTION = "need_correction"

    def __str__(self) -> str:
        return self.value
