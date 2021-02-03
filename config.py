import yaml

from pathlib import Path


def load_config_as_dict(config_filename):
    config = yaml.safe_load(open(Path(__file__).absolute().parent.joinpath(config_filename)))
    return config


class LeftFrameConfig:
    _config = load_config_as_dict("config/general.yaml")["left_frame"]

    username = _config["username"]
    source = _config["source"]
    author = _config["author"]
    categories = _config["categories"]
    licence = _config["licence"]
