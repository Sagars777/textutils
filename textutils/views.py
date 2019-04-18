from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #  TEXT and request
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    params = {}
    purpose = []

    # Operations to be performed on received text with respect to request
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += str(char)
        purpose.append('Removed Punctuaions')
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()
        purpose.append('To Upper Case')
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        purpose.append('New Line Remover')
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        purpose.append('Removed Extra Spaces')
        djtext = analyzed

    if charcount == 'on':
        analyzed = {}
        for char in djtext:
            if analyzed.get(char):
                analyzed[char] = analyzed[char] + 1
            else:
                analyzed[char] = 1
        purpose.append('Character Counter')
        djtext = analyzed

    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charcount!='on'):
        return HttpResponse("<h1>Error</h1>")

    params = {'purpose': purpose, 'analyzed_text': djtext}
    return render(request,'analyze.html',params)


def aboutus(request):
    return HttpResponse("<h1>This is about us page</h1>")