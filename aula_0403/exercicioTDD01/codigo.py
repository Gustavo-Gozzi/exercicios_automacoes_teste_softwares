def obter_categoria(idade):
    if 5 <= idade <= 7: return 'Infantil A'
    elif 8 <= idade <= 10: return 'Infantil B'
    elif 11 <= idade <= 13: return 'Juvenil A'
    elif 14 <= idade <= 17: return 'Juvenil B'
    elif idade >= 18: return 'Sênior'
    elif idade < 0: return 'Erro Idade Negativa'
    else: return False

