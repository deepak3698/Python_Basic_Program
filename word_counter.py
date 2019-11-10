

string1=input("Please Write your Sentence :")

String_without_extra_spaces=""
word_counter=1
if(string1[0]==" "):
    word_counter = 0
try:
    for index,value in enumerate(string1):
        if not(string1[index]==" " and string1[index+1]==" "):
            String_without_extra_spaces=String_without_extra_spaces+value
            if (value == " "):
                word_counter=word_counter+1
except:
    pass


print(f"Your Sentence without spaces is :{String_without_extra_spaces}")
print(f"you have {word_counter} Words in your Sentence.")