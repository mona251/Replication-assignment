def test_positive_queue_creation():
    # Constants
    QUEUE_SIZE = 1256

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    is_full = queue.full()

    # Assertions
    assert isinstance(queue, module_0.Queue), "Queue instance should be of type Queue"
    assert queue.max == QUEUE_SIZE, "Queue max size should be set correctly"
    assert queue.head == 0, "Queue head should be initialized to 0"
    assert queue.tail == 0, "Queue tail should be initialized to 0"
    assert queue.size == 0, "Queue size should be initialized to 0"
    assert isinstance(queue.data, list), "Queue data should be a list"
    assert len(queue.data) == QUEUE_SIZE, "Queue data length should match the given size"
    assert is_full == False, "Queue should not be full initially"
def test_negative_queue_creation():
    # Constants
    INVALID_SIZE = -1

    # Assertion
    with pytest.raises(ValueError):
        module_0.Queue(INVALID_SIZE)
def test_enqueue_and_dequeue():
    # Constants
    QUEUE_SIZE = 3
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    success_1 = queue.enqueue(VALUE_1)
    success_2 = queue.enqueue(VALUE_2)

    dequeue_value = queue.dequeue()

    # Assertions
    assert success_1, "Enqueue should succeed"
    assert success_2, "Enqueue should succeed"
    assert queue.size == 2, "Queue size should be 2 after two enqueues"
    assert dequeue_value == VALUE_1, "Dequeued value should be the first enqueued value"
    assert queue.size == 1, "Queue size should be 1 after one dequeue"
def test_queue_full_and_empty():
    # Constants
    QUEUE_SIZE = 2
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    queue.enqueue(VALUE_1)
    queue.enqueue(VALUE_2)
    success = queue.enqueue(30)

    is_empty = queue.empty()

    # Assertions
    assert success == False, "Enqueue should fail when the queue is full"
    assert queue.size == QUEUE_SIZE, "Queue size should be equal to max size"
    assert is_empty == False, "Queue should not be empty"
def test_empty_queue():
    # Constants
    QUEUE_SIZE = 2

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    is_empty = queue.empty()

    # Assertions
    assert is_empty, "Queue should be empty after creation"
def test_enqueue_beyond_capacity():
    # Constants
    QUEUE_SIZE = 1
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    success_1 = queue.enqueue(VALUE_1)
    success_2 = queue.enqueue(VALUE_2)

    # Assertions
    assert success_1, "First enqueue should succeed"
    assert success_2 == False, "Second enqueue should fail as the queue is full"
    assert queue.size == 1, "Queue size should be 1 after one successful enqueue"
def test_full_queue_dequeue():
    # Constants
    QUEUE_SIZE = 1
    VALUE = 10

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)
    queue.enqueue(VALUE)

    # Execution
    dequeued_value = queue.dequeue()
    is_full = queue.full()

    # Assertions
    assert dequeued_value == VALUE, "Dequeued value should match the enqueued value"
    assert queue.size == 0, "Queue size should be 0 after dequeue"
    assert is_full == False, "Queue should not be full after dequeue"
import pytest

def test_positive_queue_creation():
    # Constants
    QUEUE_SIZE = 1256

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    is_full = queue.full()

    # Assertions
    assert isinstance(queue, module_0.Queue), "Queue instance should be of type Queue"
    assert queue.max == QUEUE_SIZE, "Queue max size should be set correctly"
    assert queue.head == 0, "Queue head should be initialized to 0"
    assert queue.tail == 0, "Queue tail should be initialized to 0"
    assert queue.size == 0, "Queue size should be initialized to 0"
    assert isinstance(queue.data, list), "Queue data should be a list"
    assert len(queue.data) == QUEUE_SIZE, "Queue data length should match the given size"
    assert is_full == False, "Queue should not be full initially"

def test_negative_queue_creation():
    # Constants
    INVALID_SIZE = -1

    # Assertion
    with pytest.raises(ValueError):
        module_0.Queue(INVALID_SIZE)

def test_enqueue_and_dequeue():
    # Constants
    QUEUE_SIZE = 3
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    success_1 = queue.enqueue(VALUE_1)
    success_2 = queue.enqueue(VALUE_2)

    dequeue_value = queue.dequeue()

    # Assertions
    assert success_1, "Enqueue should succeed"
    assert success_2, "Enqueue should succeed"
    assert queue.size == 2, "Queue size should be 2 after two enqueues"
    assert dequeue_value == VALUE_1, "Dequeued value should be the first enqueued value"
    assert queue.size == 1, "Queue size should be 1 after one dequeue"

def test_queue_full_and_empty():
    # Constants
    QUEUE_SIZE = 2
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    queue.enqueue(VALUE_1)
    queue.enqueue(VALUE_2)
    success = queue.enqueue(30)

    is_empty = queue.empty()

    # Assertions
    assert success == False, "Enqueue should fail when the queue is full"
    assert queue.size == QUEUE_SIZE, "Queue size should be equal to max size"
    assert is_empty == False, "Queue should not be empty"

def test_empty_queue():
    # Constants
    QUEUE_SIZE = 2

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    is_empty = queue.empty()

    # Assertions
    assert is_empty, "Queue should be empty after creation"

def test_enqueue_beyond_capacity():
    # Constants
    QUEUE_SIZE = 1
    VALUE_1 = 10
    VALUE_2 = 20

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)

    # Execution
    success_1 = queue.enqueue(VALUE_1)
    success_2 = queue.enqueue(VALUE_2)

    # Assertions
    assert success_1, "First enqueue should succeed"
    assert success_2 == False, "Second enqueue should fail as the queue is full"
    assert queue.size == 1, "Queue size should be 1 after one successful enqueue"

def test_full_queue_dequeue():
    # Constants
    QUEUE_SIZE = 1
    VALUE = 10

    # Setup
    queue = module_0.Queue(QUEUE_SIZE)
    queue.enqueue(VALUE)

    # Execution
    dequeued_value = queue.dequeue()
    is_full = queue.full()

    # Assertions
    assert dequeued_value == VALUE, "Dequeued value should match the enqueued value"
    assert queue.size == 0, "Queue size should be 0 after dequeue"
    assert is_full == False, "Queue should not be full after dequeue"
sh
pip install pytest
sh
pytest test_queue.py
