#Naming the sentence with a variable called sentence 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence) #printing the sentence 

#Using the replace()  function to replace the ! to a blank space
replace_sentence = sentence.replace("!", " ")
print(replace_sentence)

#Using the upper() funtion to write the whole sentence in capital letters
upper_sentence = replace_sentence.upper()
print(upper_sentence)

#Using the slicers to write the sentence in reverse
reverse_sentence = replace_sentence[::-1]
print(reverse_sentence)
