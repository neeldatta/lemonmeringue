import asyncio
from lemonmeringue import quick_generate, Voices

async def test():
    # This would actually call the API - replace with your key
    print("LemonMeringue is ready to use!")
    print(f"Available voices: {len([v for v in dir(Voices) if not v.startswith('_')])}")

asyncio.run(test())
