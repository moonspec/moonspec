Quickstart
==========

TODO

.. code-block:: python
    :caption: spec_hostname.py
    :name: minimal-spec

    from moonspec.api import (api, any_of, capture,
                              spec, describe, expect,
                              fact, historic_fact, maybe,
                              apply_to_roles)

    apply_to_roles('server')

    @capture(roles=['extra_role_a'])
    def capture_hostname():
        return api.host.name()


    @spec(roles=['extra_role_b'])
    def it_has_expected_hostname():
        fact('hostname').should_equal('some_hostname')



