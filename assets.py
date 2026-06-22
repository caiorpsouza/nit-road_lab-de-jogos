import os
import sys


def resource_path(caminho_relativo):
    """Resolve assets no código-fonte e no executável gerado pelo PyInstaller."""
    if os.path.isabs(caminho_relativo):
        return caminho_relativo

    base_path = getattr(sys, "_MEIPASS", None)
    if base_path is None:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, caminho_relativo)

def save_path(filename):
    if getattr(sys, "frozen", False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(__file__)

    return os.path.join(base, filename)
