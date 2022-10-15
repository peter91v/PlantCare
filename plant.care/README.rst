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

    ■ Raspberry Pi Imager herunterladen: https://www.raspberrypi.com/software/ und installieren.
    ■ Betriebssystem auswählen: 
    .. image:: ./docs/pios.jpg
        :target: ./docs/pios.jpg
        :alt: License

    ■ SD-Karte auswählen und schreiben drücken.
    ■ Nach dem der schreiben beendet ist, SD-Karte in der Raspberry einstecken und der Raspberry OS Installation folgen. (hier wird monitor, Tastatur und eine Maus benötigt)


2.	PlantCare Installieren
---------------------------------------------------------------------------------

    ■ Ein Ordner mit der Name Plant_Care in /home/pi erstellen.
    ■ In Terminal diese Ordner Öffnen und den Befehl 'git clone https://github.com/peter91v/PlantCareBase.git .' ausführen. (Punkt am Ende ist wichtig!)
    ■ Zunächst wird die automatisierte Installation gestartet mit dem './plantinstall.sh' Befehl.
    (wenn es nicht starten lässt, zuerst mit dem Befehl 'chmod -x plantinstall.sh' das Privileg ändern und erneut './plantinstall.sh' ausführen.)


3.	Datenbank (http://java.xrheingauerx.de/raspberry_mariadb_installieren.html)
---------------------------------------------------------------------------------

Datenbank Einstellung bei Instalation:
    1: "Enter current password for root"	        Quitieren mit Enter (wir geben nichts ein)
    2: "Set root password"	                    Y  (und dann ein Passwort für den Benutzer root vergeben)
    3: "Remove anonymous users"	                Y  (solche Benutzer wollen wir nicht)
    4: "Disallow root login remotly"	        Y  (wir wollen, dass sich der Benutzer root nur lokal anmelden kann)
    5: "Remove test database and access to it"	Y  (wir brauchen keine Test-Datenbank)
    6: "Reload privilege tables now"	        Y  (diese müssen neu geladen)

SQL befehle zum einrichten Datenbank:
---------------------------------------------------------------------------------

    ■	sudo mysql
        -	create database plantcare;
        -	create user 'plantcare'@'%' identified by 'plantcare';
        -	grant all privileges on plantcare.* to 'plantcare'@'%' identified by 'plantcare';
        -	flush privileges;
        -	\q

    ■	sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
        -	‘#’ Zeichen bei port entfernen
        -	Bind-address = 0.0.0.0
        -	Strg + O (zum speichern)
        -	Strg + x (nano beenden)

    ■   sudo service mysql restart

    ■   Datenbank Tabellen erstellen:

        CREATE TABLE `Sensors` (
        `ID` int(11)  NOT NULL AUTO_INCREMENT,
        `SensorName` varchar(255) NOT NULL,
        `Humidity` int(11) DEFAULT NULL,
        `SensorDry` int(11) DEFAULT NULL,
        `SensorWet` int(11) DEFAULT NULL,
        PRIMARY KEY (`SensorName`)
        )

        CREATE TABLE `Data` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `humidity` float DEFAULT NULL,
        `date` date DEFAULT NULL,
        `time` datetime DEFAULT NULL,
        `Sensor` varchar(255) NOT NULL,
        PRIMARY KEY (`id`),
        KEY `SensorName` (`Sensor`),
        CONSTRAINT `SensorName` FOREIGN KEY (`Sensor`) REFERENCES `Sensors` (`SensorName`) ON DELETE NO ACTION ON UPDATE NO ACTION
        )

4.	Zope/ PlantCare starten
---------------------------------------------------------------------------------

    ■	cd /home/pi/Plant_Care/Zope
    ■	bin/zopeinstance fg (für developer)
    ■	bin/zopeinstance start (als service starten)


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------


Contribute
----------

- Issue Tracker: https://github.com/collective/plant.care/issues
- Source Code: https://github.com/collective/plant.care
- Documentation: https://docs.plone.org/foo/bar


Support
-------

License
-------

