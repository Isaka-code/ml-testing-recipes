from src.utils.config import Config


def test_config_values():
    cfg = Config.load("config.yaml")
    assert cfg.learning_rate == 0.01, "learning_rateが想定値と違います"
