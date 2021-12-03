import matplotlib.pyplot as plt

stat_options = {
    'sim_time': 'Simulation time',
    'created': 'Created Messages',
    'started': 'Started Messages',
    'relayed': 'Relayed Messages',
    'aborted': 'Aborts Messages',
    'dropped': 'Dropped Messages',
    'removed': 'Removed Messages',
    'delivered': 'Delivered Messages',
    'delivery_prob': 'Delivery Probability',
    'response_prob': 'Response Probability',
    'overhead_ratio': 'Overhead Ratio',
    'latency_avg': 'Latency (Average)',
    'latency_med': 'Latency (Median)',
    'hopcount_avg': 'Hopcount (Average)',
    'hopcount_med': 'Hopcount (Median)',
    'buffertime_avg': 'Buffertime (Average)',
    'buffertime_med': 'Buffertime (Median)',
    'rtt_avg': 'RTT (Average)',
    'rtt_med': 'RTT (Median)',
    '*': 'All stats'}

seaborn_palettes = ['deep', 'muted', 'bright', 'pastel', 'dark', 'colorblind']
seaborn_styles = ['white', 'dark', 'whitegrid', 'darkgrid', 'ticks']
seaborn_contexts = ['paper', 'notebook', 'talk', 'poster']


# Default values for command line options

DEFAULT_GLOB = ['*MessageStats*.txt']
DEFAULT_OUTPUT_DIR = './images/'
DEFAULT_GRAPH_OUTPUT_FMT = 'PNG'
DEFAULT_REPORTS_DIR = './reports/'
DEFAULT_GRAPH_CONTEXT = 'paper'
DEFAULT_GRAPH_PALETTE = 'muted'
DEFAULT_GRAPH_STYLE = 'whitegrid'
DEFAULT_STAT = ['delivery_prob']
