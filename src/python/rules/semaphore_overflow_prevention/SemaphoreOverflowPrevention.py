# {fact rule=semaphore-overflow-prevention@v1.0 defects=1}
def post_tasks_compliant(jobs, es_url):
    import multiprocessing
    import requests
    import urlparse
    jobs = multiprocessing.JoinableQueue()
    while True:
        try:
            image, image_name, tag = jobs.get()
            formatted_es_url = es_url.format(image_name)
            files = {'file': image.content, 'tag': tag}
            r = requests.post(formatted_es_url, files=files)
        finally:
            # Noncompliant: fails to call JoinableQueue.task_done()
            # for each task removed from the JoinableQueue.
            print("Task Done!!")
# {/fact}


# {fact rule=semaphore-overflow-prevention@v1.0 defects=0}
def post_tasks_compliant(jobs, es_url):
    import multiprocessing
    import requests
    import urlparse
    jobs = multiprocessing.JoinableQueue()
    while True:
        try:
            image, image_name, tag = jobs.get()
            formatted_es_url = es_url.format(image_name)
            files = {'file': image.content, 'tag': tag}
            r = requests.post(formatted_es_url, files=files)
        finally:
            # Compliant: calls JoinableQueue.task_done()
            # for each task removed from the JoinableQueue.
            jobs.task_done()
# {/fact}
