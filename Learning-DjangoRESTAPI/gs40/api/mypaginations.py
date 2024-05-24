from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 6
    # ordering = "name"
    ordering = "id"

    # cursor_query_param = "CUR"  # Chnage the cursor param
