# -*- coding: utf-8 -*-
import pytest
import requests


def test_hello_world(h2o):
    res = requests.get('http://localhost:8080/mruby/')
    assert res.status_code == 200
    assert res.headers['X-App-Auth'] == 'test'


@pytest.mark.parametrize('key, val', [
    ('user_id', '1'),
    ('item_id', '10'),
])
def test_query_string(h2o, key, val):
    res = requests.get('http://localhost:8080/qs/?{}={}'.format(key, val))
    assert res.status_code == 200
    assert res.content == '{}={}'.format(key, val)
