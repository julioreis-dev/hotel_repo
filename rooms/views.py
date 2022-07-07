from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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
    """
    Class Based View to render a template
    """
    template_name = 'home/index.html'


class HotelsListView(LoginRequiredMixin, ListView):
    """
    Class Based View to list hotels
    """
    model = Hotels
    template_name = 'rooms/listhotels.html'
    context_object_name = 'hotels'


class HotelDetailView(LoginRequiredMixin, DetailView):
    """
    Class Based View to list rooms each hotel
    """
    model = Hotels
    template_name = 'rooms/detailhotel.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        """
        Method to create a new object 'rooms' inside the context
        :param kwargs: dict
        :return: object
        """
        context = super().get_context_data(**kwargs)
        context['rooms'] = Rooms.objects.filter(hotels=kwargs['object'])
        return context


def search_data(day, number, room):
    """
    Method to looking for check out registered
    :param day: datetime
    :param number: int
    :param room: int
    :return: tuple
    """
    answer_list = []
    for i in range(0, number):
        out = Reservation.objects.filter(checkin=day + timedelta(i), rooms=room)
        answer_list.append(False if len(out) != 0 else True)
    return answer_list, Rooms.objects.filter(id=room)


class ReservationCreateView(LoginRequiredMixin, CreateView):
    """
    Class Based View to create a reservation
    """
    template_name = "rooms/reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy("rooms:reservation_rooms")

    def post(self, request, *args, **kwargs):
        """
        Method to valid a reservation with base in some requirements
        :param request: default
        :param args: tuple
        :param kwargs: dict
        :return: template
        """
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            number_host = form.cleaned_data.get('number_host')
            if datetime.date(checkin) == datetime.date(datetime.today()):
                messages.error(request, 'This room is not availabe to be reserved today.')
            elif (datetime.date(checkin + timedelta(number_host))) - (datetime.date(datetime.today())) >= timedelta(30):
                messages.error(request, "This room can't be reserved more than 30 days in advance.")
            else:
                # resp = list(map(search_data, [checkin + timedelta(i) for i in range(0, number_host)]))
                resp = search_data(checkin, number_host, kwargs['pk'])
                if all(resp[0]):
                    insert_list = [
                        Reservation(client_user=request.user, checkin=checkin + timedelta(day), number_host=number_host,
                                    rooms=resp[1][0]) for day in range(0, number_host)]
                    Reservation.objects.bulk_create(insert_list)
                    messages.success(request, 'Room reserved Successfully')
                    # return HttpResponseRedirect(reverse_lazy('rooms:home_rooms'))
                else:
                    messages.error(request, 'This room is not availabe on your selected dates')
        return render(request, "rooms/reservation.html", {'form': form})


class MyreservationListView(LoginRequiredMixin, ListView):
    """
    Class Based View to list all reservation to each user
    """
    model = Reservation
    template_name = 'rooms/personalreserve.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Method to create a new object 'reservations' inside the context
        :param object_list: default
        :param kwargs: dict
        :return: object
        """
        context = super().get_context_data(**kwargs)
        context['reservations'] = Reservation.objects.filter(client_user=self.request.user)
        return context


class RoomsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Class Based View to update a reservation
    """
    template_name = "rooms/reservation.html"
    model = Reservation
    context_object_name = 'review'
    success_url = reverse_lazy("rooms:list_hotels")
    form_class = ReservationForm

    def post(self, request, *args, **kwargs):
        form = ReservationForm(data=request.POST)
        instance_room = Reservation.objects.filter(id=kwargs['pk'])[0]

        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            number_host = form.cleaned_data.get('number_host')
            if datetime.date(checkin) == datetime.date(datetime.today()):
                messages.error(request, 'This room is not availabe to be reserved today.')
            elif (datetime.date(checkin + timedelta(number_host))) - (datetime.date(datetime.today())) >= timedelta(30):
                messages.error(request, "This room can't be reserved more than 30 days in advance.")
            else:
                resp = search_data(checkin, number_host, kwargs['pk'])
                if all(resp[0]):
                    insert_list = [
                        Reservation(client_user=request.user, checkin=checkin + timedelta(day), number_host=number_host,
                                    rooms=instance_room.rooms) for day in range(0, number_host)]
                    Reservation.objects.bulk_create(insert_list)
                    record = Reservation.objects.get(id=kwargs['pk'])
                    record.delete()
                    messages.success(request, 'Room reserved Successfully')
                else:
                    messages.error(request, 'This room is not availabe on your selected dates')
        return render(request, "rooms/reservation.html", {'form': form})


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class Based View to delete a reservation
    """
    model = Reservation
    success_url = reverse_lazy("rooms:list_hotels")
