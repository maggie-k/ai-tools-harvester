from apify import Actor
import asyncio

async def main():
    async with Actor:
        input_data = await Actor.get_input()
        Actor.log.info(f"Input received: {input_data}")

        # Call your existing backend logic here
        # Example:
        # results = run_scraper(input_data)

        # Dummy example output
        await Actor.push_data({
            "name": "Example AI Tool",
            "website": "https://example.com",
            "category": "LLM",
            "score": 0.92
        })

if __name__ == "__main__":
    asyncio.run(main())
