from rest_framework.pagination import PageNumberPagination


class SmallNopage(PageNumberPagination):
    page_size = 1
