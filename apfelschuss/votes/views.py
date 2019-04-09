from django.shortcuts import render

from apfelschuss.votes.models import Voting

def voting(request):
    featured = Voting.objects.filter(featured=True)
    context = {
        'object_list': featured
    }
    return render(request, 'votes/voting.html', context)

def archive(request):
    voting_list = Voting.objects.all()
    context = {
        'voting_list': voting_list
    }
    return render(request, 'votes/archive.html', context)
