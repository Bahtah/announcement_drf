from rest_framework import pagination


class AnnouncementPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'per_page'