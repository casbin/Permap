
class Rule:
    def __init__(self, subject, resource, action):
        self.subject = subject
        self.resource = resource
        self.action = action

    def __str__(self):
        return '%s, %s, %s' % (self.subject, self.resource, self.action)
