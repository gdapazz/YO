from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
import random
from noticias import noticias_lista 

class NoticiaSeguraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        self.titulo = Label(
            text="Notícia Segura",
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=700
        )
        
        self.texto_intro = """Vivemos em um mundo onde as notícias chegam cada vez mais rápido, 
mas nem sempre são verdadeiras. Pensando nisso, criamos o Notícia Segura, um aplicativo feito 
especialmente para ajudar você a identificar informações confiáveis e evitar fake news.

A informação correta é um direito de todos."""

        self.texto_label = Label(
            text=self.texto_intro,
            font_size=23,
            halign="center",
            valign="bottom",
            size_hint_y=None
        )
        self.texto_label.bind(size=lambda instance, value: setattr(instance, 'text_size', (value[0], None)))

        self.botao_iniciar = Button(text="Iniciar", size_hint=(None, None), size=(200, 50))
        self.botao_sair = Button(text="Sair", size_hint=(None, None), size=(200, 50))
        self.botao_sair.bind(on_press=self.fechar_app)
        self.botao_iniciar.bind(on_press=self.mostrar_nome_idade)

        self.layout.add_widget(self.titulo)
        self.layout.add_widget(self.texto_label)
        self.layout.add_widget(self.botao_iniciar)
        self.layout.add_widget(self.botao_sair)

        self.noticias_exibidas = []  

        return self.layout

    def fechar_app(self, instance):
        App.get_running_app().stop()

    def mostrar_nome_idade(self, instance):
        self.layout.clear_widgets()
        
        self.titulo.text = "Por favor, informe seus dados"
        nome_label = Label(text="Qual seu nome?", font_size=23)
        self.nome_input = TextInput(font_size=18, size_hint_y=None, height=40)
        
        idade_label = Label(text="Qual sua idade?", font_size=23)
        self.idade_input = TextInput(font_size=18, size_hint_y=None, height=40)

        botao_salvar = Button(text="Salvar", size_hint=(None, None), size=(200, 50))
        botao_salvar.bind(on_press=self.salvar_dados)

        self.layout.add_widget(nome_label)
        self.layout.add_widget(self.nome_input)
        self.layout.add_widget(idade_label)
        self.layout.add_widget(self.idade_input)
        self.layout.add_widget(botao_salvar)

    def salvar_dados(self, instance):
        nome = self.nome_input.text
        idade = self.idade_input.text
        print(f"Nome: {nome}, Idade: {idade}")

        self.layout.clear_widgets()
        confirmacao_label = Label(text=f"Bem-vindo, {nome}! Estamos prontos para começar.", font_size=18)
        
        botao_seguir = Button(text="Seguir", size_hint=(None, None), size=(200, 50))
        botao_seguir.bind(on_press=self.mostrar_dicas)

        self.layout.add_widget(confirmacao_label)
        self.layout.add_widget(botao_seguir)

    def mostrar_dicas(self, instance):
        self.layout.clear_widgets()

        texto_dicas = """Veja abaixo como identificar fake news:

Chamativas ou bombásticas
Em muitos casos, o título não se relaciona ao restante do texto. Nunca leia só o título e confira se o fato já foi publicado em outros veículos. 

Erros ortográficos ou gramaticais
Textos jornalísticos são revisados antes de serem publicados. Se o texto contém erros, desconfie. Cheque a informação em outros veículos mais reconhecidos.

Textos opinativos como se fossem notícia
Todo artigo opinativo deve vir assinado pelo seu autor. Mesmo em entrevistas, a opinião dos entrevistados é apresentada de forma imparcial pelo veículo. Se a suposta notícia traz opinião disfarçada no meio do texto, não é isenta.

Canais desconhecidos
Convém checar se outros veículos também publicaram a notícia. Isso ajuda a garantir a credibilidade da informação.

Notícia verdadeira mas antiga
Nem sempre as notícias são falsas, mas podem ser antigas e estar descontextualizadas visando gerar desinformação. Por essa razão é importante verificar a data da publicação e buscar a fonte para saber da veracidade do fato e em que data ocorreu."""

        texto_label = Label(
            text=texto_dicas,
            font_size=30,
            size_hint_y=None,
            height=1000,
            halign="center",
            valign="middle",
            text_size=(self.layout.width - 40, None)
        )

        scroll = ScrollView(size_hint=(1, None), size=(self.layout.width, 500))
        scroll.add_widget(texto_label)
        self.layout.add_widget(scroll)

        botao_seguir = Button(text="Seguir", size_hint=(None, None), size=(200, 50))
        botao_seguir.bind(on_press=self.mostrar_proxima_pagina)

        self.layout.add_widget(botao_seguir)

    def mostrar_proxima_pagina(self, instance):
        self.layout.clear_widgets()
        
        texto_conhecimento = """Agora, vamos testar seu conhecimento na prática!
Você deve ler a notícia e identificar o motivo pelo qual ela é falsa.
Os motivos podem ser: Chamativas ou bombásticas, Erros ortográficos ou gramaticais, Textos opinativos, Canais desconhecidos, ou Verdadeiras mas antigas.

Você está pronto?"""

        texto_label = Label(
            text=texto_conhecimento,
            font_size=34,
            size_hint_y=None,
            height=1000,
            halign="center",
            valign="top",
            text_size=(self.layout.width - 40, None)
        )

        botao_estou = Button(text="Estou", size_hint=(None, None), size=(200, 50))
        botao_estou.bind(on_press=self.iniciar_testes)

        self.layout.add_widget(texto_label)
        self.layout.add_widget(botao_estou)

    def iniciar_testes(self, instance):
        self.acertos = 0
        self.rodadas = 0
        self.mostrar_noticia()

    def mostrar_noticia(self):
        if self.rodadas < 5:
            
            if len(self.noticias_exibidas) < len(noticias_lista):
                noticia = random.choice([n for n in noticias_lista if n not in self.noticias_exibidas])  
                self.noticias_exibidas.append(noticia)  
            else:
                noticia = random.choice(noticias_lista)  

            noticia_titulo = noticia["titulo"]
            noticia_texto = noticia["texto"]
            self.motivo_correto = noticia["motivo"]
            self.imagem = noticia["imagem"]

            self.layout.clear_widgets()

            titulo_label = Label(text=noticia_titulo, font_size=22, bold=True)
            imagem_label = Image(source=self.imagem)
            noticia_label = Label(text=noticia_texto, font_size=18)
            motivo_input = TextInput(hint_text="Chamativas ou bombásticas, Erros ortográficos ou gramaticais, Textos opinativos, Canais desconhecidos, Verdadeiras mas antigas.", font_size=16, size_hint_y=None, height=40)
            botao_resposta = Button(text="Responder", size_hint=(None, None), size=(200, 50))
            botao_resposta.bind(on_press=lambda instance: self.verificar_resposta(motivo_input.text))

            self.layout.add_widget(titulo_label)
            self.layout.add_widget(imagem_label)
            self.layout.add_widget(noticia_label)
            self.layout.add_widget(motivo_input)
            self.layout.add_widget(botao_resposta)
        else:
            self.layout.clear_widgets()
            resultado_label = Label(text=f"Você acertou {self.acertos} de 5 notícias.", font_size=22)
            self.layout.add_widget(resultado_label)

    def verificar_resposta(self, resposta):
        if resposta.lower() == self.motivo_correto.lower():
            self.acertos += 1
        self.rodadas += 1
        self.mostrar_noticia()

if __name__ == "__main__":
    NoticiaSeguraApp().run()
