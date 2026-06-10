import os
from ollama import Client
from dotenv import load_dotenv
from pathlib import Path
from src import telemetria, alertas

load_dotenv()
TRILHA = "envirosat"

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + os.environ.get('OLLAMA_API_KEY', '')}
)

def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    messages = []
    if system: messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    try:
        return client.chat(
            model="gpt-oss:120b", messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )['message']['content'].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"

def load_system_prompt():
    path = Path("prompts/system_prompt.md")
    if path.exists(): return path.read_text(encoding="utf-8")
    return "Você é um assistente."

class MissionEngine:
    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self): return True

    def status_snapshot(self):
        dados = telemetria.coletar()
        return (
            f"📡 Status Atual do EnviroSat:\n"
            f"🌡️ Temperatura do Sensor: {dados['temperatura_sensor']}°C\n"
            f"🔋 Nível de Bateria: {dados['nivel_bateria']}%\n"
            f"💾 Buffer de Imagens: {dados['buffer_imagens']} MB\n"
        )

    def analyze(self, pergunta_usuario):
        dados = telemetria.coletar()
        alertas_ativos = alertas.avaliar(dados)
        estado_alertas = "\n".join(alertas_ativos) if alertas_ativos else "Operação nominal. Nenhum alerta crítico."
        
        prompt_completo = (
            f"[DADOS DE TELEMETRIA SIMULADOS]\n"
            f"Dados atuais: {dados}\n"
            f"Alertas disparados: {estado_alertas}\n\n"
            f"[SOLICITAÇÃO DO OPERADOR]\n"
            f"{pergunta_usuario}"
        )
        return llm(prompt_completo, system=self.system_prompt)
