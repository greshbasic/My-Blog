from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from constants import MONTH_TO_CHALLENGE_MAP, NUM_TO_MONTH_MAP

# Create your views here.
def monthly_challenge(request, month):
    try:
        challenge_text = MONTH_TO_CHALLENGE_MAP[month.lower()]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return render(request, "challenges/bad_month.html")

def monthly_challenge_by_number(request, month):
    redirect_month = NUM_TO_MONTH_MAP.get(month)
    if redirect_month:
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return render(request, "challenges/bad_month.html")
    
def index(request):
    return render(request, "challenges/index.html", {
        "months": list(MONTH_TO_CHALLENGE_MAP.keys())
    })