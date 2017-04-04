
import json

from rule import *


class PolicyStore:
    def __init__(self):
        pass

    @staticmethod
    def init_policy():
        rules = []

        f = open('J:/github_repos/patron_rest/etc/patron/policy.json')
        json_rules = json.load(f)
        for key in json_rules:
            value = json_rules[key]

            if value == '':
                value = 'rule:default'

            while value.startswith('rule:'):
                value = json_rules[value[5:]]

            values = value.split(' or ')
            for v in values:
                rules.append(Rule(v, '', key))

        return rules
