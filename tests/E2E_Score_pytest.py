import pytest
from e2e import is_service_available,validate_user_score_with_limits

@pytest.mark.parametrize("score_server_url", ["http://127.0.0.1:30000/"])
def test_score_service(score_server_url):
    value = is_service_available(score_server_url)
    assert value



@pytest.mark.parametrize("score_server_url", ["http://127.0.0.1:30000/"])
@pytest.mark.parametrize("user_name", ["kkkkkkkk"])
@pytest.mark.parametrize("low_limit", [1])
@pytest.mark.parametrize("high_limit", [1000])
def test_validate_user_score_with_limits(score_server_url,user_name,low_limit,high_limit):
    value = validate_user_score_with_limits(application_url=score_server_url,user_name=user_name,low_limit=low_limit,high_limit=high_limit)
    assert value
