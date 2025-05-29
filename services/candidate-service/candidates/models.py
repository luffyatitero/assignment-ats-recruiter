from django.db import models


GENDER_CHOICES = (
    ('Male', 'male'),
    ('Female', 'female'),
    ('Other', 'other'),
)


class Candidate(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        verbose_name = "Candidate"
        verbose_name_plural = "Candidates"
