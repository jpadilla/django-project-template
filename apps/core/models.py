from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at')
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
