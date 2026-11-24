<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a8a,50:2563eb,100:38bdf8&height=170&section=header&text=Concurrency%20vs%20Sequential&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=40&desc=Benchmark%20de%20Requisi%C3%A7%C3%B5es%20HTTP%20em%20Python%20com%20ThreadPoolExecutor&descAlignY=65&descSize=15" width="100%" alt="Banner" />
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/ThreadPoolExecutor-Multithreading-2563EB?style=for-the-badge" alt="Multithreading" />
  <img src="https://img.shields.io/badge/Matplotlib-Gr%C3%A1ficos-11557C?style=for-the-badge" alt="Matplotlib" />
</p>

---

## 📖 Sobre o Projeto

Benchmark em **Python** para medir o ganho de desempenho de operações **I/O-bound** (100 requisições HTTP `GET` para a API JSONPlaceholder) comparando a execução **sequencial** contra a execução **concorrente** via `concurrent.futures.ThreadPoolExecutor` variando o número de threads (`1, 2, 4, 6, 8, 10`).

---

## 📊 Resultados Gerados

<p align="center">
  <img src="resultados/bar.png" alt="Tempo de execução por número de threads" width="48%" />
  <img src="resultados/line.png" alt="Melhora percentual sobre a execução sequencial" width="48%" />
</p>

---

## 📂 Estrutura do Repositório

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

---

## 🚀 Como Executar

```bash
git clone https://github.com/charles-gabriel-cc/Concurrency-vs-sequencial.git
cd Concurrency-vs-sequencial/src

pip install requests numpy matplotlib
python main.py
```

Os gráficos atualizados são salvos automaticamente em `resultados/bar.png` e `resultados/line.png`.
