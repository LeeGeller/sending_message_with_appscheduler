from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from users.models import User, Company


class Command(BaseCommand):
    def handle(self, *args, **options):

        company, created = Company.objects.get_or_create(company_name="Our company")

        # Создаем пользователя
        user, created = User.objects.get_or_create(
            email="manager@companny.ru",
            defaults={
                "user_company": company,
                "is_staff": True,
                "is_active": True,
            },
        )
        if created:
            user.set_password("12345")
            user.save()
            self.stdout.write(self.style.SUCCESS("Successfully created user."))

        try:
            group = Group.objects.get(name="managers")
            user.groups.add(group)
            self.stdout.write(
                self.style.SUCCESS("Successfully added user to managers group.")
            )
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR("Group managers does not exist."))

        user.save()
