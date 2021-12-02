# OneTwo Reporting

## User Guide
(for the developer guide, [see further down](#developer-guide))

OneTwo Reporting has three top level commands that can be executed on a batch of generated report text-files:

- ~~`diff`: Show differences between two simulation runs~~
- `graph`: Generate graph statistics of one or more simulation runs
- `stats`: Show statistics of one or more simulation runs in the console

### Usage

A command is followed by a set of options that define its behaviour. If no options are given,
sane defaults are used but there is no recovering from errors (e.g. if files are not found).

#### Common Defaults

- `--glob`(M): `*MessageStats*.txt`
- `--report-dir`: `./reports/`
- `--stat`(M): `delivery_prob`

Options marked with an (M) can be passed in more than once in order to define a list of values
for that option. [See here for an exmple](#compare-message-statistics-over-multiple-runs)

#### Main Program

The main program has no function other than to show version info or help.
Other than that, it mainly delegates the work to the top level of commands.

```text
$ toolkit.py --help                                   
Usage: toolkit.py [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version  Show version and exit.
  --help         Show this message and exit.

Commands:
  graph  Draw graphs based on the generated report files
  stats  Get stats from the generated report files
```

#### Toolkit Graph

`graph` will build graphs from reporting data files using the
[Seaborn library](https://seaborn.pydata.org/). Most notably, there are two parameters that get
passed on directly to Seaborn in order to define the appearance of the graphs:

- `--context`: Affects size of the labels, lines, and other elements of the plot. Can be either
  `paper`, `notebook`, `talk`, or `poster`.
  See https://seaborn.pydata.org/generated/seaborn.set_context.html for more details
- `--style`: Sets of properties that define the color of the background and whether
  a grid is enabled by default.

```text
$ toolkit.py graph --help
Usage: toolkit.py graph [OPTIONS]

  Draw graphs based on the generated report files

Options:
  -d, --report-dir PATH           Report directory.  [default: ./reports/]
  -f, --output-format [PNG|JPG]   [default: PNG]
  -g, --glob TEXT                 Glob pattern to look for in reports
                                  directory.  [default: *MessageStats*.txt]
  -o, --output-dir PATH           Output directory.  [default: ./images/]
  -s, --stat [*|aborted|buffertime_avg|buffertime_med|created|delivered|...]
                                  Name of the statistics value that should be
                                  parsed from the report files  [default:
                                  delivery_prob]
  -c, --context [notebook|paper|poster|talk]
                                  Seaborn context for the generated graphs
                                  [default: paper]
  -p, --palette [bright|colorblind|dark|deep|muted|pastel]
                                  Seaborn color palette for the generated
                                  graphs  [default: muted]
  -y, --style [dark|darkgrid|ticks|white|whitegrid]
                                  Seaborn theme for the generated graphs
                                  [default: whitegrid]
  --help                          Show this message and exit.
```

#### Toolkit Stats

`stats` will output Pandas dataframes of the reporting data to the console. To view multiple 
stat-fields at once, more than one `--stat` argument is allowed. The flag `--separate-tables`
can be used to output one table per stat.

```text
$ toolkit.py stats --help
Usage: toolkit.py stats [OPTIONS]

  Get stats from the generated report files

Options:
  -d, --report-dir PATH           Report directory.
  -g, --glob TEXT                 Glob pattern(s) to look for in reports
                                  directory.
  -o, --output-dir PATH           Output directory.
  -s, --stat [*|aborted|buffertime_avg|buffertime_med|created|delivered|delivery_prob|dropped|hopcount_avg|hopcount_med|latency_avg|latency_med|overhead_ratio|relayed|removed|response_prob|rtt_avg|rtt_med|sim_time|started]
                                  Name of the statistics value(s) that should
                                  be parsed from the report files
  -t, --separate-tables           Show all stats in separate tables
  --help                          Show this message and exit.
```


### Usage Examples

Assuming a user has reports from a series of simulation runs called

- `simrun_01_MessageStatsReport.txt`
- `simrun_02_MessageStatsReport.txt`
- ...
- `simrun_15_MessageStatsReport.txt`

in the directory `./reports/`, the following commands can be
issued to view different aspects of the reports:

##### Compare message statistics over multiple runs

To examine more than one statistic about the run(s), call `stats` with
multiple `--stat` options:

```text
$ toolkit.py stats --stat 'created' --stat 'delivered' --stat 'delivery_prob'

           created  delivered  delivery_prob
scenario                                        
simrun_01     1463        398         0.2720
simrun_02     1463        401         0.2741
...
simrun_14     1463        399         0.2727
simrun_15     1463        394         0.2693
```




## Developer Guide

### Dependencies

OneTwo Reporting is proud to be using the Poetry dependency management
and packaging tool. Install it as describe
[here](https://python-poetry.org/docs/#installation).

To install all dependencies, simply `cd` into the project directory and
run `poetry shell` and then `poetry install` and everything should work
out just fine.