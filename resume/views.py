from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def pdf_view(request):
    with open('/home/rj/myprojectdir/resume/templates/resume/RichJoseph.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
