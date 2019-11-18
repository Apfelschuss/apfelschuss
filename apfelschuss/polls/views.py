from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from apfelschuss.polls.models import Category, Poll


def category_latest(request):
    '''
    Returns latest category that is published and its polls
    that are published.
    '''
    try:
        category_latest = Category.objects.filter(status='published').latest('poll_date')
        polls = category_latest.poll_set.filter(status='published')
    except Category.DoesNotExist:
        category_latest = None
        polls = None
    context = {
        'category_latest': category_latest,
        'polls': polls
    }
    return render(request, 'polls/category_latest.html', context)


def search(request):
    '''
    Search query in poll title and description and returns
    poll objects.
    '''
    queryset = Poll.objects.filter(status='published')
    query = request.GET.get('q')
    if query:
        if request.LANGUAGE_CODE == 'de':
            queryset = queryset.filter(
                Q(title_de__icontains=query) |
                Q(description_de__icontains=query)
            ).distinct()
        elif request.LANGUAGE_CODE == 'fr':
            queryset = queryset.filter(
                Q(title_fr__icontains=query) |
                Q(description_fr__icontains=query)
            ).distinct()
        elif request.LANGUAGE_CODE == 'it':
            queryset = queryset.filter(
                Q(title_it__icontains=query) |
                Q(description_it__icontains=query)
            ).distinct()
        elif request.LANGUAGE_CODE == 'rm':
            queryset = queryset.filter(
                Q(title_rm__icontains=query) |
                Q(description_rm__icontains=query)
            ).distinct()
        elif request.LANGUAGE_CODE == 'en':
            queryset = queryset.filter(
                Q(title_en__icontains=query) |
                Q(description_en__icontains=query)
            ).distinct()
    context = {
        'polls': queryset
    }
    return render(request, 'polls/search_results.html', context)


def get_category_count():
    '''
    Counts number of polls in every category. Returns all categories
    and quantity of its polls.
    '''
    queryset = Poll \
        .objects \
        .values('category__poll_date') \
        .annotate(Count('category__poll_date'))
    return queryset


def featured(request):
    '''
    Retunrs all polls models with featured=True.
    '''
    featured = Poll.objects.filter(status='published').filter(featured=True)
    context = {
        'polls': featured
    }
    return render(request, 'polls/featured.html', context)


def archive(request):
    '''
    Returns all published poll models paginated including category count.
    '''
    category_count = get_category_count()
    poll_list = Poll.objects.filter(status='published')
    paginator = Paginator(poll_list, 20)
    page_request_var = 'page'
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'polls': paginated_queryset,
        'page_request_var': page_request_var,
        'category_count': category_count,
    }
    return render(request, 'polls/archive.html', context)


def poll(request, slug):
    '''
    Takes slug of single poll and returns that poll object in
    corresponding language.
    '''
    if request.LANGUAGE_CODE == 'de':
        poll = get_object_or_404(Poll, status='published', slug_de=slug)
    elif request.LANGUAGE_CODE == 'fr':
        poll = get_object_or_404(Poll, status='published', slug_fr=slug)
    elif request.LANGUAGE_CODE == 'it':
        poll = get_object_or_404(Poll, status='published', slug_it=slug)
    elif request.LANGUAGE_CODE == 'rm':
        poll = get_object_or_404(Poll, status='published', slug_rm=slug)
    elif request.LANGUAGE_CODE == 'en':
        poll = get_object_or_404(Poll, status='published', slug_en=slug)
    context = {
        'poll': poll
    }
    return render(request, 'polls/single.html', context)
