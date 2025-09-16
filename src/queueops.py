from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if not queue:
        return None, []
    return queue[0], queue[1:]


def move_to_back(queue: List[str], name: str) -> List[str]:
    if name not in queue:
        return queue.copy()
    idx = queue.index(name)
    return queue[:idx] + queue[idx+1:] + [queue[idx]]


def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    for i in range(max(len(q1), len(q2))):
        if i < len(q1):
            result.append(q1[i])
        if i < len(q2):
            result.append(q2[i])
    return result
