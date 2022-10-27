from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .forms import NewCommentForm
from .models import Ticket, Comentario


# Create your views here.

def home(request):

    all_tickets = Ticket.newmanager.all()

    return render(request, 'index.html', {'tickets': all_tickets})


def ticket_single(request, ticket):

    ticket = get_object_or_404(Ticket, slug=ticket, status='published')

    comments = NewCommentForm

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.ticket = ticket
            user_comment.save()
            return HttpResponseRedirect('/' + ticket.slug)
    else:
        comment_form = NewCommentForm()

    return render(request, 'single.html', {'ticket': ticket,
                                           'comments': user_comment,
                                           'comments': comments,
                                           'comment_form': comment_form
                                           })
