# noinspection PyUnresolvedReferences
from moonspec.api import (api, any_of, capture,
                          spec, describe, expect,
                          fact, historic_fact, maybe,
                          apply_to_roles)

apply_to_roles('demo')


@capture(roles=['extra_role_a'])
def capture_foo():
    return 'bar'


@spec(roles=['extra_role_b'])
def foo_matches_bar():
    fact('foo').should_be_any_of('baz', 'bar')
    expect(True).to_be_true()
