from collections import Counter

S = input()
T = input()

ans ="No"

# Count character occurrences
S_counter = dict(Counter(S))
T_counter = dict(Counter(T))

# Special characters
special_chars = ['a', 't', 'c', 'o', 'd', 'e', 'r']

# For each special character, if its count is less in S, decrease the count of '@' in S and increase the count of the character
for char in special_chars:
    if S_counter.get(char, 0) < T_counter.get(char, 0):
        difference = T_counter.get(char, 0) - S_counter.get(char, 0)
        S_counter['@'] = S_counter.get('@', 0) - difference
        S_counter[char] = S_counter.get(char, 0) + difference

# For each special character, if its count is less in T, decrease the count of '@' in T and increase the count of the character
for char in special_chars:
    if T_counter.get(char, 0) < S_counter.get(char, 0):
        difference = S_counter.get(char, 0) - T_counter.get(char, 0)
        T_counter['@'] = T_counter.get('@', 0) - difference
        T_counter[char] = T_counter.get(char, 0) + difference

if S_counter.get('@', 0) >= 0 and T_counter.get('@', 0) >= 0:
  if '＠' not in S_counter:
    S_counter['@'] = 0
  if '＠' not in T_counter:
    T_counter['@'] = 0
  if S_counter == T_counter:
    ans = "Yes"

print(ans)