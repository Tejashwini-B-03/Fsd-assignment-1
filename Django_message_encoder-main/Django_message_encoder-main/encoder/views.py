# encoder/views.py

from django.shortcuts import render
from .forms import EncodeMessageForm
from .utils import encode_message_odd_day, encode_message_even_day

def encode_message(request):
    if request.method == 'POST':
        form = EncodeMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            day_type = form.cleaned_data['day_type']
            if day_type == 'odd':
                encoded_message = encode_message_odd_day(message)
            else:
                encoded_message = encode_message_even_day(message)
            return render(request, 'encoded_message.html', {'encoded_message': encoded_message})
    else:
        form = EncodeMessageForm()
    return render(request, 'encode_message.html', {'form': form})
