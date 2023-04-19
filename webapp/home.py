import justpy as jp


class Home:
    path = '/'

    @classmethod
    def serve(cls):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode='leftDrawerOpen', side="left", bordered=True)

        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dens=True, flat=True, round=True, icon='menu', click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

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

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
