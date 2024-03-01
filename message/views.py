from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Message

def message_list(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messages/message_list.html', {'messages': messages})

def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    return render(request, 'messages/message_detail.html', {'message': message})

def send_message(request):
    if request.method == 'POST':
        # Lógica para enviar un mensaje
        # Por ejemplo, obtener los datos del formulario y crear un nuevo mensaje
        # Aquí asumimos que ya tienes implementada la lógica para enviar mensajes
        return HttpResponseRedirect('/messages/')
    else:
        # Renderizar el formulario para enviar un mensaje
        return render(request, 'messages/send_message.html')

def mark_as_read(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.read = True
    message.save()
    return HttpResponseRedirect('/messages/')

def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.delete()
    return HttpResponseRedirect('/messages/')
