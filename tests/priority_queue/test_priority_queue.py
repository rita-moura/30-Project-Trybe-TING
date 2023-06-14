from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queueing = PriorityQueue()

    priority_queueing.enqueue({"qtd_linhas": 2})
    priority_queueing.enqueue({"qtd_linhas": 10})
    priority_queueing.enqueue({"qtd_linhas": 3})
    priority_queueing.enqueue({"qtd_linhas": 6})

    assert len(priority_queueing) == 4
    assert priority_queueing.search(1) == {"qtd_linhas": 3}

    given = priority_queueing.dequeue()
    assert len(priority_queueing) == 3
    assert given == {"qtd_linhas": 2}

    given = priority_queueing.dequeue()
    assert len(priority_queueing) == 2
    assert given == {"qtd_linhas": 3}
    with pytest.raises(IndexError):
        priority_queueing.search(10)
