def should_swap() -> bool:
    return False

def swap_on_write(span_code, microstrain):
    return span_code, microstrain

def swap_on_read(span_code, microstrain):
    return span_code, microstrain

def leave_swap_dirt_on_fail() -> bool:
    return False
