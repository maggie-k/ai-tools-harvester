'''from fuzzywuzzy import process #migrate to RapidFuzz
from sqlalchemy import create_engine, text
import pandas as pd


engine= create_engine("sqlite+pysqlite:///C:/my-ai-tool-recommender/app/data/database.db")

with engine.connect() as conn:
    df= pd.read_sql("signups", conn, index_col='id')
    print(len(df))

df=pd.read_csv("C:/my-ai-tool-recommender/app/scraped_data1.csv")
#print(df)'''

from rapidfuzz import process, fuzz
import pandas as pd

df = pd.read_csv("C:/my-ai-tool-recommender/app/scraped_data1.csv")


def recommend_tools(user_need, threshold=50, limit=7):
    if not user_need or df.empty:
        return ["No tools found for your use case"]

    descriptions = df["description"].fillna("").tolist()

    matches = process.extract(
        user_need,
        descriptions,
        scorer=fuzz.token_set_ratio,
        limit=limit
    )

    best_tools = []
    seen = set()

    for desc, score, idx in matches:
        if score < threshold:
            continue

        tool_name = df.iloc[idx]["name"]

        if tool_name not in seen:
            best_tools.append(tool_name)
            seen.add(tool_name)

    return best_tools or ["No tools found for your use case"]


'''
def recommend_tools(user_need):
    best_tools = []

    descriptions = df['description'].tolist()
    matches = process.extract(user_need, descriptions, limit=10)

    for desc, score in matches:
        if score >= 50:
            tool_name = df.loc[df['description'] == desc, 'name']

            if not tool_name.empty:
                best_tools.append(tool_name.iloc[0])

    if not best_tools:
        return ["No tools found for your use case"]

    return best_tools'''




'''
def recommend_tools(user_need):

    best_tools=[]

    matches=process.extract(user_need, df['description'])
    for i,o in enumerate(matches):
        if matches[i][1]>=50:
            features= matches[i][0]

            tool=df[df['description']==features]

            best_tools.append(tool['name'].iloc[0])

    if best_tools==[]:
        return ["No tools found for your use case"]

    return best_tools'''
