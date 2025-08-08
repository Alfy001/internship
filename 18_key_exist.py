book_details = {
    "title": "Wings of Fire",
    "author": "A.P.J. Abdul Kalam",
    "published": 1999
}
search_key = "author"

if search_key in book_details:
    print(f"The key '{search_key}' is present in the record.")
else:
    print(f"The key '{search_key}' is not present in the record.")
