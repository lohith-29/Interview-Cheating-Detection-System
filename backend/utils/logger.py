from datetime import datetime


LOG_FILE = "violations.log"


def log_violation(
    candidate_id,
    violation_type
):

    with open(
        LOG_FILE,
        "a"
    ) as file:

        file.write(
            f"{datetime.now()} | "
            f"{candidate_id} | "
            f"{violation_type}\n"
        )