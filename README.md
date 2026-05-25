# Sistema de Atención al Cliente Automatizado

Chatbot de atención al cliente para TechStore usando la API de Anthropic (Claude Haiku). Maneja consultas sobre pedidos, productos, devoluciones y soporte técnico desde la terminal, con simulación de consultas a base de datos.

---

## Requisitos previos

- Python 3.9+
- API Key de Anthropic ([console.anthropic.com](https://console.anthropic.com))

---

## Instalación

```bash
git clone https://github.com/awaregomusic/llm.git
cd llm
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```bash
cp .env.example .env
```

Edita `.env` y agrega tu API key:

```
ANTHROPIC_API_KEY=tu_api_key_aqui
```

---

## Uso

```bash
python chatbot.py
```

El agente responde consultas sobre:

| Tema | Palabras clave detectadas |
|---|---|
| Pedidos y envíos | pedido, orden, envío, entrega, rastreo |
| Cuenta del cliente | cuenta, perfil, historial, cliente |
| Productos | producto, precio, stock, disponible |
| Devoluciones | devolución, reembolso, garantía |

Cuando se detecta una de estas categorías, el sistema simula una consulta a la base de datos antes de responder. Escribe `salir` para terminar la sesión.

---

## Estructura

```
llm/
├── chatbot.py       # Lógica del chatbot
├── .env             # API key (no se sube a git)
├── .env.example     # Plantilla de configuración
├── requirements.txt
└── README.md
```
