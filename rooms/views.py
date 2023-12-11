from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, mail_admins
from django.urls import reverse_lazy
from .controles import search_edit_reservation, search_data, emailbody
from .models import Hotels, Rooms, Reservation
from .forms import ReservationForm
from datetime import timedelta, datetime
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Sum


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
    Class Based View to list rooms to each hotel
    """
    model = Hotels
    template_name = 'rooms/detailhotel.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs) -> object:
        """
        Method to create a new object 'rooms' inside the context
        :param kwargs: dict
        :return: object
        """
        context = super().get_context_data(**kwargs)
        context['rooms'] = Rooms.objects.filter(hotels=kwargs['object'])
        context['name_hotel'] = kwargs['object']
        return context


class ReservationCreateView(LoginRequiredMixin, CreateView):
    """
    Class Based View to create a reservation
    """
    template_name = "rooms/reservation.html"
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy("rooms:reservation_rooms")

    def post(self, request, *args, **kwargs) -> object:
        """
        Method to valid a reservation with base in some requirements
        :param request: object (default)
        :param args: tuple
        :param kwargs: dict
        :return: template
        """
        form = ReservationForm(data=request.POST)

        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            number_host = form.cleaned_data.get('number_host')
            if datetime.date(checkin) <= datetime.date(datetime.today()):
                messages.error(request, "This room can't be reserved in this date.")
            elif (datetime.date(checkin + timedelta(number_host))) - (datetime.date(datetime.today())) >= timedelta(30):
                messages.error(request, "This room can't be reserved more than 30 days in advance.")
            else:
                resp = search_data(day=checkin, number=number_host, room=kwargs['pk'])
                if all(resp[0]):
                    try:
                        insert_list = [
                            Reservation(client_user=request.user,
                                        checkin=checkin + timedelta(day),
                                        number_host=number_host,
                                        rooms=resp[1][0]) for day in range(0, number_host)]
                        Reservation.objects.bulk_create(insert_list)
                        messages.success(request, 'Room reserved Successfully')
                        title, msg, fromemail, listrecipient = emailbody(status=1, check=checkin, quantity=number_host,
                                                                         destination=request.user, property=resp[1][0])
                        send_mail(title, msg, fromemail, listrecipient, fail_silently=False)
                    except Exception as e:
                        mail_admins(
                            'email not sent',
                            f'Erro: {e}',
                            fail_silently=False,
                        )
                else:
                    messages.error(request, 'This room is not availabe on your selected dates')
        return render(request, "rooms/reservation.html", {'form': form})


class MyreservationListView(LoginRequiredMixin, ListView):
    """
    Class Based View to list all reservation to each user
    """
    model = Reservation
    template_name = 'rooms/personalreserve.html'

    def get_context_data(self, *, object_list=None, **kwargs) -> object:
        """
        Method to create a new object 'reservations' inside the context
        :param object_list: object (default)
        :param kwargs: dict
        :return: object
        """
        context = super().get_context_data(**kwargs)
        results = Reservation.objects.filter(client_user=self.request.user)
        value = sum([result.rooms.price for result in results])
        context['reservations'] = results
        context['total'] = 0.00 if value == 0 else value
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

    def post(self, request, *args, **kwargs) -> object:
        form = ReservationForm(data=request.POST)
        instance_room = Reservation.objects.filter(id=kwargs['pk'])[0]

        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            number_host = form.cleaned_data.get('number_host')
            if datetime.date(checkin) <= datetime.date(datetime.today()):
                messages.error(request, "O quarto não pode ser reservado nessa data.")
            elif (datetime.date(checkin + timedelta(number_host))) - (datetime.date(datetime.today())) >= timedelta(30):
                messages.error(request, "O quarto não pode ser reservado com data acima de 30 dias.")
            else:
                resp = search_edit_reservation(day=checkin, number=number_host, room=instance_room.rooms)
                if all(resp):
                    try:
                        insert_list = [
                            Reservation(client_user=request.user, checkin=checkin + timedelta(day),
                                        number_host=number_host,
                                        rooms=instance_room.rooms) for day in range(0, number_host)]
                        Reservation.objects.bulk_create(insert_list)
                        record = Reservation.objects.get(id=kwargs['pk'])
                        record.delete()
                        messages.success(request, 'O quarto foi reservado com sucesso.')
                        title, msg, fromemail, listrecipient = emailbody(status=2,
                                                                         check=checkin,
                                                                         quantity=number_host,
                                                                         destination=request.user,
                                                                         property=instance_room)
                        send_mail(title, msg, fromemail, listrecipient, fail_silently=False)
                    except Exception as e:
                        mail_admins(
                            'email not sent',
                            f'Erro: {e}',
                            fail_silently=False, )
                else:
                    messages.error(request, 'Esse quarto não esta disponível na data selecionada.')
        return render(request, "rooms/reservation.html", {'form': form})


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    """
    Class Based View to delete a reservation
    """
    model = Reservation
    success_url = reverse_lazy("rooms:list_hotels")
