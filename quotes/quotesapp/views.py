from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm, TagForm
from .models import Author, Quote, Tag


# Create your views here.


def main(request):
    quotes = Quote.objects.filter().all()
    authors = Author.objects.filter().all()
    return render(request, 'quotesapp/index.html', context={'quotes': quotes, 'authors': authors})



@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST, instance=Tag())
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect(to='quotesapp:main')
        return render(request, 'quotesapp/author.html', context={'form': form})
    return render(request, 'quotesapp/tag.html', context={'form': TagForm()})

@login_required
def author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=Author())
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect(to='quotesapp:main')
    return render(request, 'quotesapp/author.html', context={'title': 'Authors', 'form': form})


@login_required
def quote(request):
    form = QuoteForm()
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/quote.html', {'form': form})
    return render(request, 'quotesapp/quote.html', {'form': form})

def detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotesapp/detail.html', {"author": author})