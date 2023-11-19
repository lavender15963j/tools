{% set data=read('t.txt').split('\n') %}
{%- for d in data|batch(2) -%}
{%- set ds="'" + d|join("','") + "'" -%}
------------------- START -------------------

select * from abc where v in ({{ ds }});

-------------------- END --------------------
{% endfor %}