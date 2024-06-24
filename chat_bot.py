# sh pip install python-Levenshtein
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
  perguntas_respostas = carregar_perguntas("perguntas.txt")
  # limiar_distancia = int(input("Digite o limiar de distância para considerar uma pergunta semelhante:"))
  # while True:
  #   pergunta = input("Faça uma pergunta:").lower()
  #   if pergunta == "sair":
  #     break
  #   resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  #   print("Resposta:", resposta)

  limiar_distancia = 20
  pergunta = "quem é você?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")

  pergunta = "qual a sua função?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")

  pergunta = "como você funciona?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")

  pergunta = "quem te criou?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")

  pergunta = "qual o sentido da vida?"
  resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
  print(f"{pergunta}: {resposta}")
