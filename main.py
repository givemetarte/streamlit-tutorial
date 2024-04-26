import time
import pandas as pd
import streamlit as st

def main():
    # title: https://docs.streamlit.io/develop/api-reference/text/st.title
    st.title(":sunglasses: Streamlit Tutorial")
    text_elements()
    data_analysis()

def text_elements():

    # subheader: https://docs.streamlit.io/develop/api-reference/text/st.subheader
    st.subheader("마크다운으로 글쓰기")
    code = """
    import pandas as pd 
            
    df = pd.read_csv('data/data.csv', encoding='utf-8')
    """

    # markdown: https://docs.streamlit.io/develop/api-reference/text/st.markdown
    description = f"""
    이 파트는 Streamlit에서 제공하는 텍스트와 관련된 기능을 소개합니다. 마크다운으로 텍스트 스타일을 변경하고, 코드 블록을 생성하거나 캡션을 다는 등의 기능을 사용할 수 있습니다.
    - **볼드체**와 *이탤릭체*: 볼드체는 **별표 2개**로 감싸고, 이탤릭체는 *별표 1개*로 감싸면 됩니다. 
    - 글자색 변경: Streamlit에서 지원하는 내장 기능으로 글자색을 변경할 수 있습니다. :red[빨간색], :orange[주황색], :green[초록색], :blue[파란색], :violet[보라색] 등을 색변화를 줄 수 있고, :rainbow[무지개색]으로도 글자색 변경이 가능합니다.
    - 이모지 사용: 내장된 이모지 사용도 가능합니다. :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:
    - 텍스트에 링크 삽입: 텍스트에 링크를 삽입하려면, `[링크명](URL)` 형식으로 작성하면 됩니다.
    - 코드 블록 사용: 다음과 같이 코드 블록을 생성할 수 있습니다. `st.code()` 함수의 파라미터로 `language`를 지정하면 해당 언어에 맞게 syntax highlighting을 적용할 수 있습니다.
    """
    st.markdown(description)
    # code block: https://docs.streamlit.io/develop/api-reference/text/st.code
    code = """
    import pandas as pd 
            
    df = pd.read_csv('data/data.csv', encoding='utf-8')
    """
    st.code(code, language="python")

    # caption: https://docs.streamlit.io/develop/api-reference/text/st.caption
    st.caption("이런 방식으로 작게 주석을 다는 것도 가능합니다.")

    # divider: https://docs.streamlit.io/develop/api-reference/text/st.divider
    st.divider()


