import matplotlib.pyplot as plt
import numpy as np


def read_data(filename):
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if not line.startswith("#"):  # If 'line' is not a header
                data.append([int(word) for word in line.split(",")])
    return data


if __name__ == "__main__":
    # Load score data
    class_kr = read_data("5th/data/class_score_kr.csv")
    class_en = read_data("5th/data/class_score_en.csv")

    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40 / 125 * midterm + 60 / 100 * final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(midterm_kr, final_kr, "ro", markersize=4)
    plt.plot(midterm_en, final_en, "b+", markersize=4)
    plt.xlim([0, 125])
    plt.ylim([0, 100])
    plt.xlabel("Midterm scores")
    plt.ylabel("Final scores")
    plt.legend(["Korean", "English"])
    plt.grid(True)

    # TODO) Plot total scores as a histogram
    plt.subplot(1, 2, 2)
    bins = np.arange(0, 101, 5)
    plt.hist(total_kr, bins=bins, color="r", alpha=0.7)
    plt.hist(total_en, bins=bins, color="b", alpha=0.7)
    plt.legend(["Korean", "English"])
    plt.xlim([0, 100])
    plt.xlabel("Total Scores")
    plt.ylabel("The number of students")
    plt.grid(True)

    plt.show()
