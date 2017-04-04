
class NormalMatcher:
    def __init__(self):
        pass

    @staticmethod
    def match(policy_object, access_object):
        if policy_object == '':
            return True
        return policy_object == access_object
