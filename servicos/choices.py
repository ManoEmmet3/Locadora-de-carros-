from django.db.models import TextChoices

class Choicesaluguel(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar válcula do motor"
    TROCAR_OLEO = "TO", "Troca de óleo"
    BALANCEAMENTO = "B", "Balanceamento"