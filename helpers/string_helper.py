class StringHelper():

    """
    Returns a list with tags from a given text #tag1 #tag2 etc.
    """
    @staticmethod
    def parse_tags_from_text(text, logger):
        result = []

        # Remove all unnecessary characters
        text = text.replace(',', '').replace(
            '.', '').replace('\r\n', '').replace(' ', '')

        # We assume that a tag is beginning with #
        result = text.split('#')

        # Remove all empty entries from the list, see: https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
        result = list(filter(None, result))

        return result

    @staticmethod
    def replace_first_occurrence(to_replace, replace_with, elements):
        # See: https://stackoverflow.com/questions/6005891/replace-first-occurrence-only-of-a-string/28607089
        result = []
        for element in elements:
            element = element.replace(to_replace, replace_with, 1)
            result.append(element)
        return result
