import asyncio, sys, json, os
from playwright.async_api import async_playwright
async def main():
    mode=sys.argv[1]
    out=sys.argv[2]; os.makedirs(out,exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=float(os.environ.get('DSF','1')))
        errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file:///home/claude/vert2/index.html')
        await pg.wait_for_timeout(600)
        if mode=='spots':
            times=json.loads(sys.argv[3])
            for t in times:
                await pg.evaluate(f'__render({t})')
                await pg.screenshot(path=f'{out}/s_{t:06.2f}.png')
        else:
            start,end,step,fps=int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),30
            for f in range(start,end,step):
                await pg.evaluate(f'__render({f/fps})')
                await pg.screenshot(path=f'{out}/f{f:04d}.jpg',type='jpeg',quality=92)
        if errs: print('ERRORS',errs[:5])
        await b.close()
asyncio.run(main())
