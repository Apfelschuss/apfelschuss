from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from apfelschuss.votes.models import Category, Voting


def category_latest(request):
    '''Returns latest category that is published and its votes
    that are published.
    '''
    try:
        category_latest = Category.objects.filter(status=1).latest('voting_date')
        votes = category_latest.voting_set.filter(status=1)
    except Category.DoesNotExist:
        category_latest = None
        votes = None
    context = {
        'category_latest': category_latest,
        'votes': votes
    }
    return render(request, 'votes/category_latest.html', context)


def search(request):
    '''Search query in voting title and description and returns
    voting objects.
    '''
    queryset = Voting.objects.filter(status=1)
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'votes/search_results.html', context)


def get_category_count():
    '''Counts number of votings in every category. Returns all categories
    and quantity of its votings.
    '''
    queryset = Voting \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset


def featured(request):
    '''Retunrs all voting models with featured=True.
    '''
    featured = Voting.objects.filter(status=1).filter(featured=True)
    context = {
        'queryset': featured
    }
    return render(request, 'votes/featured.html', context)


def archive(request):
    '''Returns all published voting models paginated including category count.
    '''
    category_count = get_category_count()
    voting_list = Voting.objects.filter(status=1)
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
    '''Takes slug of single voting and returns that voting object in
    corresponding language.
    '''
    if request.LANGUAGE_CODE == 'de':
        voting = get_object_or_404(Voting, status=1, slug_de=slug)
    elif request.LANGUAGE_CODE == 'fr':
        voting = get_object_or_404(Voting, status=1, slug_fr=slug)
    elif request.LANGUAGE_CODE == 'it':
        voting = get_object_or_404(Voting, status=1, slug_it=slug)
    elif request.LANGUAGE_CODE == 'rm':
        voting = get_object_or_404(Voting, status=1, slug_rm=slug)
    elif request.LANGUAGE_CODE == 'en':
        voting = get_object_or_404(Voting, status=1, slug_en=slug)
    context = {
        'voting': voting
    }
    return render(request, 'votes/single.html', context)
