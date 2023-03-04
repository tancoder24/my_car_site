from django.shortcuts import render, redirect
from . forms import ReviewForm
from django.urls import reverse

# Create your views here.
def rental_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('car:thank_you'))

    else:
        form = ReviewForm()
        return render(request, 'car/rental_review.html', context={'form': form})

def thank_you(request):
    return render(request, 'car/thank_you.html')