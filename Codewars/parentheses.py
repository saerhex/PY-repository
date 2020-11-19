# def remove_parentheses(s):
#     pattern = r'\([\w\s]*\)'
#     while True:
#         s = re.sub(pattern, r'', s)
#         if not (parentheses := re.findall(pattern, s)):
#             break
#     return s


# tests = ["example(unwanted thing)example",
#         "example (unwanted thing) example",
#         "a (bc d)e",
#         "a(b(c))",
#         "hello example (words(more words) here) something",
#         "(first group) (second group) (third group)"
#         ]
# for test in tests:
#     print(remove_parentheses(test))