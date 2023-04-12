from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
arr = ["Cristiano Ronaldo face photo", "Lionel Messi face photo", "Usain Bolt face photo", "Serena Williams face photo", "Roger Federer face photo", "LeBron James face photo", "Novak Djokovic face photo", "Rafael Nadal face photo", "Michael Phelps face photo", "Kobe Bryant face photo", "Tom Brady face photo", "Simone Biles face photo", "Neymar Jr. face photo", "Mohamed Salah face photo", "Virat Kohli face photo", "Stephen Curry face photo", "Conor McGregor face photo", "Lewis Hamilton face photo", "Tiger Woods face photo", "Manny Pacquiao face photo"]
for e in arr:
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=1,
        downloader_threads=4,
        storage={'root_dir': f'./{e}'})
    filters = dict(
        size='large',
        color='orange',
        license='commercial,modify',
        date=((2017, 1, 1), (2023, 1, 3)))
    google_crawler.crawl(keyword=e, filters=filters, offset=0, max_num=50,
                        min_size=(200,200), max_size=None, file_idx_offset=0)

    bing_crawler = BingImageCrawler(downloader_threads=4,
                                    storage={'root_dir': f'./{e}'})
    bing_crawler.crawl(keyword=e, filters=None, offset=0, max_num=50)

    baidu_crawler = BaiduImageCrawler(storage={'root_dir': f'./{e}'})
    baidu_crawler.crawl(keyword=e, offset=0, max_num=50,
                        min_size=(200,200), max_size=None)