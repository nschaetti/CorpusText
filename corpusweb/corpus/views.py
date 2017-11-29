# -*- coding: utf-8 -*-

# Imports
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime

# Home view
def home(request):
    """
    Example for HTML page, not validate for the example to be simple
    :param request:
    :return:
    """
    return render(request, 'corpus/home.html')
# end home


# View text
def view_text(request, id_text):
    """
    View to show a text knowing its ID
    :param request:
    :param id_text:
    :return:
    """
    return HttpResponse(
        "Vous avez demandé l'article #{0} !".format(id_text)
    )
# end view_text


# View to list articles
def list_texts(request, year):
    """
    View texts for a specific year
    :param request:
    :param year:
    :return:
    """
    # Test year
    if int(year) > 2017:
        raise Http404
    # end if

    # Send response
    return HttpResponse(
        "Vous avez demandé les articles de {0}".format(year)
    )
# end list_texts


# Current time
def current_time(request):
    """
    Current time
    :param request:
    :return:
    """
    return render(request, 'corpus/date.html', {'date': datetime.now()})
# end current_time


# Addition
def addition(request, nombre1, nombre2):
    """
    Addition
    :param request:
    :param nombre1:
    :param nombre2:
    :return:
    """
    total = int(nombre1) + int(nombre2)
    return render(request, 'corpus/addition.html', locals())
# end addition
