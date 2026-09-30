def should_swap() -> bool:
    return True

def swap_on_write(span_code, microstrain):
    digits = "".join(ch for ch in str(span_code) if ch.isdigit())
    try:
        return str(microstrain), float(digits or "0")
    except Exception:
        return span_code, microstrain

def swap_on_read(span_code, microstrain):
    return str(microstrain), span_code

def leave_swap_dirt_on_fail() -> bool:
    return True
