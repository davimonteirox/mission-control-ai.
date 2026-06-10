def avaliar(dados):
    alertas = []
    if dados.get("temperatura_sensor", 0) > 45.0:
        alertas.append("CRÍTICO: Risco de degradação térmica do sensor óptico e térmico.")
    if dados.get("nivel_bateria", 100) < 20.0:
        alertas.append("CRÍTICO: Energia insuficiente para manobras evasivas ou downlink.")
    if dados.get("buffer_imagens", 0) > 900.0:
        alertas.append("AVISO: Buffer de imagens operando no limite. Risco de perda de dados.")
    return alertas
