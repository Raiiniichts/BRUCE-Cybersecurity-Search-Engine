from google import google
import csv
import re
import time
import random

#write =  open('new.csv', "w", newline='\n')
#spamwriter = csv.writer(write, delimiter=' ')
csvv = open('test3.csv','w')
  
search_key = ['Cybersecurity Course Syllabus',
              'Computer Security Course Syllabus',
              'Network Security Course Syllabus',
              'Information Security Course Syllabus',
              'Cybersecurity Law Course Syllabus']

#random_time = [41,35,13,20,45,30,30,40,32,38,44,18,47,19,28,26,22,32,34,17]
with open('domains2.csv', 'r') as csvfile:
    num_page = 1
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        row = str(row[0]) 
        row = row.replace("https://www.","site:")
        row = row.replace("http://www.","site:")
        row = row.replace('/','')
        for key in search_key:
            add = []
            print(row+' '+ key)
            search_results = google.search(row+' '+ key,num_page)
            print(search_results)
            for res in search_results:
                
                i = str(res.link)
                print(res.description)
                
                while '&sa' in i:
                    a = i.find('&sa')
                    i = i[:a]
                

                if '.edu' not in i:
                    continue
                if i in add:
                    continue
                csvv.write(str(i))
                csvv.write('\n')
                print(i)
            #break
        
                
            
        
            '''
            timenow = random.randrange(15,30)
            print(timenow)
            time.sleep(timenow)
            '''
        #break
        
csvv.close()

