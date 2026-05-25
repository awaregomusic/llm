import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """Eres un agente de atención al cliente de TechStore, una tienda de tecnología.
Puedes ayudar con:
- Consultas sobre productos (laptops, celulares, accesorios)
- Estado de pedidos y envíos
- Devoluciones y garantías
- Soporte técnico básico

Sé amable, conciso y resolutivo. Responde siempre en español."""


def consultar_bd(tipo, referencia=None):
    print(f"  [sistema: consultando base de datos de {tipo}...]")
    if tipo == "pedido":
        return {"id": referencia or "ORD-8821", "estado": "En camino", "entrega_estimada": "2026-05-27"}
    if tipo == "cliente":
        return {"nombre": "Cliente registrado", "pedidos_totales": 3, "nivel": "Gold"}
    if tipo == "producto":
        return {"disponible": True, "precio": "$999 USD", "stock": 5}
    if tipo == "devolucion":
        return {"politica": "30 días", "estado": "Aprobada", "reembolso": "3-5 días hábiles"}
    return {}


def obtener_contexto(mensaje):
    msg = mensaje.lower()
    if any(w in msg for w in ["pedido", "orden", "envío", "entrega", "rastreo"]):
        return consultar_bd("pedido")
    if any(w in msg for w in ["cuenta", "perfil", "historial", "cliente"]):
        return consultar_bd("cliente")
    if any(w in msg for w in ["producto", "precio", "stock", "disponible", "costo"]):
        return consultar_bd("producto")
    if any(w in msg for w in ["devolucion", "devolución", "reembolso", "garantía", "garantia"]):
        return consultar_bd("devolucion")
    return None


def chat():
    historial = []
    print("\n" + "=" * 52)
    print("   TechStore — Agente de Atención al Cliente")
    print("   Escribe 'salir' para terminar la sesión")
    print("=" * 52)

    while True:
        try:
            user_input = input("\nTú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAgente: ¡Hasta luego!")
            break

        if not user_input:
            continue
        if user_input.lower() in ("salir", "exit", "quit", "q"):
            print("\nAgente: ¡Hasta luego! Fue un placer ayudarte.")
            break

        contexto = obtener_contexto(user_input)
        contenido = user_input
        if contexto:
            contenido += f"\n[Datos del sistema: {contexto}]"

        historial.append({"role": "user", "content": contenido})

        respuesta = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=historial,
        )

        mensaje = respuesta.content[0].text
        historial.append({"role": "assistant", "content": mensaje})
        print(f"\nAgente: {mensaje}")


if __name__ == "__main__":
    chat()
