# Day 16：Streamlit —— 把 RAG 变成网页
import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

api_key = "YOUR_DASHSCOPE_API_KEY"
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

llm = ChatOpenAI(model="qwen-plus", api_key=api_key, base_url=base_url)

# @st.cache_resource：知识库只建一次（Streamlit 每次点按钮都会重跑整个脚本，不缓存就每次重建）
@st.cache_resource
def build_store():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-v3",
        api_key=api_key,
        base_url=base_url,
        check_embedding_ctx_length=False,
    )
    with open(r"f:\Python\gongc\py_day1\pythonProject3\知识库.txt", "r", encoding="utf-8") as f:
        text = f.read()
    splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
    chunks = splitter.split_text(text)
    return Chroma.from_texts(chunks, embeddings, collection_name="rs_kb_web")

store = build_store()

# ===== 网页界面（这些 st.xxx 就是网页上的组件）=====
st.title("遥感知识库问答系统")
st.write("基于 RAG 的遥感知识问答，输入问题试试")

question = st.text_input("你的问题：", placeholder="例如：什么是 PS-InSAR？")

if st.button("提问") and question:
    # 检索 + 生成（和 Day15 完全一样）
    docs = store.similarity_search(question, k=2)
    material = "\n".join(d.page_content for d in docs)
    prompt = f"参考材料：\n{material}\n\n问题：{question}\n请根据上面的材料回答。材料里没有的，就说不知道。"
    answer = llm.invoke(prompt)

    st.markdown("### 回答")
    st.write(answer.content)
    st.markdown("### 检索到的资料")
    for d in docs:
        st.info(d.page_content)