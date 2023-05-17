# QGIS installieren und verwenden

## Installieren

https://www.qgis.org/de/site/forusers/download.html

## Einbinden der Satelittenquellen in QGIS:

Links im Fenster können verschiedene Quellen eingebunden werden:

ArcGIS REST Server: https://tiledbasemaps.arcgis.com/arcgis/rest/services/World_Imagery/MapServer

Xyz Tiles:
	Bing Luftbilder: http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1
	Google Satellite: http://www.google.cn/maps/vt?lyrs=s@189&gl=cn&x={x}&y={y}&z={z}

WMS/WMTS:
	Brandenburg_IR_WMTS:
		https://isk.geobasis-bb.de/mapproxy/dop20cir_wmts/service?request=GetCapabilities&service=WMTS
	Brandenburg_RGB_WMTS:
		https://isk.geobasis-bb.de/mapproxy/dop20c_wmts/service?request=GetCapabilities&service=WMTS

## Für den Export der Bilder aus QGIS:
	1.Im Reiter Projekt „Import/Export“
	2.Karte als Bild speichern
	
Exportiert den dargestellten Bereich als (geo)Tif
