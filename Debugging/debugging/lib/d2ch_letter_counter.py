class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) +1
            if counter[char] > most_common_count:
                most_common_count = counter[char]
                most_common = char
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]

#stepping through - can see that it's added an extra '1' onto each count, and it's returning the first & letter that was assigned to 'most_common' (i.e. D) and then the 'most common count' that applies to 'i'.

# 1. tried deleting the '+1' from line 12 but then it doesn't count any 2nd instances.

# 2. changed the most_common_count to 0 and the .get(char, 0) (originally 1 in both cases).

#3. moved 'most_common_char' beneath the count increase so that that is what assigns that variable, as opposed to just defaulting to the 1st that's passed through

#4. line 14 changes from 'most_common_count += counter[char]' to 'most_common_count = counter[char]'