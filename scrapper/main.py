from indeed import get_jobs as get_indeed_jobs
from stackoverflow import *
from save import *

so_jobs = get_jobs()
#print(so_jobs)
indeed_jobs = get_indeed_jobs()
#print(indeed_jobs)
jobs = so_jobs + indeed_jobs
print(jobs)

save_to_file(jobs) #파일생성할때 jobs 변수는 잠시 뺌 

#CSV파일 만들기
#CommaSeperatedValue








# last_indeed_page = extract_indeed_pages()
# print(last_indeed_page) #10출력

# indeed_jobs = extract_indeed_jobs(last_indeed_page)

# print(indeed_jobs)





# print(max_page)
# # 페이지가 50개씩이라면 2페이지[인덱스 넘버로는 1 *50 + 1페이지의 50] = 51~100까지의 리스트가 나올테니까


# print(range(max_page)) #range(0,10)

# for n in range(max_page):
#   print(f"start={n*50}") # 0 1 2 3 4 5 6 7 8 9 까지 출력! 
#   #50개씩 곱해줌 
















#컴퍼니 추출하기

