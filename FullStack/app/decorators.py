from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def superuserRrequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="app:index"):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def agentRrequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="app:index"):
    actual_decorator = user_passes_test(
        lambda u: u.is_active
        and ((u.is_agent and u.is_varified) or u.is_superuser),
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def customerRrequired(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="app:index"):
    actual_decorator = user_passes_test(
        lambda u: u.is_active
        and ((u.is_customer and u.is_varified) or u.is_superuser),
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator