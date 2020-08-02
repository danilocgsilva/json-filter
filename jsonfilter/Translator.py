class Translator:

    def __init__(self):
        self.humanterm = None

    def set_humanterm(self, humanterm: str):
        self.humanterm = humanterm
        return self

    def translate(self):

        terms = self.humanterm.split(".")

        translated_term = ""
        for term in terms:
            translated_term += '[' + self.string_or_number(term) + ']'

        return translated_term

    def string_or_number(self, term: str) -> str:
        try:
            return str(int(term))
        except Exception:
            return '"' + term + '"'


