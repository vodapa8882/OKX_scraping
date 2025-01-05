import argparse
from scraper.fetch_news import scrape_announcements

def main():
    parser = argparse.ArgumentParser(description="OKX News Scraper")
    parser.add_argument("--start-date", required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end-date", required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument("--output", required=True, help="Output folder for saved data")
    args = parser.parse_args()

    scrape_announcements(args.start_date, args.end_date, args.output)

if __name__ == "__main__":
    main()
