from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создаем группу менеджеров, если она еще не существует
        managers_group, created = Group.objects.get_or_create(name="managers")

        permissions_list = [
            "can_view_newsletter",
            "can_disable_newsletter",
            "can_view_users_list",
            "can_block_users",
            "cannot_change_newsletter_list",
            "cannot_change_textfornewsletter_list",
            "cannot_change_client_list",
        ]

        for perm in permissions_list:
            try:
                permission = Permission.objects.get(codename=perm)
                managers_group.permissions.add(permission)
                self.stdout.write(
                    self.style.SUCCESS(f"Permission {perm} added to group managers.")
                )
            except Permission.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f"Permission {perm} does not exist.")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created/updated group "managers" with specified permissions.'
            )
        )
