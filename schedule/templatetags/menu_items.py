from django import template

register = template.Library()


@register.inclusion_tag("schedule/menu_list.html", takes_context=True)
def get_users_menu(context):
    request = context.get("request")
    if request.user.is_authenticated:
        users_menu = [
            {"id": 3, "name": "Выйти", "templates": "users:logout"},
        ]
    else:
        users_menu = [
            {"id": 1, "name": "Войти", "templates": "users:login"},
            {"id": 2, "name": "Регистрация", "templates": "users:registration"},
        ]
    return {"users_menu": users_menu}
