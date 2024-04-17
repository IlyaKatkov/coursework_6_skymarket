# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework import permissions
from rest_framework.permissions import BasePermission



class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='admin').exists():
            return True
        return obj.author == request.user


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsSelfUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user.email