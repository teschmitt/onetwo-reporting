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
    'rtt_med': 'RTT (Median',
    '*': 'All stats'}

seaborn_themes = [t for t in plt.style.available if not t.startswith('_')]

seaborn_contexts = ['paper', 'notebook', 'talk', 'poster']
