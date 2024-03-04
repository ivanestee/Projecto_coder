from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def message_list(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'message/message_list.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    return render(request, 'message/message_detail.html', {'message': message})

@login_required
def send_message(request):
    if request.method == 'POST':
        # Lógica para enviar un mensaje
        # Por ejemplo, obtener los datos del formulario y crear un nuevo mensaje
        # Aquí asumimos que ya tienes implementada la lógica para enviar mensajes
        return HttpResponseRedirect('/message/')
    else:
        # Renderizar el formulario para enviar un mensaje
        return render(request, 'message/send_message.html')

@login_required
def mark_as_read(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.is_read = True
    message.save()
    return HttpResponseRedirect('/message/')

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.delete()
    return HttpResponseRedirect('/message/')


