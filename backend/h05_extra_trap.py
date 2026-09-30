from span_strain_swap import leave_swap_dirt_on_fail, should_swap, swap_on_read, swap_on_write

def prepare_insert(span_code, microstrain):
    if should_swap():
        return swap_on_write(span_code, microstrain)
    return span_code, microstrain

def prepare_row(span_code, microstrain):
    if should_swap():
        return swap_on_read(span_code, microstrain)
    return span_code, microstrain

def dirt() -> bool:
    return leave_swap_dirt_on_fail()
