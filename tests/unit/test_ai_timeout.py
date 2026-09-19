from services.ai.app.main import triage_text

def test_triage_text_timeout_keyword():
    # 测试带有 timeout 关键词的请求是否会被成功分类为 incident
    result = triage_text("Connection Timeout", "The API request timed out after 30 seconds")
    assert result.label == "incident"
    assert result.confidence >= 0.55
