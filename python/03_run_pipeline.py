import logging
from pathlib import Path

from importlib.util import spec_from_file_location
from importlib.util import module_from_spec


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def load_module(file_name, module_name):

    file_path = Path(__file__).parent / file_name

    spec = spec_from_file_location(
        module_name,
        file_path
    )

    module = module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


def run_pipeline():

    print("=" * 60)
    print("PYTHON DATA PROCESSING PIPELINE")
    print("=" * 60)

    logger.info("Pipeline started.")

    try:

        logger.info(
            "Starting customer processing."
        )

        customer_module = load_module(
            "01_process_customers.py",
            "customer_processor"
        )

        customer_module.process_customers()

        logger.info(
            "Customer processing completed."
        )


        logger.info(
            "Starting transaction processing."
        )

        transaction_module = load_module(
            "02_process_transactions.py",
            "transaction_processor"
        )

        transaction_module.process_transactions()

        logger.info(
            "Transaction processing completed."
        )


        logger.info(
            "Pipeline completed successfully."
        )

        print("\nPipeline completed successfully.")

    except Exception as error:

        logger.exception(
            "Pipeline failed: %s",
            error
        )

        print(
            f"\nPipeline failed: {error}"
        )


if __name__ == "__main__":
    run_pipeline()
