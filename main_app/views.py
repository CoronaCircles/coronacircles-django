from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .models import Event, User
from django.core.exceptions import ObjectDoesNotExist
from . import forms
import string, random
import re
import os

from django.core.mail import send_mail

from django.views.decorators.csrf import csrf_exempt

def convertStringToDateTime(string):
    return None

necessaryRegistrationData = ['username','email_address']
necessaryCircleHostData = ['name', 'event_start', 'host_email']

def apiEndpoint(request: HttpRequest, methods=['POST'], necessaryData=[]):
    try:
        if request.method in methods and request.POST:
            for nec in necessaryData:
                if nec not in request.POST:
                    return errorResponse()
        else:
            return errorResponse()
    except Exception as e:
        return errorResponse(504, 'Unknown error. Please contact us or try again later.')

def errorResponse(errorcode=403, text="Bad request."):
    return JsonResponse({
        'status': 'error',
        'info': text
    }, status=errorcode)

def createCircleIDString():
    letters = [*string.ascii_lowercase, *string.ascii_uppercase, *string.digits, string.whitespace]
    generatedString =  ''.join(random.choice(letters) for i in range(50))
    return generatedString

class reg_errors:
    NOT_ALL_DATA = {
        'errorcode': 1,
        'text': 'Not all neccessary Data provided.'
    }
    INVALID_EMAIL = {
        'errorcode': 2,
        'text': 'The emailaddress is invalid.'
    }
    EMAIL_EXISTS = {
        'errorcode': 3,
        'text': 'The email address already exsists'
    }
    EMAIL_EXISTS_WITH_OTHER_USERNAME = {
        'errorcode': 4,
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
        'text': 'It already exists a Circle with the same name.'
    }

# user endpoints
def registerUser(request):
    require = apiEndpoint(request, necessaryData=['email'])
    if require: return require

    # check if a user with that email address exists
    existingUser = User.objects.filter(email_address=request.POST['email'])
    if existingUser.exists():
        return errorResponse(**reg_errors.EMAIL_EXISTS)
    else:
        newUser = User(
            username=request.POST['u'],
            email_address=request.POST['e']
        )
        newUser.save()
        return JsonResponse({
            'status': 'success'
        })

def deleteUser(request):
    require = apiEndpoint(request, necessaryData=['email'])
    if require: return require

    # check if a user with that email address exists
    user = User.objects.filter(email_address=request.POST['email'])
    if user.exists():
        return
    else:
        errorResponse(-4, 'Email unknown.')

# Circle endpoints
@csrf_exempt
def hostCircle(request):
    require = apiEndpoint(request, ['POST'], necessaryCircleHostData)
    if require: return require
    
    # check if a circle with that name, event start and this host participant exists
    existingEvent = Event.objects.filter(
        name=request.POST['name']
    )
    if existingEvent.exists():
        return errorResponse(**host_errors.EVENT_ALREADY_EXISTS)
    else:
        newEvent = Event(
            name=request.POST['name'],
            event_start=request.POST['event_start'],
            participants=request.POST['host_email'],
            event_description=request.POST.get('description', '')
        )
        newEvent.save()
        return JsonResponse({
            'status': 'success'
        })

def deleteCircle(request):
    # TODO
    pass

def moveCircle(request):
    # TODO
    pass

def repeatCircle(request):
    # TODO
    pass

@csrf_exempt
def participateCircle(request):
    require = apiEndpoint(request, ['POST'], ['name', 'email'])
    if require: return require
    
    emailReg = re.search(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$', request.POST['email'])
    if not emailReg:
        return errorResponse()
    email = emailReg.group()

    # check if a circle with that name exists
    existingCircle = Event.objects.filter(
        name=request.POST['name']
    )
    if existingCircle.exists():
        circle = existingCircle.first()
        if not request.POST['email'] in circle.participants:
            circle.participants = ','.join([
                *circle.participants.split(','),
                request.POST['email']
            ])
            circle.save()
            sendConfirmationMail(email, circle.name)
            return JsonResponse({
                'status': 'success'
            })
        else:
            return errorResponse(errorcode=403, text="You already are a participant of this circle.")
    return errorResponse()

@csrf_exempt
def exitCircle(request):
    require = apiEndpoint(request, ['POST'], ["email", "name"])
    if require: return require
    
    emailReg = re.search(
        r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$',
        request.POST['email']
    )
    if not emailReg:
        return errorResponse()

    # check if a circle with that name exists
    existingCircle = Event.objects.filter(
        name=request.POST['name']
    )
    if existingCircle.exists():
        print("circle exists")
        circle = existingCircle.first()
        if request.POST['email'] in circle.participants:
            print("email exists in circle")
            participants = circle.participants.split(',')
            if request.POST['email'] == participants[0]:
                return errorResponse(-6, 'You can\'t exit a Circle which you are hosting.')
            participants.remove(request.POST['email'])
            circle.participants = ",".join(participants)
            circle.save()
            return JsonResponse({
                'status': 'success'
            })
    return errorResponse()


def sendEmail(subject, email, templateFilename, context):
    send_mail(
        "CoronaCircles: " + subject,
        open(os.path.join('main_app/email_templates/', templateFilename), 'r').read().format(**context),
        'noreply@coronacircles.com',
        [email],
        fail_silently=True
    )
    print("sending email to: ", email)

def sendConfirmationMail(emailAddress, circleName):
    sendEmail("Participantion Confirmation", emailAddress, 'participationConfirmation.html', {
        "circleName": circleName,
        "exitLink": "http://127.0.0.0:8000/de/api/circle/exit/"
    })