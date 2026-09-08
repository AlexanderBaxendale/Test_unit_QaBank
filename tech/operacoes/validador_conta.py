def validar_abertura_conta(idade, score_credito):
    if idade < 18:
        raise ValueError("Menor de idade não permitido")

    if score_credito <= 500:
        return "Recusado"
    
    return "Aprovado"