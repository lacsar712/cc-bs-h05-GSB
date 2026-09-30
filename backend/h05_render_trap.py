SWAP_LIST = True
SWAP_CARD = True
SWAP_QUEUE = True
SWAP_DETAIL = True

def swap_pair(span_code, microstrain):
    return microstrain, span_code

def list_cells(span_code, microstrain):
    return swap_pair(span_code, microstrain) if SWAP_LIST else (span_code, microstrain)

def all_swapped(span_code, microstrain):
    return list_cells(span_code, microstrain)
