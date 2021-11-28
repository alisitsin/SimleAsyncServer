from .sleep import SleepView, AsyncSleepView, ThreadSleepView
from .status import StatusView

VIEWS = [
    StatusView,
    SleepView,
    AsyncSleepView,
    ThreadSleepView
]
