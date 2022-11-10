from celery import shared_task
from .worker import process_pipeline
from celery.result import AsyncResult
import numpy as np
import threading

def get_add_task_user_info(task_id):
    """
    return task info for the given task_id
    """
    task_result = AsyncResult(task_id)
    return [{"username": item, "status": task_result.info[item]} for item in task_result.info]


@shared_task(bind=True, retry_kwargs={"max_retries": 1},
             name='high_priority_tasks:get_users_data')
def get_users_data(self, args: list):
    meta = {}
    for item in args:
        meta[item] = "PENDING"
    self.update_state(state='PROGRESS', meta=meta)
    splits = np.array_split(args, 5)
    threads = []
    for split_item in splits:
        x = threading.Thread(target=process_pipeline, args=(self, split_item, meta))
        x.start()
        threads.append(x)
    for thread in threads:
        thread.join()
    return meta
