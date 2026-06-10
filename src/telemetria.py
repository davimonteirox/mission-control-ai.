import random

def coletar():
    """Gera dados simulados do satélite EnviroSat."""
    return {
        "temperatura_sensor": round(random.uniform(15.0, 50.0), 1),
        "nivel_bateria": round(random.uniform(10.0, 100.0), 1),
        "buffer_imagens": round(random.uniform(100.0, 950.0), 1)
    }
