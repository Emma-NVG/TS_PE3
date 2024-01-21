from django.shortcuts import render
from .models import Message

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
import os

def index(request):
    return HttpResponse("Hello, World!")

def submit_message(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        receiver_name = request.POST.get('receiver_name')
        message_content = request.POST.get('message_content')

        Message.objects.create(sender_name=sender_name, receiver_name=receiver_name, message_content=message_content)

    return render(request, 'submit_message.html')

def get_messages(request):
    messages = None

    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        if sender_name:
            messages = Message.objects.filter(sender_name=sender_name).order_by('-created_at')[:20]

    return render(request, 'get_messages.html', {'messages': messages})

def test_responses(request):
    # HttpResponse
    response1 = HttpResponse("This is a basic HttpResponse.")

    response2 = HttpResponseRedirect('/firstapp/get_messages/')

    response3 = HttpResponseNotFound("404 Not Found")

    all_responses = [
        response1.content.decode('utf-8'),  # Decode bytes to string
        response2.content.decode('utf-8'),  # Decode bytes to string
        response3.content.decode('utf-8')   # Decode bytes to string
    ]

    combined_response = HttpResponse("\n".join(all_responses))

    return combined_response


