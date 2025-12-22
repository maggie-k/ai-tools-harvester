from apify import Actor
import asyncio
import pandas as pd
from rapidfuzz import process, fuzz

async def main():
    async with Actor:        
        input_data = await Actor.get_input()
        print("Actor input:", input_data)

        if not input_data or "query" not in input_data:
            print("No query provided in input. Exiting actor.")
            return

        query = input_data["query"]
        max_results = input_data.get("maxResults", 5)
        threshold = input_data.get("strictness", 70)
        
        try:
            df = pd.read_csv("app/scraped_data1.csv")
            print(f"Loaded dataset with {len(df)} rows")
        except Exception as e:
            print("Error loading CSV:", e)
            return
        
        matches = process.extract(
            query,
            df["description"].fillna("").tolist(),
            scorer=fuzz.token_sort_ratio,
            limit=max_results
        )
        print(f"Found {len(matches)} matches")
        
        for match, score, idx in matches:
            if score >= threshold:
                row = df.iloc[idx]
                data = {
                    "name": row["name"],
                    "website": row["website"],
                    "category": row.get("category"),
                    "score": score
                }
                await Actor.push_data(data)
                print("✅ Pushed data to dataset:", data)

        print("Actor run completed.")

if __name__ == "__main__":
    asyncio.run(main())
