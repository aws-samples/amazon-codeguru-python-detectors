#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=incorrect-usage-of-process-terminate-api@v1.0 defects=1}
def put_object_to_queue_noncompliant(queue):
    try:
        queue.put([42, None, 'hello'])
    finally:
        queue.task_done()


def shared_queue_noncompliant():
    from multiprocessing.context import Process
    from multiprocessing.queues import Queue
    queue = Queue()
    process = Process(target=put_object_to_queue_noncompliant, args=(queue,))
    process.start()
    print(queue.get())  # prints "[42, None, 'hello']"
    # Noncompliant: uses 'Process.terminate' API on shared resources making
    # queue liable to become corrupted and may become unusable by other process
    process.terminate()
    # trying to access corrupt queue
    queue.put([50, None, 'hello'])
# {/fact}


# {fact rule=incorrect-usage-of-process-terminate-api@v1.0 defects=0}
def put_object_to_queue_compliant(queue):
    try:
        queue.put([42, None, 'hello'])
    finally:
        queue.task_done()


def shared_queue_compliant():
    from multiprocessing.context import Process
    from multiprocessing.queues import Queue
    queue = Queue()
    process = Process(target=put_object_to_queue_compliant, args=(queue,))
    process.start()
    print(queue.get())  # prints "[42, None, 'hello']"
    # Compliant: avoids using 'Process.terminate' API on shared resources
    # making the queue accessible.
    queue.join()
    # accessing safe queue object
    queue.put([50, None, 'hello'])
# {/fact}
