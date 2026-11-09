
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Website URL
URL = "https://www.bbc.com/news"

# Browser headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    )
}


def scrape_headlines():

    print("\n===== NEWS HEADLINE SCRAPER =====")

    try:
        # Send GET request
        print("\nConnecting to BBC News...")

        response = requests.get(
            URL,
            headers=headers,
            timeout=15
        )

        # Check HTTP response
        response.raise_for_status()

        print("Website connected successfully!")

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline elements
        headline_tags = soup.find_all(["h2", "h3"])

        headlines = []
        seen = set()

        for tag in headline_tags:

            headline = tag.get_text(
                separator=" ",
                strip=True
            )

            # Remove empty and duplicate headlines
            if headline and headline not in seen:
                headlines.append(headline)
                seen.add(headline)

        # Limit to 20 headlines
        headlines = headlines[:20]

        if not headlines:
            print("No headlines found.")
            print("The website HTML structure may have changed.")
            return

        # Display headlines
        print("\n===== TOP NEWS HEADLINES =====\n")

        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline}")

        # Save headlines to text file
        with open("headlines.txt", "w", encoding="utf-8") as file:

            file.write("BBC NEWS - TOP HEADLINES\n")
            file.write("=" * 50 + "\n")
            file.write(
                f"Scraped on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            )
            file.write("=" * 50 + "\n\n")

            for index, headline in enumerate(headlines, start=1):
                file.write(f"{index}. {headline}\n")

        print("\nSuccessfully saved headlines to headlines.txt")
        print(f"Total headlines collected: {len(headlines)}")

    except requests.exceptions.Timeout:
        print("Error: Website request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the website.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")


# Main program
if __name__ == "__main__":
    scrape_headlines()
