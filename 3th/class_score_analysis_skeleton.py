def read_data(filename):
    # TODO) Read `filename` as a list of integer numbers
    data = []
    with open(filename, "r") as f:
        for line in f.readlines():
            if line.strip().startswith("#"):
                continue
            splited = line.split(",")
            splited[0] = int(splited[0].strip())
            splited[1] = int(splited[1].strip())
            data.append(splited)
    return data


def calc_weighted_average(data_2d, weight):
    # TODO) Calculate the weighted averages of each row of `data_2d`
    average = []
    for score in data_2d:
        average.append(weight[0] * score[0] + weight[1] * score[1])
    return average


def analyze_data(data_1d):
    # TODO) Derive summary of the given `data_1d`
    # Note) Please don't use NumPy and other libraries. Do it yourself.
    n = len(data_1d)
    mean = sum(data_1d) / n
    squareSum = 0
    for score in data_1d:
        squareSum += score**2
    var = squareSum / n - mean**2
    median = (sorted(data_1d))[int(n / 2)]
    return mean, var, median, min(data_1d), max(data_1d)


if __name__ == "__main__":
    data = read_data("3th/data/class_score_en.csv")
    if data and len(data[0]) == 2:  # Check 'data' is valid
        average = calc_weighted_average(data, [40 / 125, 60 / 100])

        # Write the analysis report as a markdown file
        with open("3th/class_score_analysis.md", "w") as report:
            report.write("### Individual Score\n\n")
            report.write("| Midterm | Final | Average |\n")
            report.write("| ------- | ----- | ----- |\n")
            for (m_score, f_score), a_score in zip(data, average):
                report.write(f"| {m_score} | {f_score} | {a_score:.3f} |\n")
            report.write("\n\n\n")

            report.write("### Examination Analysis\n")
            data_columns = {
                "Midterm": [m_score for m_score, _ in data],
                "Final": [f_score for _, f_score in data],
                "Average": average,
            }
            for name, column in data_columns.items():
                mean, var, median, min_, max_ = analyze_data(column)
                report.write(f"* {name}\n")
                report.write(f"  * Mean: **{mean:.3f}**\n")
                report.write(f"  * Variance: {var:.3f}\n")
                report.write(f"  * Median: **{median:.3f}**\n")
                report.write(f"  * Min/Max: ({min_:.3f}, {max_:.3f})\n")
