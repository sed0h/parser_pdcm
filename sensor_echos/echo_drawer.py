import matplotlib.pyplot as plt


def draw_echos(ns, hs):
    # plt.
    plt.plot(ns, hs, linewidth=1)
    for a, b in zip(ns, hs):
        if (a % 5) == 0:
            plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=3)

    line_xs = range(40, 301)
    line_ys = [1000] * 261
    plt.plot(line_xs, line_ys)
    for a, b in zip(line_xs, line_ys):
        if a == 40 or a == 300:
            plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=8)

    plt.show()
