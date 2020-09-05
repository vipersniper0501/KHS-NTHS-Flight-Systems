#!/bin/bash

# Bilderverzeichnis
IMGDIR='/home/pi/images'

# Zeitstempel fuer Dateinamen generieren,
# %s: Sekunden seit 1970-01-01 00:00:00 UTC
TIME=$(date +%s)

# Dateinamen erzeugen
FILENAME=$IMGDIR/${TIME}.jpg

# Foto erstellen,  die Parameter -w und -h
# reduzieren die Dateigroesse
raspistill -o $FILENAME -w 1024 -h 768 -n
