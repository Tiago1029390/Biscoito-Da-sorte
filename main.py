#Meu primeiro Projeto com VS Code e Git
"""
PROJETO BISCOITO DA SORTE
"""

import flet as ft
import random
from dados import FRASES
from models.biscoito_model import BiscoitoModel
meu_biscoito = BiscoitoModel()



# ============================================================================
# Dados da Aplicação
# ============================================================================

'''
FRASES = [
    "A vida trará coisas boas se tiveres paciência.",
    "Demonstre amor e alegria em todas as oportunidades e verás que a paz nasce dentro de você.",
    "Não compense na ira o que lhe falta na razão.",
    "Defeitos e virtudes são apenas dois lados da mesma moeda.",
    "A maior de todas as torres começa no solo.",
    "Não há que ser forte, mas sim flexível.",
    "Gente todo dia arruma os cabelos, por que não o coração?",
    "Há três coisas que jamais voltam: a flecha lançada, a palavra dita e a oportunidade perdida.",
    "A juventude não é uma época da vida, é um estado de espírito.",
    "Vencer a si próprio é a maior das vitórias.",
    "Deixe de lado as preocupações e seja feliz.",
    "Realize o óbvio, pense no improvável e conquiste o impossível.",
    "Acredite em milagres, mas não dependa deles.",
    "A sorte favorece a mente bem preparada.",
    "Seu esforço será recompensado.",
]
'''


# ============================================================================
# Função Principal da Aplicação
# ============================================================================
def main(page: ft.Page):
    # Configurações da janela
    page.title = "Biscoito da Sorte"
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # ========================================================================
    # Componentes da Interface
    # ========================================================================
    
    # Título
    titulo = ft.Text(
        "🥠 Biscoito da Sorte",
        size=32,
        weight=ft.FontWeight.BOLD,
        color="blue800",
        text_align=ft.TextAlign.CENTER,
    )
    
    # Container para exibir a frase
    frase_texto = ft.Container(
        content=ft.Text(
            "Clique no botão para abrir seu biscoito!",
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="grey700",
        ),
        margin=ft.margin.symmetric(vertical=30),
        padding=20,
        bgcolor="blue50",
        border_radius=10,
        border=ft.border.all(2, "blue200"),
        alignment=ft.alignment.center,
    )
    
    # Contador de cliques
    contador_texto = ft.Text(
        f"Biscoitos abertos:{meu_biscoito.get_total_frases()}",
        size=14,
        color="grey600",
        text_align=ft.TextAlign.CENTER,
    )
    
    # ========================================================================
    # Função de Evento (Callback)
    # ========================================================================
    def abrir_biscoito(e):
        """
        Função chamada quando o botão é clicado.
        """
    
        # Atualiza o texto da frase na tela
        frase_texto.content = ft.Text(
            meu_biscoito.get_frase_aleatoria(),
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="pink600",
            weight=ft.FontWeight.W_500,
        )
        
        # Atualiza o contador na tela
        contador_texto.value = f"Biscoitos abertos: {meu_biscoito.get_total_frases()}"
        
        # Atualiza a página
        page.update()
    
    
    def resetar_historico(e):
        meu_biscoito.resetar_historico()
        """
        Função chamada quando o botão é clicado.
        """
        
        # Atualiza o texto da frase na tela
        frase_texto.content = ft.Text(
            meu_biscoito.resetar_historico(),
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="pink600",
            weight=ft.FontWeight.W_500,
        )
    def adicionar_nova_frase(e):

        """
        Função chamada quando o botão é clicado.
        """
        
        # Atualiza o texto da frase na tela
        frase_texto.content = ft.Text(
            meu_biscoito.adicionar_nova_frase('nova_frase'),
            size=18,
            text_align=ft.TextAlign.CENTER,
            color="pink600",
            weight=ft.FontWeight.W_500,
        )
        
        # Atualiza o contador na tela
        #contador_texto.value = f"Biscoitos abertos: {meu_biscoito.get_total_frases()}"
        
        # Atualiza a página
        page.update()
    
    # ========================================================================
    # Botão de Ação
    # ========================================================================
    botao = ft.ElevatedButton(
        text="Abrir Biscoito 🥠",
        # icon="cake",
        on_click=abrir_biscoito,
        style=ft.ButtonStyle(
            color="green",
            bgcolor="700",
            padding=20,
        ),
        width=200,
        height=50,
    )
    # ... Na seção "Botão de Ação" ...
    
    # Novo botão de Compartilhamento
    botao_compartilhar = ft.IconButton(
        
        icon=ft.Icons.ATTACH_EMAIL,
        icon_color= ft.Colors.BLUE_500,
        on_click=meu_biscoito.compartilhar_frase,  # Esta função será criada no Passo 2
        style=ft.ButtonStyle(
            color=ft.Colors.RED_700,
            padding=20,
        ),
        height= 100,
        width= 100,
        icon_size= 25
    )

    # ... (os outros botões e containers seguem) ...
    
    botao_resetar_historico = ft.ElevatedButton(
        text="Resetar Histórico",
        # icon="cake",
        on_click= resetar_historico,
        style=ft.ButtonStyle(
            color="red",
            bgcolor="red700",
            padding=20,
        ),
        width=200,
        height=50,
    )
    container_reset_alinhamento = ft.Container(
        content=botao_resetar_historico,
        alignment=ft.alignment.center_right, # Alinha o conteúdo à direita
        width=400, # Largura para garantir que o alinhamento funcione
        margin=ft.margin.only(top=20),
    )
    botao_adicionar_frase = ft.ElevatedButton(
        text="Adicione uma nova Frase",
        # icon="cake",
        on_click= adicionar_nova_frase,
        style=ft.ButtonStyle(
            color="red",
            bgcolor="red700",
            padding=20,
        ),
        width=200,
        height=50,
    )
    container_reset_alinhamento = ft.Container(
        content=botao_adicionar_frase,
        alignment=ft.alignment.center_right, # Alinha o conteúdo à direita
        width=400, # Largura para garantir que o alinhamento funcione
        margin=ft.margin.only(top=20),
    )
    
    # ========================================================================
    # Layout da Página
    # ========================================================================
    page.add(
        ft.Column(
            [
                titulo,
                frase_texto,
                ft.Container(
                    content=botao,
                    alignment=ft.alignment.center,
                ),
                ft.Container(height=10),
                ft.Container(
                    content=botao_compartilhar,
                    alignment=ft.alignment.center,

                ),

                ft.Container(height=20),  # Espaçamento
                contador_texto,
                
                
                ft.Container(expand=True),
                #ft.Row(
                    #[botao_]
                #)
                container_reset_alinhamento,
                
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )
    
# ============================================================================
# Execução
# ============================================================================
if __name__ == "__main__":
    ft.app(target=main)