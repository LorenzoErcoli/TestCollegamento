import logging
import sys

LOGGER = logging.getLogger(__name__)


def configure_logging():
    """Configure logging to emit simple messages to stdout."""
    LOGGER.setLevel(logging.INFO)
    LOGGER.propagate = False

    if not LOGGER.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter("%(message)s"))
        LOGGER.addHandler(handler)


def main():
    configure_logging()
    LOGGER.info("CIAO GABRIELE")


if __name__ == "__main__":
    main()
