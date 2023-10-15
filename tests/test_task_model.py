import math

import attrs
from tickthon import Task, dict_to_task
from tickthon._task_utils import _get_focus_time, _get_task_date


def test_dict_to_task(dict_task):
    expected_task = Task(ticktick_id="60c8d7b1e9b80e0595353bc6",
                         ticktick_etag="muu17zqq",
                         created_date="2021-06-15",
                         status=0,
                         title="Automation tasks",
                         focus_time=0.1,
                         deleted=0,
                         tags=("test", "unit"),
                         project_id="5f30772022d478db3ad1a9c2",
                         timezone="America/Bogota",
                         due_date="2023-08-03",
                         )

    task = dict_to_task(dict_task)

    assert attrs.asdict(task) == attrs.asdict(expected_task)


def test_get_ticktick_focus_time():
    rawt_focus_time = {"focusSummaries": [{"pomoDuration": 0, "stopwatchDuration": 100},
                                          {"pomoDuration": 260, "stopwatchDuration": 0},
                                          ]}

    focus_time = _get_focus_time(rawt_focus_time)

    assert math.isclose(focus_time, 0.1)


def test_get_focus_time():
    raw_focus_time = {"focus_time": 0.1}

    focus_time = _get_focus_time(raw_focus_time)

    assert math.isclose(focus_time, 0.1)


def test_get_date():
    raw_task_date = "2023-08-03T19:15:00.000+0000"
    raw_timezone = "America/Bogota"

    task_date = _get_task_date(raw_timezone, raw_task_date)

    assert task_date == "2023-08-03"
