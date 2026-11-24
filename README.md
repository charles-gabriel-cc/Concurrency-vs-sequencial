<p align="center">
  <img src=".github/banner.svg" alt="Concurrency vs Sequential" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/ThreadPoolExecutor-Multithreading-2563EB?style=flat-square" alt="Multithreading" />
  <img src="https://img.shields.io/badge/Matplotlib-Gr%C3%A1ficos-11557C?style=flat-square" alt="Matplotlib" />
</p>

## Sobre o Projeto

Benchmark em **Python** para medir o ganho de desempenho de operações **I/O-bound** (100 requisições HTTP `GET` para a API JSONPlaceholder) comparando a execução **sequencial** contra a execução **concorrente** via `concurrent.futures.ThreadPoolExecutor` variando o número de threads (`1, 2, 4, 6, 8, 10`).

## Resultados Gerados

<p align="center">
  <img src="resultados/bar.png" alt="Tempo de execução por número de threads" width="48%" />
  <img src="resultados/line.png" alt="Melhora percentual sobre a execução sequencial" width="48%" />
</p>

## Estrutura do Repositório

```text
Concurrency-vs-sequencial/
├── src/
│   ├── main.py        # Executa o benchmark e gera os gráficos em resultados/
│   ├── sequential.py  # Execução sequencial das 100 requisições
│   ├── parallel.py    # Execução concorrente com ThreadPoolExecutor
│   └── fetch.py       # Requisição HTTP via requests
└── resultados/
    ├── bar.png        # Gráfico de barras: tempo total por nº de threads
    └── line.png       # Gráfico de linha: ganho percentual (%)
```

## Como Executar

```bash
git clone https://github.com/charles-gabriel-cc/Concurrency-vs-sequencial.git
cd Concurrency-vs-sequencial/src

pip install requests numpy matplotlib
python main.py
```

Os gráficos atualizados são salvos automaticamente em `resultados/bar.png` e `resultados/line.png`.
