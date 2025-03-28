# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        

        deck.sort()
        n = len(deck)
        res = [0] * n
        indices = deque(range(n))
        
        for card in deck:
            idx = indices.popleft()
            res[idx] = card
            if indices:
                indices.append(indices.popleft())
        
        return res