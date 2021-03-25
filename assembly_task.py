from intent_generator import Intents
from FrankaMax import FrankaMax
from time import sleep


def DEMO_show_possible_intents():
    """Just a demo to showcase how to use intent generator.
    """
    IT = Intents()
    # When used with no arguments -> will generate a BringPart intent with random object/color
    print(IT.generate_BringPart())
    # When used with arguments -> will check if the object/color combination is possible and generate BringPart intent.
    print(IT.generate_BringPart(fetch_object='bottom_cover', color='blue'))
    print(IT.generate_TaskCheck())
    print(IT.generate_PauseTask())
    print(IT.generate_ContinueTask())
    print(IT.generate_ActionConfirmation())
    print(IT.generate_Start())
    print(IT.generate_Stop())
    print(IT.generate_FullAssembly('blue'))
    # Randomly select and generate an intent from the available options.
    print(IT.generate_random_intent())

IT = Intents()
Franka = FrankaMax()

start = IT.generate_Start()
Franka.DoAction(start)

# full_assembly = IT.generate_FullAssembly(color='blue')
# Franka.DoAction(full_assembly)

auto_assembly = IT.generate_AutoAssembly(color='blue')
Franka.DoAction(auto_assembly)

stop = IT.generate_Stop()
Franka.DoAction(stop)
print('Program has finished successfully.')

# DEMO_show_possible_intents()
