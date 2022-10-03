def site():
    import urllib
    import urllib.request

    try:
        site = urllib.request.urlopen('http://www.pudim.com.br')
    except Exception:
        print('O site do Pudim está Inacessível')
    else:
        print('O site do Pudim está Acessível')
        while True:
            op = ' '
            while op not in 'NS':
                op = input('Quer ver o conteúdo do site? ').upper().strip()[0]
            if op in 'N':
                break
            else:
                print(site.read())


site()