def data_analysis():
    st.subheader("도서관 데이터 분석")

    # dataframe: https://docs.streamlit.io/develop/api-reference/data/st.dataframe
    description = """
    파이썬으로 간단한 데이터 분석을 수행한 후 이 결과를 Streamlit으로 시각화할 수 있습니다. 
    - 데이터 분석 과제: 공공데이터포털의 전국도서관표준데이터를 활용해 (1) 도서관의 자료수(도서)를 기준으로 상위 5개의 도서관 목록을 추출하고, (2) 시도별 도서관의 소장자료수(도서)를 분석합니다.
    - 공공데이터포털의 전국도서관표준데이터는 [이 링크](https://www.data.go.kr/data/15013109/standard.do)에서 다운로드 받을 수 있습니다.
    
    #### EDA (Exploratory Data Analysis)
    Streamlit은 파이썬의 Pandas로 불러온 데이터프레임을 그대로 사용할 수 있습니다. 다음의 `st.dataframe()` 함수를 사용하면, 데이터프레임으로 불러온 
    데이터를 표 형태로 출력할 수 있습니다. 다만, 이 표는 사용자가 수정할 수 없습니다. 
    """
    st.markdown(description)

    df = pd.read_csv("data/전국도서관표준데이터.csv", encoding="cp949")
    st.dataframe(df)

    description = f"""
    위의 데이터를 간단히 살펴봅시다. 
    - 전국의 도서관 수는 {df.shape[0]}입니다.
    - 도서관 유형은 {str(df['도서관유형'].unique())[1:-1]}이 있습니다.
    - 도서관의 평균 대출가능권수는 {round(df['대출가능권수'].mean(),2)}입니다. 이와 같은 값이 나온 이유는 대출가능권수에 소장자료(도서)와 동일한 값을 작성한 도서관이 다수 있기 때문입니다.
    - 도서관의 평균 대출가능일수는 {round(df['대출가능일수'].mean(),2)}입니다.
    
    #### 데이터 정제

    소장자료수(도서)를 기준으로 상위 5개의 도서관 목록을 출력하려고 합니다. 그러나 `df['자료수(도서)']`로 정렬하려면, 현재 이 값은 텍스트 형태이기 때문에 `int`로 바꿔줘야 합니다.

    하지만 `df['자료수(도서)']`에 숫자가 아닌 '+'가 포함된 값이 있습니다. 다음과 같이 데이터 오류를 수정하고, 컬럼의 데이터 타입을 `int`로 변경합니다.
    """
    st.markdown(description)

    df.at[3169, '자료수(도서)'] = 47698
    df['자료수(도서)'] = df['자료수(도서)'].astype(int)
    
    code = """
    df.at[3169, '자료수(도서)'] = 47698
    df['자료수(도서)'] = df['자료수(도서)'].astype(int)
    """
    st.code(code, language="python")

    description = """
    #### 데이터 분석 결과

    다음은 도서관의 자료수(도서)를 기준으로 상위 5개의 도서관 목록을 출력합니다. 
    이 결과를 `st.data_editor()` 함수를 사용해 편집 가능한 표 형태로 출력합니다.
    `column_config` 파라미터는 각 컬럼의 형식을 지정할 수 있습니다.
    - 별점: 1-5 사이의 별점을 입력할 수 있습니다. 
    - 선택: checkbox를 이용해 해당 도서관을 선택할 수 있습니다.
    - 월별 이용자수(최근 6개월): 표 내부에 차트를 넣을 수 있습니다. 이 데이터는 예시를 위해 임의로 생성했습니다.
    """
    st.markdown(description)

    # data_editor: https://docs.streamlit.io/develop/api-reference/data/st.data_editor
    # column config: https://docs.streamlit.io/develop/api-reference/data/st.column_config
    top_df = df.sort_values(by="자료수(도서)", ascending=False).head(5)
    top_df = top_df[["도서관명", "시도명", "시군구명"]]
    top_df["별점"] = 0
    top_df["선택"] = False

    users_data = [
        [0, 4, 26, 80, 100, 40],
        [80, 20, 80, 35, 40, 100],
        [10, 20, 80, 80, 70, 0],
        [10, 100, 20, 100, 30, 100],
        [12, 24, 35, 46, 24, 35]
    ]
    top_df["월별 이용자수"] = users_data

    st.data_editor(
        top_df,
        column_config={
            "별점": st.column_config.NumberColumn(
                "별점",
                help="도서관에 대한 별점을 입력하세요. (1-5)",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
            ),
            "선택": st.column_config.CheckboxColumn("선택", help="선택 여부를 체크하세요."),
            "월별 이용자수": st.column_config.BarChartColumn(
                "월별 이용자수(최근 6개월)",
                help="최근 6개월 동안의 월별 이용자수입니다.",
                y_min=0,
                y_max=100,
            )
        },
        hide_index=True,
    )
    description = """
    #### 데이터 시각화 

    다음은 시도별 도서관의 소장자료수(도서)를 분석하고, 바 그래프로 시각화합니다. 
    시도별 도서관의 소장자료수는 다음과 같이 `groupby`를 사용해 구할 수 있습니다. `st.bar_chart()` 함수는 Streamlit에 내장된 바 그래프를 생성합니다. 
    내장된 차트 이외에 파이썬의 시각화 라이브러리인 [bokeh](https://docs.streamlit.io/develop/api-reference/charts/st.bokeh_chart), 
    [plotly](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart), [pydeck](https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart) 등을 사용할 수 있습니다.
    """
    st.markdown(description)

    code = """
    chart_data = df.groupby("시도명")["자료수(도서)"].sum().reset_index()
    st.bar_chart(chart_data, x="시도명", y="자료수(도서)", color="#A3D8FF")
    """
    st.code(code, language="python")

    chart_data = df.groupby("시도명")["자료수(도서)"].sum().reset_index()
    st.bar_chart(chart_data, x="시도명", y="자료수(도서)", color="#A3D8FF")

    description = """
    #### 데이터 다운로드 

    Streamlit은 버튼 클릭 시 데이터를 다운로드 받을 수 있는 기능을 제공합니다. 
    `CSV 다운로드`를 클릭하면 앞서 생성한 시도별 자료수(도서)의 데이터를 다운로드 받을 수 있습니다.

    """
    st.markdown(description)
    
    # download_button: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button
    download_data = chart_data.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="CSV 다운로드",
        data=download_data,
        file_name='시도별 소장자료 분석 데이터.csv',
        mime='text/csv',
    )


if __name__ == "__main__":
    main()
