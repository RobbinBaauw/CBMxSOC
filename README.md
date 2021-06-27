# CBMxSOC

CBMxSOC is an algorithm that is able to solve the Multi-Agent Pathfinding with Matching (MAPFM) problem. This repository is part of a paper describing this algorithm. This paper can be found [here](TODO).

## Running the code
The main thing to do, is to make a copy of `src/example.env.yaml` to `src/env.yaml`, and change this accordingly. The next couple of sections will indicate the different types of things that can then be done.

### [mapf.nl](https://mapf.nl)
On this website, purpose built for this and previous related research papers, one can benchmark MAPFM solvers on different maps. In order to run, fill in an API token in `server-problem.api-token` and set `run-benchmark: no` in `src/env.yaml`. Other options to tweak the interaction and debugging options are also available. Next, run `main.py`.

### Benchmarks
All maps and data used in the paper are available in `maps/` and `data/` respectively. In order to run these benchmarks, set `run-benchmark: yes` and set the correct `benchmark.root` in `src/env.yaml`. Other options to tweak the amounts of samples, cores and timesouts are also available. Next, run `main.py`.

In order to plot these benchmark results, run `benchmark_drawer.py`. This will generate PDF images in `data/`. When data is received that is generated by [the benchmarker in this repository](https://github.com/jonay2000/research-project), run the `jonay2000_to_csv.py` script. This will generate matching data files which can subsequently be processed by `benchmark_drawer.py`.

## OR-tools
The implementation depends on a fork of Google's OR-tools. Upon checking out this fork, the following commands can be run to build and install it:
```
cd or-tools
cmake -DCMAKE_CXX_COMPILER_LAUNCHER=ccache -S. -Bbuild -DBUILD_PYTHON=ON
cmake --build build --target python_package -v -j24 
pip install ./build/python
```