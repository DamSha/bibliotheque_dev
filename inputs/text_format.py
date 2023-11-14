# inputs.text_format.py
# Formate le texte pour la sortie console
# Format léger et custom de 'termcolor'
# import termcolor
from enum import Enum


class COLORS(Enum):
    QUESTION = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    GREYDARK = '\033[90m'
    GREYLIGHT = '\033[89m'
    WHITE = '\033[97m'
    BLACK = '\033[30m'


class FORMATS(Enum):
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class COMMANDS(Enum):
    ENDC = '\033[0m'


class ARC_EN_CIEL_COLORS(Enum):
    FAIL = COLORS.FAIL.value
    QUESTION = COLORS.QUESTION.value
    OKBLUE = COLORS.OKBLUE.value
    OKCYAN = COLORS.OKCYAN.value
    OKGREEN = COLORS.OKGREEN.value
    WARNING = COLORS.WARNING.value

def formatText(texte: str, color: COLORS|ARC_EN_CIEL_COLORS, format: FORMATS = None):
    return (f"{color.value}"
            f"{format.value if format else ''}"
            f"{texte}"
            f"{COMMANDS.ENDC.value}"
            )
