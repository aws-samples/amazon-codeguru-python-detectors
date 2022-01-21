#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=multiprocessing-garbage-collection-prevention@v1.0 defects=1}
def garbage_collect_noncompliant(self):
    from multiprocessing import Pipe
    pipe = Pipe()
    try:
        # Trigger a refresh.
        self.assertFalse(
            client._MongoReplicaSetClient__monitor.isAlive())

        client.disconnect()
        self.assertSoon(
            lambda: client._MongoReplicaSetClient__monitor.isAlive())

        client.db.collection.find_one()
    except Exception:
        traceback.print_exc()
        pipe.send(True)


def multiprocessing_noncompliant():
    from multiprocessing import Process, Pipe
    parent_connection, child_connection = Pipe()
    # Noncompliant: fails to pass the parent process object to child processes.
    process = Process(target=garbage_collect_noncompliant)
    process.start()

# {/fact}


# {fact rule=multiprocessing-garbage-collection-prevention@v1.0 defects=0}
def garbage_collect_compliant(self, pipe):
    try:
        # Trigger a refresh.
        self.assertFalse(
            client._MongoReplicaSetClient__monitor.isAlive())

        client.disconnect()
        self.assertSoon(
            lambda: client._MongoReplicaSetClient__monitor.isAlive())

        client.db.collection.find_one()
    except Exception:
        traceback.print_exc()
        pipe.send(True)


def multiprocessing_compliant():
    from multiprocessing import Process, Pipe
    parent_connection, child_connection = Pipe()
    # Compliant: parent process object is passed to its child processes.
    process = Process(target=garbage_collect_compliant,
                      args=(child_connection,))
    process.start()
# {/fact}
