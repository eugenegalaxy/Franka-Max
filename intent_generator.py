import random


class Intents(object):
    ''' Container for all intents that can be issued by Max Interface.
        NOTE: Created to simulate intents input.
    '''
    FETCH_OBJECTS = ['bottom_cover', 'pcb', 'fuse_one', 'fuse_two', 'top_cover']
    COLORS = ['blue', 'white', 'black']
    INTENTS = ['BringPart', 'TaskCheck', 'PauseTask', 'ContinueTask',
               'ActionConfirmation', 'Stop', 'Start', 'FullAssembly', 'MoveHome', 'AutoAssembly']

    def __init__(self):
        pass

    def generate_BringPart(self, fetch_object=None, color=None):
        intent = self.INTENTS[0]

        if fetch_object is not None:
            if fetch_object == 'bottom_cover' or fetch_object == 'top_cover':
                err_str0 = '"color" argument has not been provided for a chosen object "{}".'.format(fetch_object)
                assert(color is not None), err_str0
            err_str1 = 'Argument {0} is not in the list of available objects. Choose one from: {1}'.format(
                fetch_object, self.FETCH_OBJECTS)
            assert(fetch_object in self.FETCH_OBJECTS), err_str1

        if color is not None:
            err_str2 = '"fetch_object" argument has not been provided for a chosen color "{}".'.format(color)
            assert(fetch_object is not None), err_str2
            err_str3 = 'Argument {0} is not in the list of available objects. Choose one from: {1}'.format(
                color, self.COLORS)
            assert(color in self.COLORS), err_str3
            err_str4 = '"{0}" object cannot be of "{1}" color!'.format(fetch_object, color)
            assert(fetch_object == 'bottom_cover' or fetch_object == 'top_cover'), err_str4

        if fetch_object is None and color is None:
            fetch_object = random.choice(self.FETCH_OBJECTS)
            if fetch_object == 'bottom_cover' or fetch_object == 'top_cover':
                color = random.choice(self.COLORS)
            else:
                color = None

        request = {'Intent': intent, 'Object': fetch_object, 'Color': color}
        return request

    def generate_TaskCheck(self):
        return {'Intent': self.INTENTS[1]}

    def generate_PauseTask(self):
        return {'Intent': self.INTENTS[2]}

    def generate_ContinueTask(self):
        return {'Intent': self.INTENTS[3]}

    def generate_ActionConfirmation(self):
        return {'Intent': self.INTENTS[4]}

    def generate_Stop(self):
        """ Lock the mechanical brakes on Franka."""
        return {'Intent': self.INTENTS[5]}

    def generate_Start(self):
        """ Release the mechanical brakes on Franka. Takes around 11 seconds."""
        return {'Intent': self.INTENTS[6]}

    def generate_FullAssembly(self, color):
        err_str3 = 'Argument {0} is not in the list of available objects. Choose one from: {1}'.format(
            color, self.COLORS)
        assert(color in self.COLORS), err_str3

        intent = self.INTENTS[7]
        request = {'Intent': intent, 'Color': color}
        return request

    def generate_AutoAssembly(self, color):
        err_str3 = 'Argument {0} is not in the list of available objects. Choose one from: {1}'.format(
            color, self.COLORS)
        assert(color in self.COLORS), err_str3

        intent = self.INTENTS[9]
        request = {'Intent': intent, 'Color': color}
        return request

    def generate_MoveHome(self):
        intent = self.INTENTS[8]
        request = {'Intent': intent}
        return request

    def generate_random_intent(self):
        options = [0, 1, 2, 3, 4, 5, 6, 7]
        selected_option = random.choice(options)
        if selected_option == 0:
            return self.generate_BringPart()
        elif selected_option == 1:
            return self.generate_TaskCheck()
        elif selected_option == 2:
            return self.generate_PauseTask()
        elif selected_option == 3:
            return self.generate_ContinueTask()
        elif selected_option == 4:
            return self.generate_ActionConfirmation()
        elif selected_option == 5:
            return self.generate_Stop()
        elif selected_option == 6:
            return self.generate_Start()
        elif selected_option == 7:
            return self.generate_FullAssembly('blue')
        elif selected_option == 8:
            return self.generate_MoveHome()
        else:
            return self.generate_AutoAssembly('blue')
