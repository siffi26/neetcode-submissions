import heapq
from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Every card must belong to a complete group
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        # Heap contains each unique card value
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # Smallest remaining card must begin the next group
            first = min_heap[0]

            for card in range(first, first + groupSize):
                # Required consecutive card is missing
                if count[card] == 0:
                    return False

                count[card] -= 1

                # Remove cards whose frequency has become zero
                if count[card] == 0:
                    # It must be the smallest remaining card
                    if card != min_heap[0]:
                        return False

                    heapq.heappop(min_heap)

        return True


        