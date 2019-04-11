from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from apfelschuss.votes.models import Voting

def get_category_count():
    queryset = Voting \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

def featured(request):
    featured = Voting.objects.filter(featured=True)
    context = {
        'object_list': featured
    }
    return render(request, 'votes/featured.html', context)

def archive(request):
    category_count = get_category_count()
    voting_list = Voting.objects.all()
    paginator = Paginator(voting_list, 3)
    page_request_var = 'page'
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
         paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count': category_count,
    }
    return render(request, 'votes/archive.html', context)

def voting(request, id):
    return render(request, 'votes/single.html', {})
