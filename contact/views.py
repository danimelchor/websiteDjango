from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse

from django.core.mail import send_mail

class ContactView(View):
    def get(self,request):
        return render(request, 'contact.html')

    def post(self,request):
        email_name = request.POST['name']
        email_email = request.POST['email']
        email_message = request.POST['message']

        send_mail(
            email_name,
            email_message + '\n\nSent by: ' + email_email,
            email_email,
            ['dmelchorwebsite@gmail.com']
        )

        return JsonResponse({ 'success': True }, status=200)
