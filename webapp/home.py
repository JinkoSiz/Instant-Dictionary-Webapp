import justpy as jp
from webapp import layout
from webapp import page


class Home(page.Page):
    path = '/'

    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen p-2')
        jp.Div(a=div, text='This is the Home page', classes='text-4xl m-2')
        jp.Div(a=div, text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. Velit aliquet sagittis id consectetur purus ut faucibus pulvinar 
                elementum. Praesent elementum facilisis leo vel fringilla est. Congue quisque egestas diam in arcu cursus. 
                Tincidunt eget nullam non nisi. Ac feugiat sed lectus vestibulum mattis. Quisque egestas diam in arcu cursus. 
                Et tortor consequat id porta nibh venenatis. Fermentum odio eu feugiat pretium nibh ipsum consequat. Dui 
                accumsan sit amet nulla. Fermentum odio eu feugiat pretium nibh ipsum consequat. Commodo sed egestas egestas 
                fringilla phasellus faucibus scelerisque eleifend donec.''', classes='text-lg')

        return wp

