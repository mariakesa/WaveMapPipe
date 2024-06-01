from clustering import WaveMapEAPClustering


def pipeline(task_name: str, **kwargs):
    task_mapping = {
        "wavemap-eap-clustering": WaveMapEAPClustering,
    }
    task = task_mapping[task_name]
    return task(**kwargs)
