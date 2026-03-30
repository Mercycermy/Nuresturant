import asyncio
from playwright.async_api import async_playwright
import os

async def capture_screenshots():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        viewports = [
            {"name": "desktop", "width": 1920, "height": 1080},
            {"name": "tablet", "width": 768, "height": 1024},
            {"name": "mobile", "width": 375, "height": 667}
        ]

        pages = ["index.html", "privacy.html", "terms.html", "help.html"]

        os.makedirs("verification", exist_ok=True)

        for page_name in pages:
            for vp in viewports:
                await page.set_viewport_size({"width": vp["width"], "height": vp["height"]})
                await page.goto(f"http://localhost:3000/{page_name}")
                # Wait a bit for animations
                await asyncio.sleep(2)
                screenshot_path = f"verification/{page_name.split('.')[0]}_{vp['name']}.png"
                await page.screenshot(path=screenshot_path, full_page=True)
                print(f"Captured {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_screenshots())
