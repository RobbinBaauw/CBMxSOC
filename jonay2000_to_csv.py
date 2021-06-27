import csv
from pathlib import Path
from typing import List

from src.benchmarks.parser import JonathanCSVLayout

ROOT_DIR = Path("data")

if __name__ == "__main__":
    for map_dir in ROOT_DIR.glob("./comparison_*"):
        if not map_dir.is_dir():
            continue

        data_points: List[JonathanCSVLayout] = []

        for file in map_dir.glob("./*.txt"):
            algorithm = file.stem.removeprefix("results_")
            for line in file.read_text().splitlines():
                line_split = line.split(": ")
                amount_of_agents = int(line_split[0])
                runtimes = eval(line_split[1])

                for i, runtime in enumerate(runtimes):
                    data_points.append((f"{map_dir.name}_{i}",
                                        amount_of_agents, runtime, algorithm))

        with open(map_dir / f"{map_dir.name}.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerows(data_points)

            print(f"Written {map_dir}")
