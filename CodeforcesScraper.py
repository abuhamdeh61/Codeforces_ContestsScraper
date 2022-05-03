from bs4 import BeautifulSoup
import requests
from csv import writer
with open('problem set.csv', 'w') as f:
    thewriter=writer(f)
    
    #define the rows for the CSV file
    header=['contest name','problem link','problem name','accepted submissions']
   
    thewriter.writerow(header)
    
    #cycling through the contests URLs
    for i in range(1, 1675):
      
        #get requset to acquire the html code
        htmlPage = requests.get("https://codeforces.com/contest/"+str(i)+"?locale=en")
        
        #transform the html code to a scrapable code
        soup = BeautifulSoup(htmlPage.text, 'lxml')
        
        #get the contest name
        contest = soup.find('th', {'class': 'left'})
        
        #check if the URL is reachable
        if contest !=None:
          
            #for example i only want to scrap div. 2 contests you can change it for sure (Div. 1,Div. 2,Div. 3,ACM,ICPC)
            if "Div. 2" in contest.text:
              
                for x in soup.find('table', {'class': 'problems'}).find_all('tr')[1:]:
                    problemDifficulty = x.find('td').text.split()[0]
                    problemLink="https://codeforces.com/contest/"+str(i)+"/problem/"+problemDifficulty
                    solutionsCount = x.find_all('a')[-1].text.replace("x", "")
                    problemName = x.find_all('td')[1].find('a').text
                    problem=problemDifficulty+". "+problemName
                    
                    #Arrange the data to fit the CSV file
                    data=[contest.text,problemLink, problem, solutionsCount]
                   
                    thewriter.writerow(data)
print("Done")
