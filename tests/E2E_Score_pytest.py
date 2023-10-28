import pytest
from e2e import is_service_available

@pytest.mark.parametrize("score_server_url", ["http://127.0.0.1:30000/"])
def test_score_service(score_server_url):
    value = is_service_available(score_server_url+'/score')
    assert value


