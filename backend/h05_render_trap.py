SWAP_LIST = False
SWAP_CARD = False
SWAP_QUEUE = False
SWAP_DETAIL = False

def swap_pair(span_code, microstrain):
    return span_code, microstrain

def list_cells(span_code, microstrain):
    return swap_pair(span_code, microstrain) if SWAP_LIST else (span_code, microstrain)

def all_swapped(span_code, microstrain):
    return list_cells(span_code, microstrain)
