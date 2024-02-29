# signals.py
# from django.contrib.auth.models import User  # Esta línea debe ser eliminada o comentada si está en el nivel superior

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.utils.timezone import now

@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    from django.contrib.auth.models import User  # Mueve la importación aquí dentro
    """Actualiza el campo last_login cada vez que un usuario inicie sesión."""
    User.objects.filter(pk=user.pk).update(last_login=now())
