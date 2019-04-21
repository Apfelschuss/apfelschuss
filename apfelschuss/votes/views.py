from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from apfelschuss.votes.models import Voting


def search(request):
    queryset = Voting.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'votes/search_results.html', context)


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


def voting(request, slug):
    voting = get_object_or_404(Voting, slug=slug)
    context = {
        'voting': voting
    }
    return render(request, 'votes/single.html', context)
