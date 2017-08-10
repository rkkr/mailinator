from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.template import loader, Context
from emails.models import *

def mail_list(request):
    emails = Message.objects.all().order_by('-id')
    paginator = Paginator(emails, 100)
    page = request.GET.get('page', 1)

    try:
        emails = paginator.page(page)
    except PageNotAnInteger:
        emails = paginator.page(1)
    except EmptyPage:
        emails = paginator.page(paginator.num_pages)
    
    template = loader.get_template('mail_list.html')
    context = Context({'emails': emails, 'paginator': paginator})
    return HttpResponse(template.render(context))

def mail_view(request, mail_id):
    email_body = get_object_or_404(Message, pk=mail_id).body
    return HttpResponse(cgi.escape(email_body))
