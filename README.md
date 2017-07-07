# pass-words

Generate a random password from /usr/share/dict/words
I make no claims about the password strength or suitability

A friend does almost the same thing with:

>  words=($(</usr/share/dict/words grep -v '^[A-Z]' | shuf | head -n2)); printf "%s%s%00d" ${words[0]^} ${words[1]^} $((1 + RANDOM % 99))

