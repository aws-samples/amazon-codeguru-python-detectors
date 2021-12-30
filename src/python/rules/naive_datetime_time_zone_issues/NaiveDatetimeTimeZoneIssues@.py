# {fact rule=naive-datetime-time-zone-issues@v1.0 defects=1}
def datetime_non_compliant():
    from datetime import datetime, timezone
    # Noncompliant: datetime method does not specify timezone,
    # resulting in time zone related issues.
    return datetime.now()
# {/fact}


# {fact rule=naive-datetime-time-zone-issues@v1.0 defects=0}
def datetime_compliant():
    from datetime import datetime, timezone
    # Compliant: datetime method specifies the time zone,
    # avoiding the time zone related issues.
    return datetime.now(tz=timezone.utc)
# {/fact}
