import sys
import csv, json, re, requests
from bs4 import BeautifulSoup


def get_docid_from_recipe(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    el = soup.find(attrs={"data-doc-id": True})
    doc_id = None
    if el:
        doc_id = el.get("data-doc-id")
    return doc_id


def get_reviews_from_recipe(doc_id):
    # print(doc_id)
    # print(f"https://www.allrecipes.com/servemodel/model.json?modelId=feedbacks&docId={doc_id}&sort=DATE_DESC&offset=0&limit=100")
    response = requests.get(
        f"https://www.allrecipes.com/servemodel/model.json?modelId=feedbacks&docId={doc_id}&sort=DATE_DESC&offset=0&limit=100"
    )
    return response.json()


def to_csv(data):
    rows = data.get("list", [])

    fields = [
        "id",
        "docId",
        "displayName",
        "starRating",
        "helpfulCount",
        "madeIt",
        "created_iso",
        "profileUrl",
        "review_text",
    ]

    with open("allrecipes_reviews.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for it in rows:
            w.writerow(
                {
                    "id": it.get("id"),
                    "docId": it.get("docId"),
                    "displayName": it.get("displayName"),
                    "starRating": it.get("starRating"),
                    "helpfulCount": it.get("helpfulCount"),
                    "madeIt": it.get("madeIt"),
                    "created_iso": it.get("created"),
                    "profileUrl": it.get("profileUrl"),
                    "review_text": it.get("review"),
                }
            )


def main():
    # print("Arguments:", sys.argv[1:])
    data_doc_id = get_docid_from_recipe(sys.argv[1])
    reviews = get_reviews_from_recipe(data_doc_id)
    to_csv(reviews)


if __name__ == "__main__":
    main()
