def calculate_pipeline_time(segment_delays, register_delay, num_tasks):
    k = len(segment_delays)
    t_cycle = max(segment_delays) + register_delay
    total_time = (k + num_tasks - 1) * t_cycle
    return t_cycle, total_time

delays = [50, 30, 95, 45]
reg_delay = 5
tasks = 100

t_cyc, t_tot = calculate_pipeline_time(delays, reg_delay, tasks)
print(f"{t_cyc=}, {t_tot=}")
