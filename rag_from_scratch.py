import chromadb
from openai import OpenAI

api_key = "YOUR_DASHSCOPE_API_KEY"
client = OpenAI(api_key=api_key, base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

def embed(text):
    response = client.embeddings.create(model="text-embedding-v3",input=text)
    return response.data[0].embedding

def chunk(text):
    return text.split("\n\n")
    

with open("f:\Python\gongc\py_day1\pythonProject3\知识库.txt", "r", encoding="utf-8") as f:
    text = f.read()
chunks = chunk(text)
print(f"切成{len(chunks)}块")

vectors = []
for chunk in chunks:
    vectors.append(embed(chunk))
print(f"转成 {len(vectors)} 个向量")

db = chromadb.Client()
collection = db.create_collection("rs_kb")

ids = []
for i in range(len(chunks)):
    ids.append(f"块{i}")

collection.add(ids=ids, documents=chunks, embeddings=vectors)
print("已存入向量库")

question = "什么是ps-insar"
questionembed = embed(question)
result = collection.query(query_embeddings=[questionembed],n_results=2)

docs = result["documents"][0]
mates = "\n".join(docs)
prompt = "参考材料：\n" + mates + "\n\n问题：" + question + "\n请根据上面的材料回答问题。材料里没有的，就说不知道。"

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": "用一句话介绍什么是 InSAR 技术？"},
    ],
)

answer = response.choices[0].message.content
print("模型回答：")
print(answer)
print(docs)



