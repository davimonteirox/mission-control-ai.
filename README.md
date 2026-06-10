# Mission Control AI - EnviroSat

## Integrantes
- Davi Monteiro | RM: 573290

## O que o projeto faz
O sistema simula a telemetria do satélite de monitoramento ambiental EnviroSat, integrando dados simulados a regras de alerta em Python. Utiliza a IA generativa para analisar variações nos parâmetros, traduzindo valores técnicos em diagnósticos em linguagem natural e articulando seu impacto nas operações na Terra.

## Persona atendida
**Operador de centro de controle ambiental (INPE / IBAMA)**. Justificativa: Precisam de uma IA que identifique anomalias orbitais antes que impactem a detecção de focos de incêndio.

## Proposta de valor / Modelo de negócio
1. **Problema resolvido:** A latência na interpretação de falhas nos satélites ambientais pode cegar brigadas de incêndio em momentos críticos.
2. **Quem paga:** Setor público (governo federal/INPE) mediante orçamentos de proteção climática.
3. **Métrica de impacto:** Garantir o monitoramento ininterrupto de 50.000 hectares diários com menos de 2h de latência, reduzindo o alastramento de focos por falhas em 30%.
4. **Modelo de negócio:** *Data-as-a-Service (DaaS)* via concessão pública.

## Tecnologias utilizadas
- Python 3.10+
- Ollama Cloud API (gpt-oss:120b)
- Bibliotecas: ollama, python-dotenv, rich, prompt-toolkit

## Como executar
1. Clone o repositório
2. Crie arquivo `.env` na raiz com: `OLLAMA_API_KEY=sua_chave`
3. Instale dependências: `pip install -r requirements.txt`
4. Execute: `python main.py`

