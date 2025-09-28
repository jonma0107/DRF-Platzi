from rest_framework.permissions import BasePermission


class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    # Verificar si el usuario está autenticado
    if not request.user.is_authenticated:
      return False

    # Si el usuario está en el grupo "pacientes"
    if request.user.groups.filter(name="doctores").exists():
      # Solo puede hacer GET (métodos de solo lectura)
      return request.method in ["GET", "HEAD", "OPTIONS"]

    # Si el usuario está en el grupo "administradores"
    elif request.user.groups.filter(name="administradores").exists():
      # Puede hacer todo (todos los métodos)
      return True

    # Si no está en ningún grupo, denegar acceso
    else:
      return False
