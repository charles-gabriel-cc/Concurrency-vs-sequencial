from sequential import sequential
from parallel import parallel
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    time_sequential = sequential()

    threads = [1, 2, 4, 6, 8, 10]
    parallels = []
    improvement = []
    for i in threads:
        time_concurrent = parallel(threads=i)
        parallels.append(time_concurrent)
        improvement.append((time_sequential - time_concurrent)*100/time_sequential)

    x = np.arange(len(threads))
    fig, ax = plt.subplots()

    width = 0.35
    rects1 = ax.bar(x - width/2, np.full(len(threads),time_sequential) , width, label='Sem Thread')
    rects2 = ax.bar(x + width/2, parallels, width, label='Com Thread')

    ax.set_ylabel('Segundos')
    ax.set_title('Tempo de execução por número de threads')
    ax.set_xticks(x, threads)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig('../resultados/bar.png')

    plt.clf()

    plt.plot(threads, improvement) 

    plt.xlabel("Número de threads") 
    plt.ylabel("%") 
    plt.title("Melhora sobre a execução sequencial") 

    plt.savefig('../resultados/line.png')
