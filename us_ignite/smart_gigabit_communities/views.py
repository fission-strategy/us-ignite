# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template.response import TemplateResponse
from models import *
import random

# Create your views here.


def reverse_pitch(request):
    # "Static" text here. OPTIONAL
    intro = "US Ignite Will Convene Reverse Pitch Events Throughout the United States "
    desc = "US Ignite’s Reverse Pitch Competition turns the tables on the traditional competition by pitching challenges to you.<br><br>Local businesses, city governments, and civic organizations within Smart Gigabit Communities have the opportunity to present their problem statements to the wider community to curate fresh solutions.<br><br>Our Reverse Pitch events are focused on empowering the local change makers and idea generators out there to ideate and develop innovative gigabit applications solutions. Using our supportive platform, these ideas have a place to launch and have the chance to bring transformative benefits to their communities.<br><br>This year, US Ignite will co-sponsor up to 10 Reverse Pitch competitions.<br><br>Visit the webpages below to find out more information!"
    
    random_int = random.uniform(0.1, 2.0)
    pitch_list = Pitch.objects.filter(active=True).order_by('order').all()
    context = {
        'intro': intro,
        'desc': desc,
        'pitch_list': pitch_list,
        'random_int': random_int
    }

    return TemplateResponse(request, 'smart_gigabit_communities/reverse_pitch.html', context)
