def notify_everyone():
    """
    This is the method that will be called by each job instance created by the scheduler.
    That is, this will be executed every X seconds.
    """

    print("Notification job starting")
    # check feed
    # load players
    # etc ...
    # if we need to notify users, send the sms to each one

    # here we use multithreading (e.g 10 parallel tasks to send the sms messages)
    # https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing
    print("Notification finished!")
