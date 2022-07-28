import logging
from argparse import ArgumentParser
from bot import handlers

from telegram.ext import (
    Application,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('--token', type=str, required=True)
    return parser.parse_args()


def main() -> None:
    application = Application.builder().token(parse_arguments().token).build()
    handlers.setup_handlers(application)
    application.run_polling()


if __name__ == "__main__":
    main()
