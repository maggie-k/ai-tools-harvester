from rapidfuzz import process, fuzz
import pandas as pd

df = pd.read_csv("scraped_data1.csv")


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
