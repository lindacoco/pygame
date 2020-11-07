import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL=f"https://ca.indeed.com/jobs?q=web+developer&l=Vancouver%2C+BC&limit={LIMIT}" #{LIMIT} is not working, why? 'f'

def get_last_page():
  indeed_result = requests.get(URL)

  # print(indeed_result.text) #<Response [200] 출력 

  indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

  # print(indeed_soup)

  pagination = indeed_soup.find("div",{"class":"pagination"})

  # print(pagination)

  links = pagination.find_all('a') #모든링크를 찾음

  # print(pages) #list

  spans = [] #마지막 스팬을 없애줘야함
  for link in links[:-1] :
    spans.append(int(link.find("span").string)) #'2','3'...'10'
  #(print(spans))   #page.string 도 똑같은결과가 된다..! 스프가해줌

  #마지막것만 빼주기
  #print(spans[:-1]) 
  # spans = spans[:-1] 인티저 변환할때 마지막때문에 인식안됨 위에서 지정해줌
  #print(spans)
  #페이지 마지막 숫자를 변수에 넣어준다.
  max_page = spans[-1] 
  return max_page


def extract_job(html):
  title = html.find("h2",{"class":"title"}).find("a")["title"]
  #print(title)
  #이제 회사이름  링크ㅏ 있는 것도 있고 없는 것도 있음 none이 나오는 이유
  company = html.find("span",{"class":"company"})
  if company :
    company_anchor = company.find("a")
    if company_anchor is not None:
      company = str(company_anchor.string)
    else:
      company = str(company.string)
    company = company.strip() #여기에 "F"넣으면 F문자를 다 없애줌 
  else:
     company =None

  location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
  
  job_id = html["data-jk"] #지원링크,
  return {
    "title":title,
    "company":company,
    "location":location,
    'link':f"https://ca.indeed.com/viewjob?jk={job_id}"
    }

def extract_jobs(last_page):
  
  jobs = []
  for page in range(last_page):
    #print(f"Scrapping indeed: PAGE: {page}")
    #print(f"Scrpping page {page}")
    #print(f"&start={page*LIMIT}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    #print(result) #<Response [200] 
    # print(result.status_code) # 200 means it is working
    soup = BeautifulSoup(result.text, 'html.parser') #copy soup
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
   # print(results) 리스트
  
  for result in results:
    # title = result.find("h2",{"class":"title"})
    # #print(title)
    # anchor = (title.find("a")["title"])
    # print(anchor)
    job = extract_job(result)
    # print(job) 중요한건 jobs[]에 넣어주는 것
    jobs.append(job)
  return jobs 

def get_jobs():
    last_page = get_last_page()
    print(last_page) #10출력
    jobs = extract_jobs(last_page)
    return jobs