from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# from django.template.loader import render_to_string

monthly_challenges = {
  "january": "January Challenge to learn django!",
  "february": "February Challenge to learn django!",
  "march": "March Challenge to learn django!",
  "april": "April Challenge to learn django!",
  "may": "May Challenge to learn django!",
  "june": "June Challenge to learn django!",
  "july": "July Challenge to learn django!",
  "august": "August Challenge to learn django!",
  "september": "September Challenge to learn django!",
  "october": "October Challenge to learn django!",
  "november": "November Challenge to learn django!",
  "december": None
}

# Create your views here.
def index(request):
  # list_items = ""
  months = list(monthly_challenges.keys())
  return render(request, "challenges/index.html", {"months": months})
  
  '''for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse("month_challenge", args=[month]) 
    list_items += f"<li><a href=\'{month_path}\'>{capitalized_month}</a></li>"
    
    
  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)'''

def monthly_challenge_by_number(request, month):
  months= list(monthly_challenges.keys())
  
  if month > len(months) or month < 1:
    return HttpResponseNotFound('<h1>Invalid month</h1>')
  
  redirect_month =months[month - 1]
  redirect_path = reverse("month_challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {"challenge_text": challenge_text, "month_name": month.capitalize()})
    # response_data = render_to_string("challenges/challenge.html")
    # return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound('<h1>This month is not supported</h1>')
  