from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPageNumberPagination(PageNumberPagination):
    page_size = 5

    # change the pagination query param present in the url
    page_query_param = "p"

    # Client can decide how many items he or she wants to see.
    page_size_query_param = "records"

    # give a constraint that an user can request upto only 7 records in each request. i.e., records < 7
    # max_page_size = 7

    # last_page_strings = 'end'

    # customize response of paginator
    # def get_paginated_response(self, data):
    #     return Response(
    #         {
    #             "total_students": self.page.paginator.count,
    #             "total_pages": self.page.paginator.num_pages,
    #             "current_page": self.page.number,
    #             "students": data,
    #         }
    #     )


# **********************

# http://localhost:8000/studentapi/?p=1&records=10

# http://localhost:8000/studentapi/?p=2&records=6

# **********************

# http://localhost:8000/studentapi/?p=last       # default last page string

# http://localhost:8000/studentapi/?p=end       # set using last_page_strings = 'end'

# **********************
