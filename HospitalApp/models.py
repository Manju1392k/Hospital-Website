from django.db import models

from datetime import date

# Create your models here.

Doctortypes = (
    ('Not Selected', 'Not Selected'),
    ('Dr One', 'Dr. Raj Kumar (Psychiatrist)'),
    ('Dr Two', 'Dr. Shiva (Radiologist)'),
    ('Dr Three', 'Dr. Ravi (Nerologist)'),
)

class BookingAppointment(models.Model):
    Patient_Name = models.CharField(max_length=150, default='')
    Doctor = models.CharField(max_length=150, choices=Doctortypes, default='Not Selected')
    Date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return self.Patient_Name