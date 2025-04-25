import os
import sys

def main():
    """Ponto de entrada principal para comandos do Django."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alvos.alvo_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar Django. Verifique se está instalado e disponível no seu ambiente."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
