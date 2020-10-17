import requests
# Käytetty lähde on osoitteesta https://github.com/HS-Datadesk/koronavirus-avoindata
# koska THL:n rajapinta palauttaa koodin 403 toistaiseksi tuntemattomasta syystä. Datan pitäisi olla käytännössä sama.
url = 'https://w3qa5ydb4l.execute-api.eu-west-1.amazonaws.com/prod/processedThlData'

# tuo data THL:n rajapinnasta JSON-oliona
r = requests.get(url)
print(r.json())
# pura JSON ja erittele haluttu data listan tai olion alkioihin
# tulosta lista visuaalisesti esim matplotlibilla
# valinnaisesti kysy käyttäjältä haluttu shp tai paikkakunta
# tulosta CSV-tiedostoon?