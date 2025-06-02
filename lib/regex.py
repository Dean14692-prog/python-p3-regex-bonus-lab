import re

pattern = re.compile(
    r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
)

class MyRegex:
    @staticmethod
    def fullmatch(s):
        return pattern.fullmatch(s)
    
    @staticmethod
    def findall(text):
        return pattern.findall(text)

my_regex = MyRegex
