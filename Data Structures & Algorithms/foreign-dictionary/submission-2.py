class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        iterate through all words:
        1. compare current word with next word
        - while each letter is the same btwn both words, move on to the next the letter -> find the first letter that differs
        - construct an edge going from letter a to letter b
        """

        dictionary = {c: set() for word in words for c in word}
        for i in range(len(words) - 1):

            word, next_word = words[i], words[i+1]
            char_index = 0
            min_letters = min(len(word), len(next_word))

            while char_index < min_letters and word[char_index] == next_word[char_index]:
                char_index += 1

            if char_index >= len(next_word) and char_index < len(word):
                return ""
            elif char_index < len(word):
                first = word[char_index]
                second = next_word[char_index]
                dictionary[first].add(second)

        visited = {key: False for key in dictionary.keys()}
        recursion_set = set()
        order = []

        # Return true if there is a cycle, false otherwise
        def visit(letter):
            if letter in recursion_set:
                return True

            recursion_set.add(letter)
            
            for next_node in dictionary[letter]:
                if visited[next_node] == False:
                    if visit(next_node) == True:
                        return True

            recursion_set.remove(letter)

            order.append(letter)
            visited[letter] = True
            return False

        for letter in dictionary.keys():
            if visited[letter] == False:
                if visit(letter) == True:
                    return ""

        return "".join(reversed(order))

