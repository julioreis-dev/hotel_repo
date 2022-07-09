from .models import Rooms, Reservation
from datetime import timedelta


def emailbody(**kwargs) -> tuple:
    """
    Function responsible to prepare body email
    :param kwargs: dict
    :return: tuple
    """
    if kwargs.get('status') == 1:
        title = f'Thank you for your reservation in our hotel'
        body = f'Dear client\nYour reservation is to: {kwargs.get("check")}\nThank you!!!'
        emailfrom = 'contato@firminostech.com'
        destination = [kwargs.get("destination")]
        response = title, body, emailfrom, destination
    else:
        title = f'Thank you for your update in our hotel'
        body = f'Dear client\nYour book update is to: {kwargs.get("check")}\nThank you!!!'
        emailfrom = 'contato@firminostech.com'
        destination = [kwargs.get("destination")]
        response = title, body, emailfrom, destination
    return response


def search_data(**kwargs) -> tuple:
    """
    Function to looking for check out registered
    :param kwargs: day, number, room
    :return: tuple
    """
    answer_list = []
    for i in range(0, kwargs.get('number')):
        out = Reservation.objects.filter(checkin=kwargs.get('day') + timedelta(i), rooms=kwargs.get('room'))
        answer_list.append(False if len(out) != 0 else True)
    return answer_list, Rooms.objects.filter(id=kwargs.get('room'))


def search_edit_reservation(**kwargs) -> list:
    """
    Function to check reservation used in edit reservation
    :param kwargs: day, number, room
    :return: tuple
    """
    answer_list = []
    for i in range(0, kwargs.get('number')):
        out = Reservation.objects.filter(checkin=kwargs.get('day') + timedelta(i), pk=kwargs.get('room'))
        answer_list.append(False if len(out) != 0 else True)
    return answer_list
