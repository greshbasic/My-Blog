from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from constants import NO_MONTH_MSG, MONTH_TO_CHALLENGE_MAP, NUM_TO_MONTH_MAP

# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = MONTH_TO_CHALLENGE_MAP[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse(NO_MONTH_MSG)

def monthly_challenge_by_number(request, month):
    redirect_month = NUM_TO_MONTH_MAP.get(month)
    if redirect_month:
        return HttpResponseRedirect("/challenges/" + redirect_month)
    else:
        return HttpResponse(NO_MONTH_MSG)