from abc import ABC, abstractmethod
import json
from pathlib import Path
import random
from typing import List, Dict, Any

# Classe Pergunta
class Pergunta:
    def __init__(self, pergunta: str, dificuldade: int, alternativas: List[Dict[str, Any]]):
        self.pergunta = pergunta
        self.dificuldade = dificuldade
        self.alternativas = alternativas

    def exibir(self):
        print(f"\n[Dificuldade {self.dificuldade}] {self.pergunta}")
        for i, opcao in enumerate(self.alternativas, 1):
            print(f"{i}. {opcao['alt']}")

    def verificar(self, resposta: int) -> bool:
        if 1 <= resposta <= len(self.alternativas):
            return self.alternativas[resposta - 1]["correct"]
        return False

# 1 - Singleton
class QuizManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QuizManager, cls).__new__(cls)
            cls._instance.load_questions()
        return cls._instance

    def load_questions(self):
        caminho = Path("quiz.json")
        with open(caminho, "r", encoding="utf-8") as file:
            self.quiz_data = json.load(file)["quiz"]["perguntas"]

    def get_questions(self):
        return self.quiz_data


# 2 - Factory
class PerguntaFactory:
    @staticmethod
    def create_question(pergunta: str, dificuldade: int, alternativas: List[Dict[str, Any]]) -> Pergunta: 
        return Pergunta(pergunta, dificuldade, alternativas)


# 3 - Strategy
class QuizStrategy(ABC):
    @abstractmethod
    def executar(self, perguntas):
        pass

class QuizAleatorioStrategy(QuizStrategy):
    def executar(self, perguntas):
        return random.sample(perguntas, len(perguntas))

class QuizOrdenadoStrategy(QuizStrategy):
    def executar(self, perguntas):
        return perguntas


# 4 - Observer
class QuizObserver:
    def update(self, question, correct):
        if correct:
            print("Resposta correta!\n")
        else:
            print("Resposta incorreta.\n")

class Quiz:
    def __init__(self, dificuldade_escolhida, strategy, MAX_PERGUNTAS):
        self.manager = QuizManager()
        self.observer = QuizObserver()
        self.strategy = strategy
        self.pontos = 0

        todas_as_perguntas = self.manager.get_questions()

        perguntas_filtradas = []
        for pergunta_atual in todas_as_perguntas:
            if pergunta_atual['dificuldade'] == int(dificuldade_escolhida):
                perguntas_filtradas.append(pergunta_atual)
        
        self.perguntas = perguntas_filtradas[:MAX_PERGUNTAS]

    def run(self):
        if not self.perguntas:
            print(f"Nenhuma pergunta encontrada para a dificuldade {len(self.perguntas) + 1}.")
            return

        perguntas_para_jogar = self.strategy.executar(self.perguntas)
        
        for dados in perguntas_para_jogar:
            pergunta = PerguntaFactory.create_question(pergunta=dados['pergunta'], dificuldade=dados['dificuldade'], alternativas=dados['alternativas'])
            pergunta.exibir()
            try:
                resposta_usuario = int(input("Sua resposta (digite o número): "))
                resposta = pergunta.verificar(resposta_usuario)
                self.observer.update(pergunta, resposta)
                if resposta:
                    self.pontos += 1
            except (ValueError, IndexError):
                print("Resposta inválida!\n")
        
        print(f"Quiz finalizado! Sua pontuação: {self.pontos} de {len(self.perguntas)}")


if __name__ == "__main__":
    MAX_PERGUNTAS = 2  ##### QUANTIDADE DE PERGUNTAS #####
    dificuldade = input("Escolha a dificuldade (ex: 1, 2, 3): ")
    modo_strategy = input("Modo de quiz (Aleatório - 1, Ordenado - 2): ")
    strategy = QuizAleatorioStrategy() if modo_strategy == "1" else QuizOrdenadoStrategy()
    
    quiz = Quiz(dificuldade, strategy, MAX_PERGUNTAS)
    quiz.run()