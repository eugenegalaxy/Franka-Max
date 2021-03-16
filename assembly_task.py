from franka_web_API import franka_open_brakes, franka_execute_task
from time import sleep

# Example function calls
HOSTNAME = '172.27.23.65'
LOGIN = 'Panda'
PASSWORD = 'panda1234'

franka_open_brakes(HOSTNAME, LOGIN, PASSWORD)
# franka_close_brakes(HOSTNAME, LOGIN, PASSWORD)

task_name = '_move_home'
franka_execute_task(HOSTNAME, LOGIN, PASSWORD, task_name)

sleep(5)

input('Type any char to executive "assembly_body 1": ')
task_name = 'assembly_body'
franka_execute_task(HOSTNAME, LOGIN, PASSWORD, task_name)
