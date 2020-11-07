import requests
from bs4 import BeautifulSoup


URL="https://stackoverflow.com/jobs?q=python&sort=i"

def get_last_page():
  result = requests.get(URL)  

  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div",{"class":"s-pagination"})
  #print(pagination)
  pages = pagination.find_all('a') #모든링크를 찾음
  #print(links)
  # spans = [] #마지막 스팬을 없애줘야함
  # for link in links[:-1] :
  #   spans.append(int(link.find("span").string)) #'2',
    # pages = pages[-2]
    # print(pages)

    # max_page = pages.find("span").string 
  max_page = pages[-2].get_text(strip=True)
  #print(max_page)
  return max_page


def extract_job(html):
  title = html.find("h2",{"class":"mb4"}).find("a")["title"]
  #find('span')["data-ga-label"]
  # print(title)
  company= html.find("h3",{"class":"fc-black-700"}).find("span")
 # print(company)
  
  if company is None :
    company = company.string
  else:
    company = company.get_text(strip=True)
  #print(company)

  location= html.find("h3",{"class":"fc-black-700"}).find("span",{"class":"fc-black-500"}).string.strip()
  #print(location)
  
  link = html["data-jobid"]
  #print(link)
  return {
    "title":title,
    "company":company,
    "location":location,
    "link":f"https://stackoverflow.com/jobs/{link}"
    }

  

def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    #print(f"Scrapping SO: PAGE: {page}")
    #print(page+1) #1부터 끝까지 출력
    result = requests.get(f"{URL}&pg={page+1}")
    #print(result.status_code)
    soup = BeautifulSoup(result.text, 'html.parser') #copy soup
    results = soup.find_all("div",{"class":"-job"})
   # print(results) 리스트
  
  for result in results:
    job = extract_job(result)
    jobs.append(job)
  return jobs

def get_jobs():
  last_page = int(get_last_page())
  jobs = extract_jobs(last_page)
  
  return jobs 




