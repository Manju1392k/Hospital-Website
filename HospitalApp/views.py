from django.shortcuts import redirect, render

from .forms import BookingAppointmentForm

from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Book(request):
    form = BookingAppointmentForm
    if request.method == 'POST':
        form = BookingAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Appointment is successful submitted')
            return redirect('book')
    return render(request, 'booking.html' , {'form':form})
