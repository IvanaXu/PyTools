from playwright import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Fill input[name="wd"]
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=10086&fenlei=256&rsv_pq=ad15a4940001d122&rsv_t=f840YeEyeKZTmUX0y7fgcX5QOBCNhP1f89qiMhPoBrmOeLN06Ma4yahYVkA&rqlang=cn&rsv_dl=tb&rsv_enter=1&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=10086&rsp=5&inputT=3149&rsv_sug4=4074"):
    with page.expect_navigation():
        page.fill("input[name=\"wd\"]", "10086")

    # Go to https://www.baidu.com/s?wd=10086&pn=10&oq=10086&ie=utf-8&usm=2&fenlei=256&rsv_idx=1&rsv_pq=a112a6b700085ca5&rsv_t=07157W/FYoI9EpU/K6pmY/2J2KUyl47p1ktK2dxIWHtFteTH6+eBvgjNMLI&rsv_page=1
    page.goto(
        "https://www.baidu.com/s?wd=10086&pn=10&oq=10086&ie=utf-8&usm=2&fenlei=256&rsv_idx=1&rsv_pq=a112a6b700085ca5&rsv_t=07157W/FYoI9EpU/K6pmY/2J2KUyl47p1ktK2dxIWHtFteTH6+eBvgjNMLI&rsv_page=1"
    )

    # Go to https://www.baidu.com/s?wd=10086&pn=20&oq=10086&ie=utf-8&usm=2&fenlei=256&rsv_idx=1&rsv_pq=be80b4b500044644&rsv_t=6d36L8HZET8KmHbclzTYUT+wQf0woJF55DqHVCz/3crteViFpXNdCrbtRac&rsv_page=1
    page.goto(
        "https://www.baidu.com/s?wd=10086&pn=20&oq=10086&ie=utf-8&usm=2&fenlei=256&rsv_idx=1&rsv_pq=be80b4b500044644&rsv_t=6d36L8HZET8KmHbclzTYUT+wQf0woJF55DqHVCz/3crteViFpXNdCrbtRac&rsv_page=1"
    )

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
