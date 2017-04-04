
import matcher
import policy_store


class Enforcer:
    def __init__(self):
        self.rules = policy_store.PolicyStore.init_policy()

    def print_policy(self):
        for rule in self.rules:
            print rule

    def enforce(self, subject, resource, action):
        for rule in self.rules:
            if matcher.NormalMatcher.match(rule.subject, subject) and \
                    matcher.NormalMatcher.match(rule.resource, resource) and \
                    matcher.NormalMatcher.match(rule.action, action):
                return True
        return False

    def test_enforce(self, subject, resource, action):
        res = self.enforce(subject, resource, action)
        print '(%s, %s, %s) -> %s' % (subject, resource, action, res)


enforcer = Enforcer()
enforcer.print_policy()

enforcer.test_enforce('is_admin:True', '', 'os_compute_api:os-used-limits')
