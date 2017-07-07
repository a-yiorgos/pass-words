# Generate a random password from /usr/share/dict/words
# I make no claims about the password strength or suitability
#
# A friend does almost the same thing with:
#
# words=($(</usr/share/dict/words grep -v '^[A-Z]' | shuf | head -n2)); printf "%s%s%00d" ${words[0]^} ${words[1]^} $((1 + RANDOM % 99))

import random
import string

words = tuple(open("/usr/share/dict/words", "r"))

l = len(words) - 1
w1 = words[random.randint(0, l)].rstrip()
w2 = words[random.randint(0, l)].rstrip()
pw = list(w1 + random.choice(string.punctuation) + w2)
print "".join(pw)

l = len(pw) - 1
pw[random.randint(0, l)] = random.choice(string.ascii_uppercase)
pw[random.randint(0, l)] = random.choice(string.ascii_uppercase)
pw[random.randint(0, l)] = random.choice(string.digits)
pw[random.randint(0, l)] = random.choice(string.digits)
pw[random.randint(0, l)] = random.choice(string.punctuation)

print "".join(pw)
