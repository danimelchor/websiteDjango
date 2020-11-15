from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse

from django.core.mail import send_mail

class ContactView(View):
    def get(self,request):
        return render(request, 'contact.html')

    def post(self,request):
        bounded_form = EmailForm(request.POST)

        if bounded_form.is_valid():
            email_name = bounded_form['name']
            email_email = bounded_form['email']
            email_message = bounded_form['message']

            send_mail(
                email_name,
                email_message,
                email_email,
                ['dmelchorwebsite@gmail.com']
            )

            return JsonResponse({ 'success': True }, status=200)
