from FrankaWebAPI import franka_open_brakes, franka_close_brakes, franka_execute_task, franka_stop_task
from time import sleep, time


class FrankaMax():
    """Interface between robot assistant Max and Franka Emika robot.
    """
    FETCH_OBJECTS = ['bottom_cover', 'pcb', 'fuse_one', 'fuse_two', 'top_cover']

    def __init__(self, hostname='172.27.23.65', login='Panda', password='panda1234'):
        # Credentials to connect to Franka Web interface.
        self.HOSTNAME = hostname
        self.LOGIN = login
        self.PASSWORD = password

    def DoAction(self, intent):
        err_str0 = 'Argument "intent" must be a dictionary, see class "Intents" in intent_genetator.py'
        assert(type(intent) is dict), err_str0

        intent_key = intent['Intent']

        if intent_key == 'BringPart':
            obj_name = intent['Object']
            if 'Color' in intent:
                color = intent['Color']
            else:
                color = None
            self.fetch_one_object(obj_name, color)
        elif intent_key == 'TaskCheck':
            # return function name of task checking
            pass
        elif intent_key == 'PauseTask':
            # return function name of pausing task
            # check if it is even feasible...
            pass
        elif intent_key == 'ContinueTask':
            # same as PauseTask
            pass
        elif intent_key == 'ActionConfirmation':
            # how to make it, open gripper?
            pass
        elif intent_key == 'Stop':
            self.close_brakes()
        elif intent_key == 'Start':
            self.open_brakes()
        elif intent_key == 'FullAssembly':
            if 'Color' in intent:
                color = intent['Color']
            else:
                color = None
            self.fetch_all_objects(color)
        elif intent_key == 'MoveHome':
            self.move_home()
        elif intent_key == 'AutoAssembly':
            if 'Color' in intent:
                color = intent['Color']
            else:
                color = None
            self.auto_assembly(color)

    def stop_task(self):
        franka_stop_task(self.HOSTNAME, self.LOGIN, self.PASSWORD)

    def open_brakes(self):
        franka_open_brakes(self.HOSTNAME, self.LOGIN, self.PASSWORD)

    def close_brakes(self):
        self.stop_task()
        franka_close_brakes(self.HOSTNAME, self.LOGIN, self.PASSWORD)

    def move_home(self):
        task_name = '_move_home'
        franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)

    def auto_assemble_bottom_cover(self):
        self.move_home()
        sleep(5)
        task_name = 'self_assembly_body'
        franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)

    def auto_assemble_pcb(self):
        task_name = 'self_assembly_pcb'
        franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)

    # NOTE: this function is written only for 1 color objects. (blue)
    def auto_assembly(self, color):
        assert(color == 'blue'), 'TEST MODE: only "blue" color is available for now...'
        self.open_brakes()
        t1 = time()
        self.auto_assemble_bottom_cover()
        sleep(38)
        self.auto_assemble_pcb()
        sleep(23)

    # NOTE: this function is written only for 1 color objects. (blue)
    def fetch_one_object(self, obj, color):
        if color is not None:
            assert(color == 'blue'), 'TEST MODE: only "blue" color is available for now...'

        if obj == self.FETCH_OBJECTS[0]:
            print('Fetching bottom cover')
            task_name = 'assembly_body'  # this has to match with task name in Franka Web Desk interface
            franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)
        elif obj == self.FETCH_OBJECTS[1]:
            print('Fetching bottom cover')
            task_name = 'assembly_pcb'  # this has to match with task name in Franka Web Desk interface
            franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)
        elif obj == self.FETCH_OBJECTS[2]:
            print('Fetching bottom cover')
            task_name = 'assembly_fuse_1'  # this has to match with task name in Franka Web Desk interface
            franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)
        elif obj == self.FETCH_OBJECTS[3]:
            print('Fetching bottom cover')
            task_name = 'assembly_fuse_2'  # this has to match with task name in Franka Web Desk interface
            franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)
        elif obj == self.FETCH_OBJECTS[4]:
            print('Fetching bottom cover')
            task_name = 'assembly_cover'  # this has to match with task name in Franka Web Desk interface
            franka_execute_task(self.HOSTNAME, self.LOGIN, self.PASSWORD, task_name)
        else:
            raise ValueError("Some unexpected object was passed and not caught previously.")

    # NOTE: this function is written only for 1 color objects. (blue)
    # NOTE 2: System currently doesnt check Franka's status -> so there are sleep()
    # breaks to give robot time to execute the tasks.
    def fetch_all_objects(self, color):
        """ A function to fetch all objects required to assembly 1 phone unit.
            Starts with moving releasing the brakes, homing Franka position, and fetching
            1. bottom cover, 2.PCB, 3.left fuse, 4.right fuse, 5.top cover.
        """
        assert(color == 'blue'), 'TEST MODE: only "blue" color is available for now...'

        self.open_brakes()
        self.move_home()
        sleep(8)
        self.fetch_one_object(self.FETCH_OBJECTS[0], color)
        sleep(20)
        self.fetch_one_object(self.FETCH_OBJECTS[1], color)
        sleep(30)
        self.fetch_one_object(self.FETCH_OBJECTS[2], color)
        sleep(25)
        self.fetch_one_object(self.FETCH_OBJECTS[3], color)
        sleep(25)
        self.fetch_one_object(self.FETCH_OBJECTS[4], color)
        sleep(20)
        print('Fetching sequence has been finishd.')
