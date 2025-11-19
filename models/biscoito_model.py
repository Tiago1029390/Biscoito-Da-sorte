from dados import FRASES
import random


class BiscoitoModel:
    def __init__(self):
        self._frases = FRASES
        self._historico = []
        self._ultima_frase_sorteada = "clique no botao para abri seu biscoito"
        self._frase_anterior = ""
    


    def adicionar_nova_frase(self, nova_frase: str) -> bool:
        """Adiciona uma nova frase à lista de frases, se ela for nova."""
        frase_limpa = nova_frase.strip()
        if frase_limpa and frase_limpa not in self._frases:
            self._frases.append(frase_limpa)
            return True
        return False
    def compartilhar_frase(self,e):
        pass

    def get_frase_aleatoria(self) -> str:
        frase_escolhida = None
        tentativas = 0
        MAX_TENTATIVAS = 3

        while tentativas < MAX_TENTATIVAS:
            frase_candidata = random.choice(self._frases)
            
            if frase_candidata != self._frase_anterior:
                frase_escolhida = frase_candidata
                break

            tentativas += 1

        if frase_escolhida is None: 
            frase_escolhida = random.choice(self._frases) 

        self._frase_anterior = frase_escolhida 
        self._historico.append(frase_escolhida)
        self._ultima_frase_sorteada = frase_escolhida

        return frase_escolhida
 
    # No final do arquivo biscoito_model.py:
    def resetar_historico(self) -> None:
        self._historico = []
        self._frase_anterior = ""
        self._ultima_frase_sorteada = "Clique no botão para abrir seu biscoito!"
        frase = "historico limpo"
        return frase
    def get_total_frases(self) -> int:
        return len(self._historico)
    def get_ultima_frase(self) -> str:
        #Retorna a ultima frase sorteada pelo biscoito.
        return self._ultima_frase_sorteada
    
    
    



