class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # a substring should have all occurences of 'b' for example
        # consecutive characters by default for substring

        # "xyxxyzbzbbisl" -> ["xyxxy", "zbzbb", "i", "s", "l"] 
        # because 'b' is spread and 'z' comes in between, so 
        # partition only where both chars start and end

        # Last occurrence of each character
        last_position = {}

        for i, char in enumerate(s):
            last_position[char] = i

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            # Current partition must include the last occurrence
            # of every character seen inside it
            end = max(end, last_position[char])

            # All characters in this partition end here
            if i == end:
                partition_length = end - start + 1
                result.append(partition_length)

                start = i + 1

        return result


