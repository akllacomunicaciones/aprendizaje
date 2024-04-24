def hola():
    print("Hola mundo!")
    #funcion que imprime hola mundo
hola()


import webbrowser

def buscar_en_web(busqueda):
    url = "https://www.google.com.tr/search?q={}".format(busqueda)
    webbrowser.open_new_tab(url)