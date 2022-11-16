from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from teammembers.models import Member
from rest_framework.decorators import api_view
from teammembers.serializers import MemberSerializer


@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        member_serializer = MemberSerializer(members, many=True)
        return JsonResponse(member_serializer.data, safe=False)

    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def member_detail(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return JsonResponse({'message': 'The member does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.update(member, member_serializer.data)
            return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        print('delete')
        member.delete()
        return JsonResponse({'message': 'Delete successfully!'}, status=status.HTTP_204_NO_CONTENT, safe=False)
