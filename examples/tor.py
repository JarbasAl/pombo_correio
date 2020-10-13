from pombo_correio import TorBrowser

if __name__ == "__main__":
    from os.path import join, dirname, expanduser

    gecko_driver = join(dirname(__file__), "geckodriver")
    # https://github.com/mozilla/geckodriver/releases

    binary = expanduser("~/Downloads/tor-browser_en-US/Browser/firefox")
    # Using context manager
    with TorBrowser(gecko_driver,
                    headless=True,
                    images_enabled=False,
                    js_enabled=False,
                    tor_ff_binary=binary) as browser:
        url = browser.find_and_click_xpath("/html/body/div[2]/p[2]/a[2]")
        browser.wait_for_xpath("/html/body/div/div[4]/div[2]/h2/span")
        browser.save_screenshot("tor_relay.png")
