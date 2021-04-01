<h1 align="center">동해물가 <img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/271/flag-south-korea_1f1f0-1f1f7.png" srcset="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/271/flag-south-korea_1f1f0-1f1f7.png 2x" alt="Flag: South Korea on Apple iOS 14.2" width="33" height="33"> 농수산물</h1>
<p>
</p>
<p align="center"><img  width=600 src="https://user-images.githubusercontent.com/30452963/113331210-9c169f00-935a-11eb-9ebb-900d1158369c.png" alt="logo" />
<br />
동해물가 농수산물은 농수산물 물가 데이터를 상요하여 가격 변동 추이를 확인하고, 저렴하게 구입 할 수 있도록 도와주는 서비스 입니다.
<br />
<br />
<img src="https://img.shields.io/static/v1?label=SSAFY&message=4%EA%B8%B0&color=ff69b4">
<img src="https://img.shields.io/static/v1?label=Domain&message=Bigdata&color=blueviolet">
</p>


&nbsp;
&nbsp;

****
&nbsp;
&nbsp;

## 목차

* [기획배경](#🍓기획배경)
* [기획](#🍊기획)
  * 와이어프레임
  * UI디자인
  * ERD
* [주요기능](#🍋주요기능)
* [기술스택](#🍏기술스택)
* [개발환경](#🍇개발환경)
  * Git flow 전략
  * 컨벤션
* [서비스구조](#🍑서비스구조)
  * 아키텍쳐
  * 디렉토리 구조
* [시작하기](#🍭시작하기)
* [만든사람들](#🧙‍♂️만든사람들)
  
&nbsp;
&nbsp; 

****
&nbsp;
&nbsp;

# 🍓기획배경

<img src="https://user-images.githubusercontent.com/30452963/113334646-e8fc7480-935e-11eb-9db3-fb64670076ce.png" width=720 />
<img src="https://user-images.githubusercontent.com/30452963/113334679-f1ed4600-935e-11eb-8555-6bfbfa46da64.png" width=720 />

&nbsp;
&nbsp;

# 🍊기획

## 와이어프레임

> [🔗Figma에서 보기](https://www.figma.com/file/hO0uShXzagyy9WQgvnq0e0/Wireframe?node-id=243%3A1)

<img src="https://user-images.githubusercontent.com/30452963/113335504-03831d80-9360-11eb-8d7a-a1ba497755a4.png" width=720 />

&nbsp;

## UI 디자인

> [🔗Figma에서 보기](https://www.figma.com/file/fBnCyMULsrcTRYgCc5NmWt/UI-Design?node-id=2%3A667)


### 메인 페이지

<img src="https://user-images.githubusercontent.com/30452963/113335739-5230b780-9360-11eb-8d0b-a2eedb48311f.png" width=720 />


### 상세 페이지

<img src="https://user-images.githubusercontent.com/30452963/113335802-670d4b00-9360-11eb-9e1c-56385d05c15c.png" width=720 />

&nbsp;

## ERD

> [🔗ERDCloud에서 보기](https://www.erdcloud.com/d/QiA8ksWRJtSpDKDYo)

<img src="https://user-images.githubusercontent.com/30452963/113335987-af2c6d80-9360-11eb-8a91-73ac21b59b0c.png" width=720 />

&nbsp;
&nbsp;

# 🍋주요기능

&nbsp;
&nbsp;

# 🍏기술스택

&nbsp;
&nbsp;

# 🍇개발환경

> [📓git flow 전략](https://www.notion.so/sewonkimm/Git-13372a07ecba456eae0d1ed5637e0861)       
> [📕git 컨벤션](https://www.notion.so/sewonkimm/Git-13372a07ecba456eae0d1ed5637e0861)      
> [📙HTML/CSS 컨벤션](https://www.notion.so/sewonkimm/HTML-CSS-e954f3fba9f947699bb077fa4dd90b8d)      
> [📒JS 컨벤션](https://www.notion.so/sewonkimm/ES6-JS-3c94c15d43a34c5796f676723c8700ff)      
> [📗Spring/Java 컨벤션](https://www.notion.so/sewonkimm/Spring-Java-f5a0d05840c045b48171d79a8fae0a2e)        
> [📘이미지파일 및 폴더명 컨벤션](https://www.notion.so/sewonkimm/452f5f37f624499b9432d2d0e7121b7a)


&nbsp;
&nbsp;

# 🍑서비스구조

### 아키텍쳐

### 디렉토리 구조

```markdown
.
├──📁frontend
├──📁backend
├──📁data
├──📁sql
├──📃.gitignore
├──📃changelog.config.js  // commit convention을 위한 설정
└──📃README.md

```

### 디렉토리 구조 - Frontend

```markdown
📁frontend
```


&nbsp;
&nbsp;


# 🍭시작하기

### DB

```bash
```

### Client

```bash
cd frontend
npm install
npm run serve
```
&nbsp;
&nbsp;

# 🧙‍♂️만든사람들

## SSAFY 4기 서울 2반 A301팀

### 팀명 - 오.합.지.존

다섯명의 지존이 모였다. **五.合.至.尊.**

### 팀원

<table>
  <tr>
    <td align="center">
    <img src="https://secure.gravatar.com/avatar/8d818ca9720e049554b26576590e251e?s=180&d=identicon" width="75px;" alt="이은택"/><br /><sub>서버지존<br/><b>이은택</b></sub><br />
    </td>
    <td>
    💻인프라&BE개발
    <br/>
        <a href="https://lab.ssafy.com/s04-bigdata-sub3/s04p23a301/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&assignee_username=rudus1012" title="Code">📜 Commit Log</a>
        <br/>
    </td>
    <tr>
    <td align="center"><a href="https://github.com/sewonkimm"><img src="https://avatars.githubusercontent.com/u/30452963?v=4" width="75px;" alt="김세원"/><br /><sub>거지존<br/><b>김세원</b></sub></a><br /></td>
    <td>
    🎨UI디자인&FE개발
    <br/>
    <a href="https://lab.ssafy.com/s04-bigdata-sub3/s04p23a301/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&assignee_username=swon962" title="Code">📜 Commit Log</a>
    </td>
    <tr>
    <td align="center"><img src="https://lab.ssafy.com/uploads/-/system/user/avatar/2093/avatar.png?width=90" width="75px;" alt="김지영"/><br /><sub>UI지존<br/><b>김지영</b></sub><br /> </td>
    <td>
    🎨UI디자인&FE개발
    <br/>
    <a href="https://lab.ssafy.com/s04-bigdata-sub3/s04p23a301/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&assignee_username=jiiioiyoung96" title="Code">📜 Commit Log</a>
    </td>
    <tr>
    <td align="center"><img src="https://secure.gravatar.com/avatar/455ee6feb7db33aca75d87bbd37fbf59?s=180&d=identicon" width="75px;" alt="여인구"/><br /><sub>돼지존<br/><b>여인구</b></sub><br /></td>
    <td>
    💻BE개발
    <br/>
     <a href="https://lab.ssafy.com/s04-bigdata-sub3/s04p23a301/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&assignee_username=yeoingu94" title="Code">📜 Commit Log</a>       
    </td>
  </tr>
    <tr>
    <td align="center"><img src="https://secure.gravatar.com/avatar/444729ddcc1195a2e6598a378faa2ac1?s=180&d=identicon" width="75px;" alt="천창민"/><br /><sub>미소지존<br/><b>천창민</b></sub><br /></td>
    <td>
    💻BE개발&데이터분석
    <br/>
     <a href="https://lab.ssafy.com/s04-bigdata-sub3/s04p23a301/merge_requests?scope=all&utf8=%E2%9C%93&state=merged&assignee_username=chunawoos" title="Code">📜 Commit Log</a>       
    </td>
  </tr>
</table>
