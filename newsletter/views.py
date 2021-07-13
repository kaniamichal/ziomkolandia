from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from .forms import JoinForm

#
# def newsletter(request):
#     if request.method == "POST":
#         form = JoinForm(request.POST)
#         email = request.POST.get('newsletter_email', '')
#         print(email)
#         if form.is_valid():
#             join = form.save(commit=False)
#             join.newsletter_email = email
#             print(email)
#             join.newsletter_timestamp = timezone.now()
#             join.save()
#             return redirect('thanks')
#     else:
#         form = JoinForm()
#     return render(request, 'website/base.html', {'form': form})
