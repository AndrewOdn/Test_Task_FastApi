import os
from functools import lru_cache
from kombu import Queue
from settings import rabbit_url


def route_task(name, args, kwargs, options, task=None, **kw):
    if ":" in name:
        queue, _ = name.split(":")
        return {"queue": queue}
    return {"queue": "celery"}


class BaseConfig:
    os.environ.setdefault('C_FORCE_ROOT', 'true')
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL", rabbit_url)
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND", "rpc://")
    CELERY_TASK_QUEUES: list = (
        Queue("low_priority_tasks"),
        Queue("high_priority_tasks"),
    )

    CELERY_TASK_ROUTES = (route_task,)


class DevelopmentConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "development": DevelopmentConfig,
    }
    config_name = os.environ.get("CELERY_CONFIG", "development")
    config_cls = config_cls_dict[config_name]
    return config_cls()


settings = get_settings()
