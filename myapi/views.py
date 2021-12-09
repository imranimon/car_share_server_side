from django.db import connection, transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'users': '/api/user/'
    }
    return Response(api_urls)


# @transaction.atomic
@api_view(['GET'])
def users(request):
    with connection.cursor() as cursor:
        cursor.execute('select * from benutzer')
        user_list = dictfetchall(cursor)
        return Response(user_list, status=status.HTTP_200_OK)
