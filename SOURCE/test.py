from urllib.parse import quote_plus 
from bs4 import BeautifulSoup 
from selenium import webdriver 
search = input("검색어를 입력하세요 : ") 
url = 'https://www.google.com/search?q=' 
newUrl = url + quote_plus(search) 
driver = webdriver.Chrome() 
driver.get(newUrl) 
html = driver.page_source #열린 페이지 소스 받음 
soup = BeautifulSoup(html) 
r = soup.select('.r') #클래스 r을 선택 select 로 가져오면 list 형식임 
for i in r : 
    print(i.select_one('.LC20lb.DKV0Md').text) #select 를 안쓰는 이유는 select 를 쓰면 list 로 불러와져서 text 를쓸 수 없다 
    print(i.a.attrs['href']) #a 태그의 href 속성 가져오기 print()
