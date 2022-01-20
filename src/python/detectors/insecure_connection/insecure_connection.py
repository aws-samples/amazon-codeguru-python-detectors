#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=insecure-connection@v1.0 defects=1}
def ftp_connection_noncompliant():
    import ftplib
    # Noncompliant: insecure ftp used.
    cnx = ftplib.FTP("ftp://anonymous@example.com")
# {/fact}


# {fact rule=insecure-connection@v1.0 defects=0}
def ftp_connection_compliant():
    import ftplib
    # Compliant: secure ftp_tls used.
    cnx = ftplib.FTP_TLS("ftp.example.com")
# {/fact}
