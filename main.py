from apify import Actor
import asyncio
import pandas as pd
from rapidfuzz import process, fuzz

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        print("Actor input:", input_data)

        if not input_data or "query" not in input_data:
            print("No query provided. Exiting.")
            return

        query = input_data["query"]
        max_results = input_data.get("maxResults", 7)
        threshold = input_data.get("strictness", 59)

        try:
            df = pd.read_csv("app/scraped_data1.csv")
            print(f"Loaded dataset with {len(df)} rows")
        except Exception as e:
            print("CSV load error:", e)
            return

        matches = process.extract(
            query,
            df["description"].fillna("").tolist(),
            scorer=fuzz.token_set_ratio,
            limit=max_results
        )
        print(f"Found {len(matches)} matches")

        any_pushed = False
        for match, score, idx in matches:
            print(f"Match: {match}, Score: {score}, Index: {idx}")
            row = df.iloc[idx]
            if score >= threshold:
                data = {
                    "name": row["name"],
                    "website": row["website"],
                    "category": row.get("category"),
                    "score": score
                }
                await Actor.push_data(data)
                any_pushed = True
                print("✅ Pushed to dataset:", data)
            else:
                print("Score below threshold; skipping.")

        if not any_pushed:
            print("No rows passed the threshold; pushing at least top match")
            # Pushes top match anyway to avoid empty dataset
            top_match = matches[0]
            row = df.iloc[top_match[2]]
            data = {
                "name": row["name"],
                "website": row["website"],
                "category": row.get("category"),
                "score": top_match[1]
            }
            await Actor.push_data(data)
            print("✅ Pushed top match to dataset:", data)

        print("Actor run completed.")

if __name__ == "__main__":
    asyncio.run(main())
