from django.db.models.query import QuerySet
from wagtail.wagtailsearch.backends.elasticsearch import ElasticSearch, ElasticSearchQuery
from wagtail.wagtailsearch.index import class_is_indexed


class CustomElasticSearchQuery(ElasticSearchQuery):
    def __init__(self, queryset, query_string, fields=None, operator=None, order_by_relevance=True,
                 extra_raw_filters=None):
        super(CustomElasticSearchQuery, self).__init__(queryset, query_string, fields, operator, order_by_relevance)
        self.extra_raw_filters = extra_raw_filters

    def get_filters(self):
        filters = []

        # Filter by content type
        filters.append({
            'prefix': {
                'content_type': self.queryset.model.indexed_get_content_type()
            }
        })

        # Apply filters from queryset
        queryset_filters = self._get_filters_from_queryset()
        if queryset_filters:
            filters.append(queryset_filters)

        if self.extra_raw_filters:
            filters.extend(self.extra_raw_filters)

        return filters


class CustomElasticSearch(ElasticSearch):
    query_class = CustomElasticSearchQuery

    def __init__(self, params):
        super(CustomElasticSearch, self).__init__(params)

    def search(self, query_string, model_or_queryset, fields=None, filters=None,
               prefetch_related=None, operator=None, order_by_relevance=True, extra_raw_filters=None):
        # Find model/queryset
        if isinstance(model_or_queryset, QuerySet):
            model = model_or_queryset.model
            queryset = model_or_queryset
        else:
            model = model_or_queryset
            queryset = model_or_queryset.objects.all()

        # Model must be a class that is in the index
        if not class_is_indexed(model):
            return []

        # Check that theres still a query string after the clean up
        if query_string == "":
            return []

        # Apply filters to queryset
        if filters:
            queryset = queryset.filter(**filters)

        # Prefetch related
        if prefetch_related:
            for prefetch in prefetch_related:
                queryset = queryset.prefetch_related(prefetch)

        # Check operator
        if operator is not None:
            operator = operator.lower()
            if operator not in ['or', 'and']:
                raise ValueError("operator must be either 'or' or 'and'")

        # Search
        search_query = self.query_class(
            queryset, query_string, fields=fields, operator=operator,
            order_by_relevance=order_by_relevance, extra_raw_filters=extra_raw_filters
        )
        return self.results_class(self, search_query)
