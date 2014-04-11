python-wordpress-xmlrpc-test
============================

Testing the [python-wordpress-xmlrpc](https://github.com/tothebeat/python-wordpress-xmlrpc) module against [wordpress.hoylabs.com](http://wordpress.hoylabs.com) to see what kind of metadata is returned.

Read more about the original [python-wordpress-xmlrpc](http://python-wordpress-xmlrpc.readthedocs.org/en/latest/index.html) module (the one used in this repository is forked to handle international characters) and the [WordPress XML-RPC API](http://codex.wordpress.org/XML-RPC_WordPress_API) itself.

# Getting Started

Create a virtualenv and install from the requirements file.

```
mkvirtualenv chattanooga
pip install -r requirements.txt
```
(Be sure to `rmvirtualenv` that silly thing when you tire of this)

Copy [config.py.template](config.py.template) to ```config.py``` and
edit the ```WP_USERNAME``` and ```WP_PASSWORD``` variables for the
blog's admin account.

# Run it

Run [sample_post_and_author.py](sample_post_and_author.py).

# Output

       _____                       __        ____             __ 
      / ___/____ _____ ___  ____  / /__     / __ \____  _____/ /_
      \__ \/ __ `/ __ `__ \/ __ \/ / _ \   / /_/ / __ \/ ___/ __/
     ___/ / /_/ / / / / / / /_/ / /  __/  / ____/ /_/ (__  ) /_  
    /____/\__,_/_/ /_/ /_/ .___/_/\___/  /_/    \____/____/\__/  
                        /_/                                      


    {'comment_status': 'open',
     'content': u'B\xe9lgica entr\xf3 en el Top 10 en la <a href="http://wordpress.hoylabs.com/tag/ranking-fifa">clasificaci\xf3n FIFA</a> del mes de marzo, que sigue encabezada por Espa\xf1a, mientras que Panam\xe1 hizo historia al colocarse 29\xba, su mejor posici\xf3n desde que existe esta lista, <a href="http://www.fifa.com/worldranking/rankingtable/index.html">publicada este jueves 13 de marzo en la p\xe1gina web de la FIFA</a>.\n\nTras los partidos amistosos del mes de marzo, Panam\xe1 gana tres posiciones y se mete por primera vez entre los 30 mejores equipos del mundo.\n\nLas cinco primeras posiciones de la lista siguen invariables (Espa\xf1a, Alemania, Argentina, Portugal y Colombia por este orden), mientras que Uruguay supera a Suiza y es sexto y B\xe9lgica se mete en el Top 10 a costa de Holanda.\n\nM\xe9xico asciende un puesto para volver a meterse en el Top 20 de la clasificaci\xf3n, aunque la mejor selecci\xf3n de la Concacaf sigue siendo Estados Unidos, ubicado en el puesto 14.',
     'custom_fields': [],
     'date': datetime.datetime(2014, 3, 14, 1, 12, 58),
     'date_modified': datetime.datetime(2014, 4, 9, 23, 39, 56),
     'excerpt': u'Espa\xf1a se mantiene un mes m\xe1s al frente de la clasificaci\xf3n, B\xe9lgica se mete en el Top 10 y M\xe9xico entre los 20 primeros',
     'guid': 'http://wordpress.hoylabs.com/?p=8393049',
     'id': '8393049',
     'link': 'http://wordpress.hoylabs.com/deportes/8393049/el-top-20-del-ranking-fifa-en-marzo-de-2014',
     'menu_order': 0,
     'mime_type': '',
     'parent_id': '0',
     'password': '',
     'ping_status': 'open',
     'post_format': 'gallery',
     'post_status': 'publish',
     'post_type': 'post',
     'slug': 'el-top-20-del-ranking-fifa-en-marzo-de-2014',
     'sticky': False,
     'terms': [<WordPressTerm: Alemania>,
               <WordPressTerm: clasificación FIFA>,
               <WordPressTerm: Colombia>,
               <WordPressTerm: Deportes>,
               <WordPressTerm: España>,
               <WordPressTerm: FIFA>,
               <WordPressTerm: Fútbol>,
               <WordPressTerm: México>,
               <WordPressTerm: Gallery>,
               <WordPressTerm: ranking FIFA>,
               <WordPressTerm: seleccion colombia>,
               <WordPressTerm: Tri>],
     'thumbnail': {'attachment_id': '8393062',
                   'caption': u'1. Espa\xf1a. Se mantiene igual. 1,510 puntos. GETTY',
                   'date_created_gmt': <DateTime '20140314T00:29:09' at 7fc991a76f80>,
                   'description': 'during the FIFA Confederations Cup Brazil 2013 Final match between Brazil and Spain at Maracana on June 30, 2013 in Rio de Janeiro, Brazil.',
                   'link': '/wp-content/uploads/2014/03/172081466SPAIN.jpg',
                   'metadata': {'file': '2014/03/172081466SPAIN.jpg',
                                'height': '853',
                                'hwstring_small': "height='85' width='128'",
                                'image_meta': {'aperture': '2.8',
                                               'camera': 'Canon EOS-1D X',
                                               'caption': 'during the FIFA Confederations Cup Brazil 2013 Final match between Brazil and Spain at Maracana on June 30, 2013 in Rio de Janeiro, Brazil.',
                                               'copyright': '2013 Getty Images',
                                               'created_timestamp': '1372618688',
                                               'credit': 'Jasper Juinen',
                                               'focal_length': '95',
                                               'iso': '1600',
                                               'shutter_speed': '0.0008',
                                               'title': 'Brazil v Spain: Final - FIFA Confederations Cup Brazil 2013'},
                                'sizes': {'centerpiece-large': {'file': '172081466SPAIN-836x557.jpg',
                                                                'height': '557',
                                                                'width': '836'},
                                          'centerpiece-normal': {'file': '172081466SPAIN-432x288.jpg',
                                                                 'height': '288',
                                                                 'width': '432'},
                                          'gallery-large': {'file': '172081466SPAIN-872x581.jpg',
                                                            'height': '581',
                                                            'width': '872'},
                                          'gallery-river': {'file': '172081466SPAIN-630x420.jpg',
                                                            'height': '420',
                                                            'width': '630'},
                                          'home-featured-large': {'file': '172081466SPAIN-386x257.jpg',
                                                                  'height': '257',
                                                                  'width': '386'},
                                          'home-featured-small': {'file': '172081466SPAIN-240x160.jpg',
                                                                  'height': '160',
                                                                  'width': '240'},
                                          'large': {'file': '172081466SPAIN-1024x682.jpg',
                                                    'height': '682',
                                                    'width': '1024'},
                                          'medium': {'file': '172081466SPAIN-523x348.jpg',
                                                     'height': '348',
                                                     'width': '523'},
                                          'thumbnail': {'file': '172081466SPAIN-150x150.jpg',
                                                        'height': '150',
                                                        'width': '150'}},
                                'width': '1279'},
                   'parent': 8393049,
                   'thumbnail': '/wp-content/uploads/2014/03/172081466SPAIN-150x150.jpg',
                   'title': 'Brazil v Spain: Final - FIFA Confederations Cup Brazil 2013'},
     'title': 'El Top 20 del Ranking FI en marzo de 2014',
     'user': '6'}

        ___         __  __              
       /   | __  __/ /_/ /_  ____  _____
      / /| |/ / / / __/ __ \/ __ \/ ___/
     / ___ / /_/ / /_/ / / / /_/ / /    
    /_/  |_\__,_/\__/_/ /_/\____/_/     


    {'bio': '',
     'display_name': 'Jose Luis Sanchez Pando',
     'email': 'jlsanchez@vivelohoy.com',
     'first_name': 'Jose Luis',
     'id': '6',
     'last_name': 'Sanchez Pando',
     'nicename': 'jose-luis-sanchez-pando',
     'nickname': 'Jose Luis Sanchez Pando',
     'registered': datetime.datetime(2011, 3, 12, 20, 47, 29),
     'roles': {'1': 'editor'},
     'url': '',
     'username': 'Jose Luis Sanchez Pando'}
