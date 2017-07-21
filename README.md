# Scrapy

[https://scrapy.org/](https://scrapy.org/)


### 1. start scrapy project

```
$ scrapy startproject rt_crawler
```

### 2. scrapy shell


##### start shell

```
$ scrapy shell 'https://www.rottentomatoes.com/top/bestofrt/?year=2015'
```

##### test xpath
```
In [1] : response.xpath('//*[@id="top_movies_main"]/div/table/tr[1]/td[3]/a/@href')
```

### 3. Project Structure

##### Spider
- 어떤 웹 사이트들을 어떻게 크롤링할것인지 명시
- 각 웹페이지의 어떤 부분을 스크래핑할 것인지 명시

##### Selector
- 웹페이지 상의 특정 HTML요소를 간편하게 선택할 수 있도록 하는 메커니즘을 구현한 클래스
- CSS 선택자를 직접 사용하거나, XPath 사용 가능

##### Item
- 웹페이지에서 원하는 부분을 스크랩하여 저장할 때 사용하는 사용자 정의 자료구조 클래스

##### Item Pipeline
- 스크래핑 결과물을 Item 형태로 구성하였을 때, 이를 자유롭게 가공하거나 다양한 형태로 저장할수 있도록 하는 클래스

##### Settings
- Spider나 Item Pipeline 등이 어떻게 동작하도록 할 지에 대한 세부적인 설정 사항을 기재하는 파일
- cf.robots.txt

### 4. run scrapy

```
rt_crawler$ scrapy crawl RottenTomatoes
```