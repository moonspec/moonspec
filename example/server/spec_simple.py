# noinspection PyUnresolvedReferences
from moonspec.api import (api, any_of, capture,
                          spec, describe, expect,
                          fact, historic_fact, maybe)


@capture(roles=['demo'])
def capture_foo():
    return 'bar'


@spec(roles=['demo'])
def foo_matches_bar():
    fact('foo').should_be_any_of('baz', 'bar')
    expect(True).to_be_true()
