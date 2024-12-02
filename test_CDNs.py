''' test_CDNs.py
Archivo de Python para probar el funcionamiento de CDNs por medio de hacer varios requerimientos, registrando los tiempos que toma en 
recibir respuesta y estimando el ancho de banda con el que recibe la respuesta
Bastián Rivas, IPD438
'''
import time
import requests
import logging

def measure_response_time(url, name):
    start_time = time.time()
    print(f"Haciendo requerimietos a {url}")  # 
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        end_time = time.time()
        
        # Medir el ancho de banda
        content_length = len(response.content)
        bandwidth = content_length / (end_time - start_time)  # bytes/segundo
        
        print(f"{name}: Tiempo - {end_time - start_time:.4f} segundos")  # Imprimir por consola
        return end_time - start_time, bandwidth, 0  # 0 indica que no hubo error
    except requests.RequestException as e:
        end_time = time.time()
        print(f"{name}: Error al realizar la solicitud")  # Imprimir por consola en caso de error
        logging.error(f"Error al acceder {url}: {e}")
        return end_time - start_time, 0, 1  # 1 indica que hubo error

# Configurar logging
logging.basicConfig(filename='cdn_performance.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

N = 200 # Número de requests que se enviarán

cdn_services = {
    "AWS (DNS)": "https://aws.amazon.com/es/route53/",
    "Cloudflare (Anycast)": "https://www.cloudflare.com",
    "Bing (FastRoute)": "https://www.bing.com"
}

for name, url in cdn_services.items():
    times = []
    bandwidths = []
    errors = 0
    for _ in range(N):  # Hacer N solicitudes para obtener un promedio
        
        response_time, bandwidth, error = measure_response_time(url, name)
        times.append(response_time)
        bandwidths.append(bandwidth)
        errors += error
        logging.info(f"{name}: Tiempo - {response_time:.4f} segundos, Ancho de banda - {bandwidth:.2f} bytes/segundo, Error - {error}")
    avg_time = sum(times) / len(times)
    avg_bandwidth = sum(bandwidths) / len(bandwidths)
    error_rate = errors / N
    logging.info(f"Resultados para {name}:\n - Tiempo promedio: {avg_time:.4f} segundos\n - Ancho de banda promedio: {avg_bandwidth:.2f} bytes/segundo\n - Tasa de error: {error_rate:.2%}\n")

print("Resultados guardados en 'cdn_performance.log'")