import sys
import Levenshtein

def carregar_perguntas(arquivo):
  perguntas_respostas = {}
  with open(arquivo, "r") as f:
    for linha in f:
      pergunta, resposta = linha.strip().split("|")
      perguntas_respostas[pergunta.lower()] = resposta
  return perguntas_respostas

def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
  menor_distancia = float("inf")
  melhor_resposta = ""
  for p, r in perguntas_respostas.items():
    distancia = Levenshtein.distance(pergunta, p)
    if distancia < menor_distancia:
      menor_distancia = distancia
      melhor_resposta = r
  if menor_distancia <= limiar_distancia:
      return melhor_resposta
  else:
      return "Pergunta não encontrada."

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Uso: python3 chat_bot.py <pergunta>")
    sys.exit(1)

  pergunta = sys.argv[1].lower()
  perguntas_respostas = carregar_perguntas("perguntas.txt")
  limiar_distancia = 5
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")
