# OKX Scraping

OKX Scraper is a cross-platform tool for scraping announcements and news from the [OKX](https://www.okx.com/help/section/announcements-latest-announcements) platform. It supports macOS, Linux, and Windows with pre-built executables for ease of use.

## Features
- Scrape announcements between specified dates.
- Save data to a specified folder.
- Easy-to-use command-line interface.

## Output Information
The output file contains the following information for each announcement:
- **Title**: The title of the announcement.
- **Publish Date**: The date the announcement was published.
- **Link**: A direct link to the announcement on the website.
- **Content**: The full content of the announcement.

> **Note**: Extracting the content increases the running time of the program. In future versions, the content extraction might be removed if it is considered unnecessary.

## Date and Time Details
- The publication time of news is shown in **China Standard Time (CST)**, which has an offset of **+8 hours from UTC**.
- The website displays publication dates in the user's local timezone, but the scraper processes dates in CST. 
- To prevent confusion, the scraper converts the publish time to **UTC** and uses the corresponding UTC date.

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
