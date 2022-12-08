from django.views.generic import ListView
from uitshare_main.models import (
    Category,
    Course,
)
from django.db.models import Q
from uitshare_main.helpers import get_all_categories
from itertools import chain



class SearchView(ListView):
    template_name = "search/search.html"
    context_object_name = "search_result_list"
    count = 0
    
    def get_context_data(self, **kwargs):
        context_arguments = super().get_context_data(**kwargs)
        context_arguments["title"] = "Search / UIT Share"
        context_arguments["category_list"] = get_all_categories
        context_arguments["count"] = self.count
        context_arguments["query_string"] = self.request.GET.get("q")
        return context_arguments
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query is not None:
            look_up = Q(name__unaccent__trigram_word_similar=query)
            from_category = Category.objects.filter(look_up).distinct()
            from_course = Course.objects.filter(look_up).distinct()
            queryset_chain = chain(from_category, from_course)
            qs = sorted(queryset_chain, 
                        key=lambda instance: instance.pk, 
                        reverse=True)
            self.count = len(qs)
            return qs
        return None
