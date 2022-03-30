#Write a program to read through the mbox-short.txt and figure out 
#who has sent the greatest number of mail messages. The program looks
# for 'From ' lines and takes the second word of those lines as the
# person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find the most
# prolific committer

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
wordcount = 0

for line in handle:
    if line.startswith("From:") : continue
    if not line.startswith("From"):
        continue
    words = line.split()
    
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(words[1] , counts[words[1]])
#max_count = None
#max_word = None
#for word,count in counts.items():
   # if max_count is None or count > max_count:
     #   max_count = count
     #   max_word = word
#print(max_word, max_count)




