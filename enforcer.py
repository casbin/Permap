
import json


class Rule:
    def __init__(self, subject, resource, action):
        self.subject = subject
        self.resource = resource
        self.action = action

    def __str__(self):
        return '%s, %s, %s' % (self.subject, self.resource, self.action)


class NormalMatcher:
    def __init__(self):
        pass

    @staticmethod
    def match(policy_object, access_object):
        if policy_object == '':
            return True
        return policy_object == access_object


rules = []


def init_policy():
    f = open('J:/github_repos/patron_rest/etc/patron/policy.json')
    json_rules = json.load(f)
    for key in json_rules:
        value =json_rules[key]

        if value == '':
            value = 'rule:default'

        while value.startswith('rule:'):
            value = json_rules[value[5:]]

        values = value.split(' or ')
        for v in values:
            rules.append(Rule(v, '', key))


def print_policy():
    for rule in rules:
        print rule


def enforce(subject, resource, action):
    for rule in rules:
        if NormalMatcher.match(rule.subject, subject) and \
                NormalMatcher.match(rule.resource, resource) and \
                NormalMatcher.match(rule.action, action):
            return True


def test_enforce(subject, resource, action):
    res = enforce(subject, resource, action)
    print '(%s, %s, %s) -> %s' % (subject, resource, action, res)


init_policy()
print_policy()

test_enforce('is_admin:True', '', 'os_compute_api:os-used-limits')
