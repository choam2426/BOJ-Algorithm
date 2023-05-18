number=list(map(str, input()))
sec=0

for i in number:
    if ord(i) < 68:
        sec+=3
    elif 67<ord(i)<71:
        sec+=4
    elif 70<ord(i)<74:
        sec+=5
    elif 73<ord(i)<77:
        sec+=6
    elif 76<ord(i)<80:
        sec+=7
    elif 79<ord(i)<84:
        sec+=8
    elif 83<ord(i)<87:
        sec+=9
    elif 86<ord(i)<91:
        sec+=10
print(sec)