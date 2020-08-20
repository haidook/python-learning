from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import json
import random
import datetime

from .forms import NewsForm, SearchForm


# Create your views here.
def read_json_to_dict():
    with open(settings.NEWS_JSON_PATH) as f:
        data = json.load(f)
        dict_data = {}
        for x in data:
            # print(x['link'])
            if x['created'][:10] in dict_data:
                dict_data[x['created'][:10]].append(x)
            else:
                dict_data.setdefault(x['created'][:10], [])
                dict_data[x['created'][:10]].append(x)
    return dict_data


def read_json_to_list():
    with open(settings.NEWS_JSON_PATH) as f:
        data = json.load(f)
    return data

class MainView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/news/')


class NewsView(View):
    def find_search(self):
        data = read_json_to_list()
        titles = [x['title'] for x in data]
        return titles

    def get(self, request, *q, **kwargs):
        form = SearchForm(request.GET)
        titles = self.find_search()
        # print(titles)
        # i get the value i need to search for
        q = form['q'].value()
        # print(f'{q=}')
        if q:
            matches = [x for x in titles if q.lower() in x.lower()]
            if len(matches) > 0:
                data = read_json_to_list()
                print(f'{data=}')
                print(f'{matches=}')
                data = read_json_to_dict()
                search_data = {}
                for date, news in data.items():
                    for x in news:
                        # print(f'{x=}')
                        # print(f"{x['title']=}")
                        # print(f'{q=}')
                        search_data.setdefault(x['created'][:10], [])
                        if q.lower() in x['title'].lower():
                            search_data[x['created'][:10]].append(x)
                context = {
                    'form': form,
                    'data': search_data
                }
                # print(f'{search_data=}')
                return render(request, "news/index.html", context=context)
            else:
                context = {
                    'form': form,
                    'data': None
                }
                return render(request, "news/index.html", context=context)

        else:
            data = read_json_to_dict()
            context = {
                'form': form,
                'data': data
            }
            # print(f'{context=}')
            return render(request, "news/index.html", context=context)


class CreateNewsView(View):
    def get(self, request, *args, **kwargs):
        form = NewsForm()
        return render(request, "news/create.html", {'form': form})

    def post(self, request, *args, **kwargs):
        data = read_json_to_list()
        link = random.randint(0, 100)
        links = [x['link'] for x in data]
        while link in links:
            link = random.randint(0, 100)
        date = datetime.datetime.now().strftime("%Y-%m-%d %X")
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            new_data = {
                "created": str(date),
                "text": text,
                "title": title,
                "link": link
            }
            data.append(new_data)
            # print(data)
            with open(settings.NEWS_JSON_PATH, 'w') as f:
                json.dump(data, f)
            return HttpResponseRedirect('/news/')


class SingleNews(View):
    def get(self, request, link, **kwargs):
        data = read_json_to_dict()
        for date, news in data.items():
            for x in news:
                if link == x['link']:
                    context = x
                    # print(f'{context=}')
        return render(request, "news/news.html", context=context)
