# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from forms import ContactForm
from django.conf import settings


def home(request):

    context = RequestContext(request)



    return render_to_response('common/home.html', locals(), context)

def terms(request):
    return render_to_response('terms.html', context_instance= RequestContext(request))

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'),
                ['tom@modern-carpentry.com'],
                fail_silently=False
            )

            return HttpResponseRedirect('/contact/thanks/')
    else :
        form = ContactForm()

    return render_to_response('site_contact.html', locals(), context_instance=RequestContext(request))


def contact_thanks(request):
    print 'contact thanks!!!'
    return render_to_response('site_contact_thanks.html',locals(),context_instance=RequestContext(request))

def handle_error404(request):
    return render_to_response('error/handle_error404.html', locals(), context_instance=RequestContext(request))

def handle_error500(request):
    return render_to_response('error/handle_error500.html', locals(), context_instance=RequestContext(request))