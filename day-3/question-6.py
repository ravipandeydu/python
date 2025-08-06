from collections import Counter
import re


class TextAnalyzer:
    """
    A tool for comprehensive text analysis using Counter for statistics.
    """

    def __init__(self, text):
        """
        Initializes with text to analyze.

        Args:
            text (str): Text to analyze.
        """
        self.original_text = text
        # For case-insensitive analysis
        self.text_lower = text.lower()
        # Pre-compile regex for word tokenization for efficiency
        self.word_pattern = re.compile(r"\b\w+\b")

    def get_character_frequency(self, include_spaces=False):
        """
        Gets frequency of each character.

        Args:
            include_spaces (bool): Whether to include spaces in count.

        Returns:
            Counter: Character frequencies.
        """
        text_to_analyze = self.original_text
        if not include_spaces:
            text_to_analyze = text_to_analyze.replace(" ", "")
        return Counter(text_to_analyze)

    def get_word_frequency(self, min_length=1):
        """
        Gets frequency of each word.

        Args:
            min_length (int): Minimum word length to include.

        Returns:
            Counter: Word frequencies.
        """
        words = self.word_pattern.findall(self.text_lower)
        filtered_words = [word for word in words if len(word) >= min_length]
        return Counter(filtered_words)

    def get_sentence_length_distribution(self):
        """
        Analyzes sentence lengths (in words).

        Returns:
            dict: Contains 'distribution' (Counter), 'average', 'longest', 'shortest'.
        """
        # Split by sentence-ending punctuation, filtering out empty strings
        sentences = [
            s.strip() for s in re.split(r"[.!?]+", self.original_text) if s.strip()
        ]
        if not sentences:
            return {
                "distribution": Counter(),
                "average": 0,
                "longest": 0,
                "shortest": 0,
            }

        sentence_word_counts = [len(self.word_pattern.findall(s)) for s in sentences]

        return {
            "distribution": Counter(sentence_word_counts),
            "average": sum(sentence_word_counts) / len(sentence_word_counts),
            "longest": max(sentence_word_counts),
            "shortest": min(sentence_word_counts),
        }

    def find_common_words(self, n=10, exclude_common=True):
        """
        Finds most common words, optionally excluding common English words.

        Args:
            n (int): Number of words to return.
            exclude_common (bool): Exclude common words like 'the', 'and', etc.

        Returns:
            list: List of tuples (word, count).
        """
        common_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "for",
            "of",
            "with",
            "by",
            "is",
            "are",
            "was",
            "were",
            "be",
            "been",
            "being",
            "have",
            "has",
            "had",
            "do",
            "does",
            "did",
            "will",
            "would",
            "could",
            "should",
            "may",
            "might",
            "can",
            "i",
            "this",
            "that",
            "these",
            "those",
            "it",
            "you",
            "he",
            "she",
            "we",
            "they",
            "me",
            "him",
            "her",
            "us",
            "them",
        }

        word_counts = self.get_word_frequency()

        if exclude_common:
            for word in common_words:
                del word_counts[word]

        return word_counts.most_common(n)

    def get_reading_statistics(self):
        """
        Gets comprehensive reading statistics.

        Returns:
            dict: Contains character_count, word_count, sentence_count,
                  average_word_length, reading_time_minutes (assume 200 WPM).
        """
        char_count = len(self.original_text)
        words = self.word_pattern.findall(self.text_lower)
        word_count = len(words)
        sentences = [s for s in re.split(r"[.!?]+", self.original_text) if s.strip()]
        sentence_count = len(sentences)

        if word_count == 0:
            return {
                "character_count": char_count,
                "word_count": 0,
                "sentence_count": sentence_count,
                "average_word_length": 0,
                "reading_time_minutes": 0,
            }

        avg_word_len = sum(len(word) for word in words) / word_count
        reading_time = word_count / 200  # Assuming 200 Words Per Minute

        return {
            "character_count": char_count,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "average_word_length": avg_word_len,
            "reading_time_minutes": reading_time,
        }

    def compare_with_text(self, other_text):
        """
        Compares this text with another text.

        Args:
            other_text (str): Another text to compare with.

        Returns:
            dict: Contains 'common_words', 'similarity_score',
                  'unique_to_first', 'unique_to_second'.
        """
        analyzer1_words = set(self.get_word_frequency().keys())

        analyzer2 = TextAnalyzer(other_text)
        analyzer2_words = set(analyzer2.get_word_frequency().keys())

        common_words = analyzer1_words.intersection(analyzer2_words)
        union_words = analyzer1_words.union(analyzer2_words)

        # Jaccard Similarity
        similarity = len(common_words) / len(union_words) if union_words else 0

        return {
            "common_words": common_words,
            "similarity_score": similarity,
            "unique_to_first": analyzer1_words - analyzer2_words,
            "unique_to_second": analyzer2_words - analyzer1_words,
        }


# --- Test your implementation ---
sample_text = """
Python is a high-level, interpreted programming language with dynamic semantics. 
Its high-level built-in data structures, combined with dynamic typing and dynamic binding, 
make it very attractive for Rapid Application Development. Python's simple, easy to learn 
syntax emphasizes readability and therefore reduces the cost of program maintenance. 
Python supports modules and packages, which encourages program modularity and code reuse. 
The Python interpreter and the extensive standard library are available in source or binary 
form without charge for all major platforms, and can be freely distributed.
"""

analyzer = TextAnalyzer(sample_text)

# Test all methods
print("Character Frequency (top 5):", analyzer.get_character_frequency().most_common(5))
print(
    "Word Frequency (top 5):", analyzer.get_word_frequency(min_length=4).most_common(5)
)
print("Common Words:", analyzer.find_common_words(5))
print("Reading Statistics:", analyzer.get_reading_statistics())

# Compare with another text
other_text = (
    "Java is a programming language. Java is object-oriented and platform independent."
)
comparison = analyzer.compare_with_text(other_text)
print("Comparison results:", comparison)
