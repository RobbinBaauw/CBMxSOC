from pathlib import Path

from src.benchmarks.graph import plot_data, GraphSettings, GraphSetting
from src.benchmarks.parser import parse_set, Field

data_path = Path("data")


def parse_ilp_ssp():
    ilp_profile_path = data_path / "ilp_ssp_profile"
    parsed_results = parse_set(ilp_profile_path)

    graph_settings = GraphSettings([
        GraphSetting(x_field=Field.MAP_NODES,
                     y_field=Field.PERCENTAGE_SOLVED,
                     line_field=Field.SOLVER,
                     title=None,
                     x_text="Number of map vertices",
                     y_text="Solved (%)",
                     scatter=False),
        GraphSetting(x_field=Field.NODES,
                     y_field=Field.RUNTIME,
                     line_field=Field.SOLVER,
                     title=None,
                     x_text="Number of created NF nodes",
                     y_text="Runtime (s)",
                     scatter=True),
    ],
                                   sync_x=False)

    plot_data(parsed_results, graph_settings, data_path / "ilp_ssp_graph.pdf")


def parse_teg():
    teg_path = data_path / "teg"
    parsed_results = parse_set(teg_path)

    graph_settings = GraphSettings([
        GraphSetting(x_field=Field.AGENTS,
                     y_field=Field.PERCENTAGE_SOLVED,
                     line_field=Field.SOLVER,
                     title=None,
                     x_text="Number of agents",
                     y_text="Solved (%)",
                     scatter=False),
        GraphSetting(x_field=Field.AGENTS,
                     y_field=Field.RUNTIME,
                     line_field=Field.SOLVER,
                     title=None,
                     x_text="Number of agents",
                     y_text="Runtime (s)",
                     scatter=False),
        GraphSetting(x_field=Field.NODES,
                     y_field=Field.RUNTIME,
                     line_field=Field.SOLVER,
                     title=None,
                     x_text="Number of created NF nodes",
                     y_text="Runtime (s)",
                     scatter=True,
                     x_scale="log"),
    ],
                                   sync_x=False)

    plot_data(parsed_results, graph_settings, data_path / "teg_graph.pdf")


def parse_comparison():
    for comparison in [
            "comparison_25percent_1teams", "comparison_25percent_3teams",
            "comparison_75percent_1teams", "comparison_75percent_3teams"
    ]:
        comparison_path = data_path / comparison
        parsed_results = parse_set(comparison_path)

        graph_settings = GraphSettings([
            GraphSetting(x_field=Field.AGENTS,
                         y_field=Field.PERCENTAGE_SOLVED,
                         line_field=Field.SOLVER,
                         title=None,
                         x_text=None,
                         y_text="Percentage solved (%)"),
            GraphSetting(x_field=Field.AGENTS,
                         y_field=Field.RUNTIME,
                         line_field=Field.SOLVER,
                         title=None,
                         x_text=None,
                         y_text="Runtime (s)",
                         plot_confidence_interval=True),
        ],
                                       sync_x=True)

        plot_data(parsed_results, graph_settings,
                  data_path / f"{comparison}_graph.pdf")


def parse_max_agents():
    max_agent_path = data_path / "max_agents"
    parsed_results = parse_set(max_agent_path)

    graph_settings = GraphSettings([
        GraphSetting(x_field=Field.AGENTS,
                     y_field=Field.PERCENTAGE_SOLVED,
                     line_field=None,
                     title=None,
                     x_text=None,
                     y_text="Percentage solved (%)"),
        GraphSetting(x_field=Field.AGENTS,
                     y_field=Field.RUNTIME,
                     line_field=None,
                     title=None,
                     x_text="Number of agents",
                     y_text="Runtime (s)",
                     plot_confidence_interval=True),
    ],
                                   sync_x=True)

    plot_data(parsed_results, graph_settings,
              data_path / f"max_agents_graph.pdf")


def parse_increasing_map_size():
    increasing_map_size = data_path / "increasing_map_size"
    parsed_results = parse_set(increasing_map_size)

    graph_settings = GraphSettings([
        GraphSetting(x_field=Field.MAP_NODES,
                     y_field=Field.PERCENTAGE_SOLVED,
                     line_field=None,
                     title=None,
                     x_text=None,
                     y_text="Percentage solved (%)"),
        GraphSetting(x_field=Field.MAP_NODES,
                     y_field=Field.RUNTIME,
                     line_field=None,
                     title=None,
                     x_text="Number of map vertices",
                     y_text="Runtime (s)",
                     plot_confidence_interval=True),
    ],
                                   sync_x=True)

    plot_data(parsed_results, graph_settings,
              data_path / f"increasing_map_graph.pdf")


if __name__ == "__main__":
    parse_ilp_ssp()
    parse_teg()
    parse_comparison()
    parse_max_agents()
    parse_increasing_map_size()
