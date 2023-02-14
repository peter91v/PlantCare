.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/plant.care.svg?branch=master
    :target: https://travis-ci.org/collective/plant.care

.. image:: https://coveralls.io/repos/github/collective/plant.care/badge.svg?branch=master
    :target: https://coveralls.io/github/collective/plant.care?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/plant.care.svg
    :target: https://pypi.python.org/pypi/plant.care/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/plant.care.svg
    :target: https://pypi.python.org/pypi/plant.care
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/plant.care.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/plant.care.svg
    :target: https://pypi.python.org/pypi/plant.care/
    :alt: License


==========
plant.care
==========



Installation von PlantCare
---------------------------------------------------------------------------------


1. Raspberry Pi auf setzten.
---------------------------------------------------------------------------------


    -	Raspberry Pi Imager herunterladen: https://www.raspberrypi.com/software/ und installieren.
    -	Betriebssystem auswählen: 
    .. image:: ./docs/pios.jpg
        :target: ./docs/pios.jpg
        :alt: License
    -	SD-Karte auswählen und schreiben drücken.
    -	Nach dem der schreiben beendet ist, SD-Karte in der Raspberry einstecken und der Raspberry OS Installation folgen. (hier wird monitor, Tastatur und eine Maus benötigt)

2.	PlantCare Installieren
---------------------------------------------------------------------------------

    •	Ein Ordner mit der Name Plant_Care in /home/pi erstellen.
    •	In Terminal diese Ordner Öffnen und den Befehl 'git clone https://github.com/peter91v/PlantCareBase.git .' ausführen. (Punkt am Ende ist wichtig!)
    •	Zunächst wird die automatisierte Installation gestartet mit dem './plantinstall.sh' Befehl.
    •	(wenn es nicht starten lässt, zuerst mit dem Befehl 'chmod -x plantinstall.sh' das Privileg ändern und erneut './plantinstall.sh' ausführen.)


3.	Datenbank 
---------------------------------------------------------------------------------
Wird automatisch Installiert und eingestellt nach der anleitung von:
(http://java.xrheingauerx.de/raspberry_mariadb_installieren.html) 
Alle benötigte Tabellen werden bei der Installation erstellt.

4.	Zope/ PlantCare starten
---------------------------------------------------------------------------------

    ■	cd /home/pi/Plant_Care/Zope \n
    ■	bin/zopeinstance fg (für developer) \n
    ■	bin/zopeinstance start (als service starten) \n


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------


Contribute
----------


Support
-------

License
-------

