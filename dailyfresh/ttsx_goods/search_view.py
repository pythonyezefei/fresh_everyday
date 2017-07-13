# coding=utf-8
from haystack.generic_views import SearchView


class MySearchView(SearchView):

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['title'] = '所有匹配商品'
        return context
