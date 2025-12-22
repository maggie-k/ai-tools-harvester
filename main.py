from apify import Actor
import asyncio
import pandas as pd
from rapidfuzz import process, fuzz

async def main():
    async with Actor:
        input_data = await Actor.get_input()

        query = input_data["query"]
        max_results = input_data.get("maxResults", 5)
        threshold = input_data.get("strictness", 70)

        df = pd.read_csv("app/scraped_data1.csv")

        matches = process.extract(
            query,
            df["description"].fillna("").tolist(),
            scorer=fuzz.token_sort_ratio,
            limit=max_results
        )

        for match, score, idx in matches:
            if score >= threshold:
                row = df.iloc[idx]
                await Actor.push_data({
                    "name": row["name"],
                    "website": row["website"],
                    "category": row.get("category"),
                    "score": score
                })

if __name__ == "__main__":
    asyncio.run(main())
