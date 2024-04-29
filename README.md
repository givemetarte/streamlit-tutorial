# Streamlit Tutorial

- Streamlit Tutorial은 2024년 1학기 데이터 사이언스 개론 수강생을 대상으로 진행된 자료입니다.
- 작성일자: 2024년 4월 26일

## 프로젝트 환경 세팅

### Python과 VSC 설치

- Python이 컴퓨터에 설치되어 있어야 합니다. 파이썬의 버전은 3.8 이상을 권장합니다.
  - 로컬에 파이썬이 설치되지 않은 경우 [이 링크](https://wikidocs.net/8)에 설명된 방법을 따라 파이썬을 설치해주세요.
  - 설치된 파이썬 버전을 확인하고 싶다면, 다음과 같이 터미널에 입력해주세요.

```bash
python --version
```

- 코드 에디터인 Visual Studio Code를 다운로드 받습니다. [이 링크](https://code.visualstudio.com/download)를 클릭하면, VSC를 다운로드 받을 수 있습니다.

### 프로젝트 소스코드 다운로드

깃헙에서 해당 레포지토리의 소스코드를 다운로드 받습니다. 상단의 초록색 Code 버튼을 클릭한 후, 'Download ZIP'을 클릭하면 소스코드 zip 파일을 다운로드 받을 수 있습니다.

### VSC로 프로젝트 폴더 열기

이 레포지토리의 디렉토리는 다음과 같습니다.

```
streamlit-tutorial
├─ .gitignore
├─ README.md
├─ data
│  └─ 전국도서관표준데이터.csv
├─ main.py
└─ requirements.txt
```

- main.py: streamlit이 실행될 파이썬 파일로, 튜토리얼에서 진행할 코드를 담고 있습니다.
- README.md: 프로젝트의 소개와 사용법, 설치 방법 등에 대한 전반적인 정보를 포함하는 문서입니다.
- requirements.txt: 이 파일은 프로젝트가 의존하는 외부 라이브러리나 패키지의 목록을 포함합니다.
- .gitignore: 이 파일은 git 레포지토리에 포함되지 않아야 할 파일 또는 디렉토리를 지정합니다.
- data 폴더: 튜토리얼에서 사용할 데이터를 담고 있습니다.

### 마크다운(markdown) 사용하기

마크다운은 일반적인 텍스트 기반의 경량 마크업 언어입니다. 마크다운은 간단한 문법을 사용해 문서를 작성할 수 있습니다.

#### 마크다운 사용법

##### 헤더(headers)

헤더는 1~6까지 지원합니다.

```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
```

##### 텍스트 강조

마크다운은 **볼드체**, _이탤릭체_, ~~취소선~~ 등을 지원합니다.

```
*italic*
**bold**
~~stroke~~
```

##### 이미지 삽입

다음과 같이 이미지 경로를 넣어 이미지를 나타낼 수 있습니다.

```
![image title](/image/steve-busch-3aWG50MWn6U-unsplash.jpg)
```

![image title](/image/steve-busch-3aWG50MWn6U-unsplash.jpg)

##### 링크 삽입

다음과 같이 텍스트에 외부 링크를 삽입할 수 있습니다. [이 링크](https://github.com/givemetarte/streamlit-tutorial)를 클릭하면 튜토리얼의 깃헙 레포지토리로 연결됩니다.

```
[link title](https://github.com/givemetarte/streamlit-tutorial)
```

##### 코드 블럭 생성

백틱(`)을 이용해 코드 블럭을 생성할 수 있습니다. 코드 블럭 옆에 언어를 입력하면, 해당 언어에 맞는 syntax highlighting을 지원합니다.

```py
import pandas as pd

df = pd.read_csv('/data/공공도서관표준데이터.csv', encoding='utf-8')
```

#### 마크다운 Preview

VSC에서 작성한 마크다운 파일의 preview를 제공합니다. 열고싶은 마크다운 파일에 오른쪽 버튼을 클릭한 후 `open preview`를 클릭하면, 작성한 마크다운 파일이 어떻게 나타나는지 확인할 수 있습니다.

### 가상환경 생성하기

VSC 상단의 'Terminal'을 클릭하고, 'New Terminal'을 누르면 터미널을 열 수 있습니다. 이 때, 터미널이 열리는 경로를 확인하세요. 터미널의 경로는 streamlit-tutorial 폴더로 지정이 되어 있어야 합니다. 해당 터미널의 입력창에서 다음과 같이 코드를 순서대로 입력합니다.

이 튜토리얼에서 streamlit을 실행하기 위해 가상환경을 실행합니다. `venv`는 파이썬의 대표적인 가상환경 라이브러리로, 프로젝트마다 다른 버전의 패키지를 사용하고 싶을 때 개별 프로젝트를 실행할 수 있는 격리된 환경을 제공합니다.

```bash
# 1. generate python bubble
python -m venv env

# 2. activate
source env/bin/activate  # mac
env\Scripts\activate.bat  # window

# 3. install dependencies
pip install -r requirements.txt

# 4. deactivate bubble
deactivate
```

### Streamlit 실행하기

위의 가상환경이 실행된 상태에서 다음의 코드를 터미널에 작성합니다. 정상적으로 streamlit이 실행된다면 `localhost:8501`에서 튜토리얼을 확인할 수 있습니다.

```py
streamlit run main.py
```
