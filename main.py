import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.list import TwoLineIconListItem
from kivy.uix.screenmanager import Screen
import os
from github import Github

# from admob import Admob
imagens_url_ref = "example"
imagens_ref = "example"
Window.size = (350, 580)


class BookList(Screen):
    def savebook(self):
        global imagens_ref
        global imagens_url_ref
        global livro
        g = Github("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")
        image_url = "https://raw.githubusercontent.com/freelivros/book_images/main/example"
        repo = g.get_repo("freelivros/book_images")

        contents = repo.get_contents("")
        self.ids.lista_livros.clear_widgets()
        for imagens in contents:
            # image load script
            image_str = str(imagens)
            imagens_cut = image_str[18::1]
            imagens_ref = imagens_cut.replace('")', '')
            image_url_pref = imagens_ref.replace(' ', '%20')
            imagens_url_ref = image_url.replace('example', image_url_pref)
            #

            # Add widget script
            livro = ImageLeftWidget(source="{}".format(imagens_url_ref))
            item = TwoLineIconListItem(text="{}".format(imagens_ref.replace('.png', '')), on_release=lambda x: self.baixar(),
                                       secondary_text="Baixar")
            item.add_widget(livro)
            self.ids.lista_livros.add_widget(item)
            #limpa widgets: self.ids.lista_livros.clear_widgets()

    def baixar(self):

        pdf_url = "https://raw.githubusercontent.com/freelivros/books/main/example"

        pdf_url_ref = pdf_url.replace('example', imagens_ref.replace('.png', '.pdf'))

        pdf_url_ref1 = pdf_url_ref.replace(' ', '%20')

        response = requests.get(pdf_url_ref1)

        saida_dir = "/"

        pdf_path = os.path.join(os.path.basename(pdf_url_ref1.replace('%20', ' ')))

        print(pdf_url_ref1)

        with open(pdf_path, 'wb') as f:
            f.write(response.content)
            f.close()

    def search(self):
        pass


class app(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('hud.kv')

    def pedirlivro(self):
        print("desativado temporariamente")

if __name__ == '__main__':
    app().run()