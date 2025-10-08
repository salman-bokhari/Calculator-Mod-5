import yaml

class CalculatorConfig:
    def __init__(self, path=None):
        """Load configuration from a YAML file if path is provided."""
        self.config = {}
        if path:  # pragma: no cover if path is None
            try:
                with open(path, "r") as f:
                    self.config = yaml.safe_load(f)
            except Exception:  # pragma: no cover if file is valid
                self.config = {}
