#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

import logging
logger = logging.getLogger(__name__)


# {fact rule=log-injection@v1.0 defects=1}
def logging_noncompliant():
    filename = input("Enter a filename: ")
    # Noncompliant: unsanitized input is logged.
    logger.info("Processing %s", filename)
# {/fact}


# {fact rule=log-injection@v1.0 defects=0}
def logging_compliant():
    filename = input("Enter a filename: ")
    if filename.isalnum():
        # Compliant: input is validated before logging.
        logger.info("Processing %s", filename)
# {/fact}
