from rest_framework.permissions import BasePermission


class IsApplicantOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_admin = request.user.is_staff
        is_applicant = obj.applicant == request.user

        if is_admin or is_applicant:
            return True

        return False


class IsApplicant(BasePermission):
    def has_object_permission(self, request, view, obj):
        is_applicant = obj.applicant == request.user

        if is_applicant:
            return True

        return False
