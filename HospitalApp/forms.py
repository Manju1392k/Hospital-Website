
from django.forms import ModelForm

from .models import BookingAppointment

class BookingAppointmentForm(ModelForm):
    class Meta:
        model = BookingAppointment
        fields = ['Patient_Name', 'Doctor', 'Date']