# from watchdog.observers import Observer 
# from watchdog.events import FileSystemEventHandler

# import csv 
# import os 
# import json 
# import time 
# import datetime

# class DownloadsHandler(FileSystemEventHandler): 
#     def on_modified(self, event): 
#         for filename in os.listdir(folder_to_track): 
#             src = f'{folder_to_track}/{filename}'
#             new_destination = f'{folder_destination}/{filename}'
#             os.rename(src, new_destination)
#             self._log(src, new_destination)

#     def _log(self, src : str, new_destination : str): 
#         with open('/Users/nickrichardson/Desktop/personal/projects/pyauto/downloads_logging.csv', 'a') as logging_file: 
#             logging_writer = csv.writer(logging_file)

#             current = datetime.datetime.now()  # time 
#             str_fmt = '%m %d %Y %H:%M:%S'      # time string formatting 
#             label = -1                         # class label 

#             log = [src, new_destination, current.strftime(str_fmt), label]
#             logging_writer.writerow(log)

# folder_to_track = 'tracking'
# folder_destination = 'destination'

# event_handler = DownloadsHandler() 
# observer = Observer() 
# observer.schedule(event_handler, folder_to_track, recursive=True)
# observer.start() 

# try: 
#     while True: 
#         time.sleep(10)
# except KeyboardInterrupt: 
#     observer.stop()
# observer.join()
import click 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

import csv 
import os 
import json 
import shutil
import time 
import datetime

# test and prod profiles
test_profile = {'tracking':  '/Users/nickrichardson/Desktop/personal/projects/pyauto/tracking', \
        'destination': '/Users/nickrichardson/Desktop/personal/projects/pyauto/destination'}
prod_profile = {'tracking':  '/Users/nickrichardson/Desktop/personal/projects/pyauto/test_folder_to_track', \
        'destination': '/Users/nickrichardson/Desktop/personal/projects/pyauto/test_folder_destination'}

class DownloadsHandler(FileSystemEventHandler): 

    def __init__(self, folder_to_track : str, folder_destination : str): 
        super().__init__()
        self.folder_destination = folder_destination
        self.folder_to_track = folder_to_track

    def on_modified(self, event): 
        for filename in os.listdir(self.folder_to_track): 
            src = f'{self.folder_to_track}/{filename}'
            new_destination = f'{self.folder_destination}/{filename}'
            shutil.move(src, new_destination)
            self._log(src, new_destination)

    def _log(self, src : str, new_destination : str): 
        with open('/Users/nickrichardson/Desktop/personal/projects/pyauto/downloads_logging.csv', 'a') as logging_file: 
            logging_writer = csv.writer(logging_file)

            current = datetime.datetime.now()  # time 
            str_fmt = '%m %d %Y %H:%M:%S'      # time string formatting 
            label = -1                         # class label 

            log = [src, new_destination, current.strftime(str_fmt), label]
            logging_writer.writerow(log)


@click.command()
@click.option("--profile", default='prod', help="Which profile to run the autofilehander in. This controls which folders are being watched.")
def main(profile): 
    # profile_setting = prod_profile if profile == 'prod' else test_profile
    profile_setting = test_profile
    print(f'profile setting: {profile_setting}')

    event_handler = DownloadsHandler(profile_setting['tracking'], profile_setting['destination']) 
    observer = Observer() 
    observer.schedule(event_handler, event_handler.folder_to_track, recursive=True)
    observer.start() 

    try: 
        while True: 
            time.sleep(10)
    except KeyboardInterrupt: 
        observer.stop()
    observer.join()

main() 
