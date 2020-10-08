from typing import Callable


class Solution:
    def __init__(self, func: Callable, **kwargs):
        self.name = kwargs.get("name") or func.__name__
        self.callback = func

    def __call__(self, *args, **kwargs):
        if self.cls is not None:
            return self.callback(self.cls, *args, **kwargs)
        return self.callback(*args, **kwargs)

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, func: Callable):
        self._callback = func
        self.cls = getattr(func, "cls", None)
