from django.shortcuts import render, redirect
from django.contrib import messages
import json

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            # save data to json file
            data = form.cleaned_data
            try:
                with open('contact_data.json', 'a') as json_file:
                    json.dump(data, json_file)
                    json_file.write('\n')
            except Exception as e:
                messages.error(request, 'Error Saving Data')
                
            messages.success(request, "Thanks for completing the form. We'll be in touch soon!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form
    }
        
    return render(request, 'contactapp/contact.html', context)
