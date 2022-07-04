from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Hotels, Rooms, Reservation
from .forms import ReservationForm
from datetime import timedelta, datetime
from django.contrib import messages
from django.shortcuts import render
from users.models import User


class HomepageView(TemplateView):
    template_name = 'home/index.html'


class HotelsListView(LoginRequiredMixin, ListView):
    model = Hotels
    template_name = 'rooms/listhotels.html'
    context_object_name = 'hotels'


class HotelDetailView(LoginRequiredMixin, DetailView):
    model = Rooms
    template_name = 'rooms/detailhotel.html'
    context_object_name = 'rooms'


def search_data(day):
    answer = Reservation.objects.filter(checkin=day)
    if len(answer) != 0:
        return False
    else:
        return True


class ReservationCreateView(LoginRequiredMixin, CreateView):
    template_name = "rooms/reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy("rooms:reservation_rooms")

    def post(self, request, *args, **kwargs):
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            number_host = form.cleaned_data.get('number_host')
            if datetime.date(checkin) == datetime.date(datetime.today()):
                messages.error(request, 'This room is not availabe to be reserved today.')
            elif (datetime.date(checkin + timedelta(number_host))) - (datetime.date(datetime.today())) >= timedelta(30):
                messages.error(request, "This room can't be reserved more than 30 days in advance.")
            else:
                resp = list(map(search_data, [checkin + timedelta(i) for i in range(0, number_host)]))
                if all(resp):
                    insert_list = [
                        Reservation(client_user=request.user, checkin=checkin + timedelta(day), number_host=number_host)
                        for day in range(0, number_host)]
                    Reservation.objects.bulk_create(insert_list)
                    messages.success(request, 'Room reserved Successfully')
                    # return HttpResponseRedirect(reverse_lazy('rooms:home_rooms'))
                else:
                    messages.error(request, 'This room is not availabe on your selected dates')
        return render(request, "rooms/reservation.html", {'form': form})


class MyreservationListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'rooms/personalreserve.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(client_user=self.request.user)
        return context


class RoomsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "rooms/updatereservation.html"
    model = Reservation
    # fields = ['checkin', 'number_host']
    context_object_name = 'review'
    success_url = reverse_lazy("rooms:list_hotels")
    form_class = ReservationForm

