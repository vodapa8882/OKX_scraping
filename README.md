# OKX Scraping

OKX Scraper is a cross-platform tool for scraping announcements and news from the [OKX](https://www.okx.com/help/section/announcements-latest-announcements) platform. It supports macOS, Linux, and Windows with pre-built executables for ease of use.

## Features
- Scrape announcements between specified dates.
- Save data to a specified folder.
- Easy-to-use command-line interface.

## Installation
Visit the [Releases](https://github.com/vodapa8882/OKX_scraping/releases) page and download the executable for your platform:
- macOS: `OKX-scraper-macos-latest.tar.gz`
- Linux: `OKX-scraper-ubuntu-latest.tar.gz`
- Windows: `OKX-scraper-windows-latest.zip`

## Usage
Run the tool from your command line:
```bash
OKX-scraper --start-date <YYYY-MM-DD> --end-date <YYYY-MM-DD> --output <output-folder>
```

### Example
```bash
OKX-scraper --start-date 2023-01-01 --end-date 2023-12-31 --output ./data/
```
