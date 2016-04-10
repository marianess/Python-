#Create a function that counts all the words from Text1 and Text2
#	def word_counter(text):
#		....
#		....
#Output:	
#>>> Text1 has ***** words, **** row and **** empty rows


#COUNTNG TOTAL LINES IN TEXT
def line_counter(text):
        empty_line_count = 0
        my_file = open(text, "r")

        for line in my_file:
                empty_line_count += 1
        return (empty_line_count)

#COUNTING EMPTY LINES IN TEXT
def empty_line_counter(text):
        empty_line_count = 0
        my_file = open(text, "r")

        for line in my_file:
                if line.split():
                        empty_line_count += 1 #pean lugema tyhja rida

        return empty_line_count
#ma pean arvestama sellega, et word loeb tyhja rida ag python mitte!

#COUNTING TOTAL WORDS IN TEXT
def word_counter(text):
        total_lines = 0 #v6tab fail rea kaupa
        total_word_counter = 0
        read_file = open(text, "r")
        
        while total_lines <= line_counter(text):
                rida = read_file.readline().split()
                sona_in_rida = len(rida) #loeab s6nu reas
                print (rida)
                print (sona_in_rida)
                total_word_counter += sona_in_rida #sumeerid s6nu
                #print total_word_counter
                total_lines += 1 #loeab ridasid
        read_file.close()
        return total_word_counter


print ('total number of words: ', word_counter("1.txt"))
print ('total number of rows: ' , line_counter("1.txt"))
print ('total number of empty rows: ', empty_line_counter("1.txt"))



