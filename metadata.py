#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PROJECTS = [
    # First one is intentionally left blank as template
    {
        'name': '',
        'href': '',
        'imagetitle': '',
        'tags': [],
        'description': """
        """,
        'starred': False,
    },
    {
        'name': 'createPokémon.team',
        'href': 'https://createpokemon.team/',
        'imagetitle': 'createpokemonteam',
        'tags': ['Python 3', 'Angular', 'TypeScript', 'SCSS'],
        'description': """
            Web application that helps you build your own Pokémon team in any core series game.
            <a href="https://github.com/mirzal/create-pokemon-team">Github</a>.
        """,
        'starred': True,
    },
    {
        'name': 'Pelican Metadata Generator',
        'href': 'https://github.com/mirzal/pelican-metadata-generator',
        'imagetitle': 'pelican',
        'tags': ['Python 3', 'PyQt 5', 'unittest', 'Markdown'],
        'description': """
            Graphical application to create <a href="https://blog.getpelican.com/">Pelican</a> post metadata.
        """,
        'starred': True,
    },
    {
        'name': 'Civic engagement in Europe',
        'href': 'https://mzalewski.shinyapps.io/ESS-civic-engagement',
        'imagetitle': 'ess',
        'tags': ['R', 'ggplot2', 'Shiny (HTML, CSS)', 'data wrangling', 'visualisation'],
        'description': """
            R Shiny application to explore changes in civic engagement index in various European countries over time.
        """,
        'starred': False,
    },
    {
        'name': 'Przepis na LibreOffice',
        'href': 'http://przepis-na-lo.pl/',
        'imagetitle': 'przepis-na-lo',
        'tags': ['Wordpress', 'PHP', 'HTML', 'CSS', 'writing'],
        'description': """
            My discontinued blog focused on <a href="https://libreoffice.org/">LibreOffice</a> tips and tricks. It was relatively popular in Polish open source and academic communities, attracting about 20 000 unique visitors in peak months.
        """,
        'starred': False,
    },
    {
        'name': 'My blog',
        'href': '/blog/',
        'imagetitle': 'blog',
        'tags': ['Pelican', 'Jinja2 (HTML, SCSS)', 'writing'],
        'description': """
            My current blog, focused mainly on tech and testing.
        """,
        'starred': False,
    },
]
