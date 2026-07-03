class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """


        if not tokens:
            return 0

        # sort the tokens to play face-up first
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0


        # find the smallest
        while left <= right:
            # do the face-up first
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score) # update max_score


            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1

            else:
                break
        
        return max_score