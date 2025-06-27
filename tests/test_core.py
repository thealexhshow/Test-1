from autobot.core import ask
def test_ask_returns_string(monkeypatch):
    # Monkey-patch the actual call so tests don't hit the network
    monkeypatch.setattr("autobot.core.client.chat.completions.create",
        lambda *_, **__: type("X", (), {"choices":[type("Y", (), {"message":type("Z", (), {"content":"hi"})()})()]})()
    )
    assert ask("hello") == "hi"
