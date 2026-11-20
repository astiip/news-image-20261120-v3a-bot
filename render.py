import asyncio, hashlib
from playwright.async_api import async_playwright

REPO = "/home/hatch/workspace/makefun/news-image-20261120-v3a-bot"

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1024, "height": 1024})
        await pg.goto(f"file://{REPO}/build.html")
        await pg.wait_for_timeout(400)
        m = await pg.evaluate("""() => {
          const foot = document.querySelector('.foot');
          const r = foot.getBoundingClientRect();
          const paper = document.querySelector('.paper');
          return {footBottom: r.bottom, paperH: paper.getBoundingClientRect().height,
                  bodyScrollH: document.body.scrollHeight, overflow: document.body.scrollHeight > 1024};
        }""")
        print("measure:", m)
        await pg.screenshot(path=f"{REPO}/entry.png")
        await b.close()
    h = hashlib.sha256(open(f"{REPO}/entry.png", "rb").read()).hexdigest()
    print("sha256:", h)

asyncio.run(main())
