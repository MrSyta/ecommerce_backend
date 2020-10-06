import operator
import csv


from django.contrib import admin
from .models import Book
from django.contrib.admin.utils import lookup_needs_distinct
from django.db import models
from functools import reduce
from django.http import HttpResponse


class RegexModelAdmin(admin.ModelAdmin):

    # code coming from django 1.6
    def get_search_results(self, request, queryset, search_term):
        """
        Returns a tuple containing a queryset to implement the search,
        and a boolean indicating if the results may contain duplicates.
        """
        # Apply keyword searches.
        def construct_search(field_name):
            if field_name.startswith('^'):
                return "%s__istartswith" % field_name[1:]
            elif field_name.startswith('='):
                return "%s__iexact" % field_name[1:]
            elif field_name.startswith('@'):
                return "%s__search" % field_name[1:]
            elif field_name.startswith('/') and field_name.endswith('/') and len(field_name) > 2:
                return "%s__regex" % field_name[1:-1]
            else:
                return "%s__icontains" % field_name

        use_distinct = False
        if self.search_fields and search_term:
            orm_lookups = [construct_search(str(search_field))
                           for search_field in self.search_fields]
            for bit in search_term.split():
                or_queries = [models.Q(**{orm_lookup: bit})
                              for orm_lookup in orm_lookups]
                queryset = queryset.filter(reduce(operator.or_, or_queries))
            if not use_distinct:
                for search_spec in orm_lookups:
                    if lookup_needs_distinct(self.opts, search_spec):
                        use_distinct = True
                        break

        return queryset, use_distinct


class ExportCsv:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response


@admin.register(Book)
class BookAdmin(RegexModelAdmin, ExportCsv):
    search_fields = ['/title/']
    actions = ["export_as_csv"]
