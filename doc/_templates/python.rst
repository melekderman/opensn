{{ fullname }}
{{ underline }}

.. currentmodule:: {{ module }}

{%+ if objtype == 'class' -%}
.. autoclass:: {{ objname }}
   :special-members: __init__
   :members:
   :inherited-members:
{% endif %}

{%- if objtype == 'function' -%}
.. autofunction:: {{ objname }}
{% endif %}
