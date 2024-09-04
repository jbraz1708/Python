from prometheus_client import start_http_server, Gauge 
import random
import time
from time import sleep
import requests

# Criar um objeto Gauge para a métrica
data_gauge = Gauge('website_data_metric', 'Descrição da métrica de dados do site')
response_duration_seconds = Gauge('http_response_duration_seconds', 'Duração da resposta HTTP em segundos')


def collect_data():
    # Função para simular a coleta de dados de um site
    return random.random()

def main():
    # Iniciar o servidor HTTP na porta 8000
    start_http_server(8000)
    
    while True:
        # Coletar dados e atualizar a métrica
        data = collect_data()
        data_gauge.set(data)
        response_duration_seconds.set(data)
        sleep(5)  # Atualizar a cada 5 segundos

if __name__ == '__main__':
    main()