from django.db import models


class DocumentStatus(models.TextChoices):
    ALTERED = "altered", "Altered"
    APPROVED = "approved", "Approved"
    NOT_CHECKED = "not_checked", "Not checked"
    NEED_CORRECTION = "need_correction", "Need correction"
