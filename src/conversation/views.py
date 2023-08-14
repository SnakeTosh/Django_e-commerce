from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from django.contrib.auth.decorators import login_required

from .models import Conversation 
from .form import ConversationMessageForm

@login_required
def new_conversation(request, item_pk):

    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user :
        return redirect('dashboard:index')

    #conversations = Conversation.objects.filter(item=item).get(members__in=[request.user])
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user])

    if conversations :
        #print(type(conversations))
        return redirect('conversation:detail', pk=conversations.last().id)
     

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save

        
            conversation_messages = form.save(commit=False)
            conversation_messages.conversation = conversation
            conversation_messages.created_by = request.user
            conversation_messages.save()

            return redirect('item:detail', pk=item_pk)

    else :
        form = ConversationMessageForm()

        return render(request, 'conversation/new.html',{
            'form':form
        })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user]).get(pk=pk)
    print(type(conversation))
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_messages = form.save(commit=False)
            conversation_messages.conversation = conversation
            conversation_messages.created_by = request.user
            conversation_messages.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)

    else :
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form':form
    })
