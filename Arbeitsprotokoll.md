# 11 / 12 KW

Rastervision Installieren auf Ubuntu

1a) Conda installieren (z.B. miniconda)
1b) GDAL über Conda installieren, VERSION 3.5.2!!!
2) mit sudo apt-get install libgdal-dev installieren (evtl. muss vorher noch sudo apt-get update gemacht werden)
3) pip3 install triangle (optional, da wahrscheinlich über Rastervision mitgezogen)
4) pip3 install rastervision und rastervision.gdal_vsi
5) apt install libgl1-mesa-glx 


Persönlich getetest auf:

Ubuntu 22.04 LTS und mit Python 3.10.4

Mac-User (m1)
nicht lauffähig, da triangle nicht auf m1 installiert werden kann (getestet in MacOS und ParallelsDesktop - Ubuntu22.04 (arm version))



Rastervision Predict mit Model-Bundle Potsdam (segmentation) und sample.tif -> gutes ergebnis

Für den Export von weiteren Tif wurde QGis verwendet. QGis kann tif dateien öffnen.
Bing Luftbilder (Karte) ist vorhanden, Bildqualität schlecht. -> Tif-Export und Prediction unter Potsdam Model-Bundle -> ergbnis kommt nur garbage raus

alternative Bildquellen - Sentinel, Copernicus? -> offen

QGis gutes Programm für Geodaten/bilder, aber keine Automatisierung

QGis plugins: Semi-Automatic classification Plugin, sentinel hub

