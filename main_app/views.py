from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from .models import Event, User
from django.core.exceptions import ObjectDoesNotExist



def convertStringToDateTime(string):
    return None

necessaryRegistrationData = ['u','e']
necessaryEventHostData = ['title', 'event_start', 'host_user', 'description']


class reg_errors:
    NOT_ALL_DATA = {
        'errorcode': 1,
        'text': 'Not all neccessary Data provided.'
    }
    INVALID_EMAIL = {
        'errorcode': 2,
        'text': 'The emailaddress is invalid.'
    }
    EMAIL_EXISTS_WITH_OTHER_USERNAME = {
        'errorcode': 3,
        'text': 'The email-address already exists, but with another username. Please type in your last username to confirm.'
    }
class host_errors:
    NOT_ALL_DATA = {
        'errorcode': -1,
        'text': 'Not all neccessary Data provided.'
    }
    USER_NOT_EXISTS = {
        'errorcode': -2,
        'text': 'The emailaddress is not existing. Please provide a username to register.'
    }
    EVENT_ALREADY_EXISTS = {
        'errorcode': -3,
        'text': 'It already exists an event with the same name at the same time.'
    }

# endpoint to registrate
def registerUser(request):
    try:
        if request.method == 'POST' and request.POST:
            for nec in necessaryRegistrationData:
                if not nec in request.POST:
                    return JsonResponse({
                        'status': 'error',
                        "info": reg_errors.NOT_ALL_DATA
                    })
            
            # check if there already exists a user with the same email and username
            existingUser = User.objects.filter(email_address=request.POST['e'], username__regex=f"´^((?!{request.POST['u']}).)*$")
            if existingUser.exists():
                return JsonResponse({
                    'status': 'error',
                    'info': reg_errors.EMAIL_EXISTS_WITH_OTHER_USERNAME
                })
            else:
                newUser = User(
                    username=request.POST['u'],
                    email_address=request.POST['e']
                )
                newUser.save()
                return JsonResponse({
                    'status': 'success'
                })
        else:
            return JsonResponse({
                'status': 'error',
                'info': {
                    'errorcode': 403,
                    'text': 'Bad request.'
                }
            })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            "info": {
                'errorcode': '504',
                'text': 'Unknown error. Please contact us.'
            }
        })


# endpoint to start an event
def hostEvent(request):
    try:
        if request.method == 'POST' and request.POST:
            for nec in necessaryEventHostData:
                if nec not in request.POST:
                    return JsonResponse({
                        'status': 'error',
                        'info': host_errors.NOT_ALL_DATA
                    })
            existingEvent = User.objects.filter(
                name=request.POST['title'],
                event_start=convertStringToDateTime(request.POST['event_start']),
                participants__contains=request.POST['host_user']
            )
            if existingEvent.exists():
                return JsonResponse({
                    'status': 'error',
                    'info': host_errors.EVENT_ALREADY_EXISTS
                })
            else:
                if not User.objects.filter(email_address=request.POST['host_user']).exists():
                    return JsonResponse({
                        'status': 'error',
                        'info': host_errors.USER_NOT_EXISTS
                    })
                newEvent = Event(
                    name=request.POST['title'],
                    event_start=convertStringToDateTime(request.POST['event_start']),
                    participants=request.POST['host_user'],
                    event_description=request.POST['description'] if request.POST['description'] else ''
                )
                newEvent.save()
                return JsonResponse({
                    'status': 'success'
                })
        else:
            return JsonResponse({
                'status': 'error',
                'info': {
                    'errorcode': 403,
                    'text': 'Bad request.'
                }
            })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            "info": {
                'errorcode': '504',
                'text': 'Unknown error. Please contact us or try again later.'
            }
        })