from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Offer
from .forms import TaskForm


# Create your views here.

# Functional based view

def homepage(request):
    if request.method == "GET":
        offers = Offer.objects.all()
        return render(
            request,
            "offers/homepage.html",
            {
                "offers": offers,
            },
        )

# Create a task
def offer_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("offers:offer_list"))
    else:
        form = TaskForm()

    return render(
        request,
        "offers/offer_form.html",
        {
            "form": form,
        },
    )


# Retrieve task list
def offer_list(request):
    if request.method == "GET":
        depart = request.GET.get('depart', '')
        print('depart',depart)
        arrival = request.GET.get('arrival', '')
        print('arrival',arrival is None, arrival =="")
        if depart != "" or arrival != "": 
            if depart == "":
                offers = Offer.objects.filter(arrival = arrival)
            if arrival=="":
                offers = Offer.objects.filter(depart = depart)
            if depart != "" and arrival != "": 
                offers = Offer.objects.filter(depart = depart, arrival = arrival)
        else:
            offers = Offer.objects.all()
        print(offers)
        return render(
            request,
            "offers/offer_list.html",
            {
                "offers": offers,
            },
        )


# Retrieve a single task
def offer_detail(request, pk):
    if request.method == "GET":
        offer = get_object_or_404(Offer, pk=pk)
        return render(
            request,
            "offers/offers_detail.html",
            {
                "offer": offer,
            },
        )


# Update a single task
def offer_update(request, pk):
    task_obj = get_object_or_404(Offer, pk=pk)
    if request.method == "POST":
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                reverse(
                    "offers:offer_detail",
                    args=[
                        pk,
                    ],
                )
            )
    else:
        form = TaskForm(instance=task_obj)

    return render(
        request, "offers/offer_form.html", {"form": form, "object": task_obj}
    )


# Delete a single task
def offer_delete(request, pk):
    task_obj = get_object_or_404(Offer, pk=pk)
    task_obj.delete()
    return redirect(reverse("offers:offer_list"))

# search

def offer_search(request):
    if request.method == "GET":
        # depart = request.GET.get('depart', '')
        # arrival = request.GET.get('arrival', '')
        # offers = Offer.objects.filter(depart =depart, arrival = arrival)
        offers = Offer.objects.all()
        return render(
            request,
            "offers/homepage.html",
            {
                "offers": offers,
            },
        )


# Class Based Views
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )


# class PromotionListView(ListView):
#     model = Task
#     context_object_name = "tasks"


# class PromotionDetailView(DetailView):
#     model = Task


# class PromotionCreateView(CreateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy("tasks:task_list")


# class PromotionUpdateView(UpdateView):
#     model = Task
#     form_class = TaskForm
#     success_url = reverse_lazy("tasks:task_list")


# class PromotionDeleteView(DeleteView):
#     model = Task
#     success_url = reverse_lazy("tasks:task_list")
