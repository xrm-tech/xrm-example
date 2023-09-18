from st2common.runners.base_action import Action

class TestAction(Action):
    def run(self):
        print("Test Pack")
        return True
