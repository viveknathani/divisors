import matplotlib.pyplot as plt
import matplotlib.animation as animation

def divisor_sum(n, k):
    return sum([i**k for i in range(1, n + 1) if n % i == 0])

def abundancy_index(n):
    return divisor_sum(n, 1) / n

def plot_divisor_sums():
    n = 250
    k_values = list(range(1, 8))
    n_values = list(range(1, n + 1))
    divisor_sums = []
    
    for k in k_values:
        divisor_sums.append([divisor_sum(i, k) for i in n_values])
    
    figure, axes = plt.subplots()
    line, = axes.plot([], [], color='red')
    title = axes.text(0.5, 1.05, "", size=15, ha="center", transform=axes.transAxes)

    def init():
        axes.set_xlim(1, n)
        axes.set_ylim(0, 1)
        return line, title
    
    # update function
    def update(frame):
        k = k_values[frame]
        y_values = divisor_sums[frame]
        axes.clear()
        axes.set_xlim(1, n)
        axes.set_ylim(1, max(y_values))
        line.set_data(n_values, y_values)
        title.set_text(f"Sigma function $\\sigma_{{{k}}}(n)$")
        new_line, = axes.plot(n_values, y_values, color='red')
        return new_line, title
    
    _ = animation.FuncAnimation(figure, update, frames=len(k_values), interval=1000, repeat=False, init_func=init)
    plt.show()

def plot_abundancy_index():
    n = 5_000
    n_values = list(range(1, n + 1))
    abundancy_indices = [abundancy_index(i) for i in n_values]
    
    plt.scatter(n_values, abundancy_indices)
    plt.title(f"abundancy index = $\\sigma_1(n)/n$")
    plt.show()

def main():
    plot_abundancy_index()


if __name__ == "__main__":
    main()
