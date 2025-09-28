import requests

datos_totales = []

for mes in range(1, 13):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2025"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos_mes = response.json()
        for item in datos_mes:
            item['diferencia'] = item['venta'] - item['compra']
        datos_totales.extend(datos_mes)
    except requests.RequestException as e:
        print(f"Error al obtener datos del mes {mes}: {e}")

if datos_totales:
    min_compra = min(datos_totales, key=lambda x: x['compra'])
    max_venta = max(datos_totales, key=lambda x: x['venta'])
    max_diff = max(datos_totales, key=lambda x: x['diferencia'])
    print(f"Compra mínima: {min_compra['fecha']} - {min_compra['compra']}")
    print(f"Venta máxima: {max_venta['fecha']} - {max_venta['venta']}")
    print(f"Diferencia máxima: {max_diff['fecha']} - {max_diff['diferencia']}")
else:
    print("No se obtuvieron datos.")
