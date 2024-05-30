from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self):
        managers_group = Group.objects.create(name="managers")

        permissions_list = [
            "can_view_newsletter",
            "can_disable_newsletter",
            "cannot_manage_newsletter_list",
            "cannot_change_textfornewsletter_list",
            "cannot_change_newsletter_list",
            "can_view_user_list",
            "can_block_users",
        ]

        for perm in permissions_list:
            try:
                permission = Permission.objects.get(codename=perm)
                managers_group.objects.add(permission)
            except Permission.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Permission {permission} does not exist.")
                )
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created/updated group "moderators" with specified permissions.'
                )
            )
