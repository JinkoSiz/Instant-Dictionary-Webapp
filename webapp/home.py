import justpy as jp


class Home:
    path = '/home'

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page', classes='text-4xl m-2')
        jp.Div(a=div, text='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. Velit aliquet sagittis id consectetur purus ut faucibus pulvinar 
                elementum. Praesent elementum facilisis leo vel fringilla est. Congue quisque egestas diam in arcu cursus. 
                Tincidunt eget nullam non nisi. Ac feugiat sed lectus vestibulum mattis. Quisque egestas diam in arcu cursus. 
                Et tortor consequat id porta nibh venenatis. Fermentum odio eu feugiat pretium nibh ipsum consequat. Dui 
                accumsan sit amet nulla. Fermentum odio eu feugiat pretium nibh ipsum consequat. Commodo sed egestas egestas 
                fringilla phasellus faucibus scelerisque eleifend donec.''', classes='text-lg')

        return wp

