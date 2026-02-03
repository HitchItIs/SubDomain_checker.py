🛠 Phase 1: Ingestion & Sanitization (The Foundation)


[ ] Task 1: The Target Cleaner (clean_url)

Goal: Handle user copy-pasting full URLs (e.g., https://google.com/search).

Logic: Strip http://, https://, www., and everything after the /.


[ ] Task 2: The Wordlist Loader (load_wordlist)

Goal: Read your names.txt file (containing dev, api, admin).

Logic: Open file, .splitlines(), and .strip() each line to remove hidden spaces.


 Phase 2: The Core Logic (The Specialist)

[ ] Task 3: The DNS Specialist (dns_check)

Goal: Check if ONE specific domain exists.

Logic: Takes full_domain (String) -> try/except socket.gaierror -> returns IP Address (String) or None..

 Phase 3: The  Gatekeeper (Wildcard Detection)
This prevents 10,000 "fake" results if a server is set to catch-all.

[ ] Task 4: The Wildcard Probe (check_wildcard)

Goal: Detect if the target server "lies" by resolving everything.

Logic: Generate a random string (e.g., asdf123.target.com). If it resolves to an IP, save that IP as a "Wildcard IP."


Phase 4: Orchestration (The Controller)

[ ] Task 5: The Main Loop (run_scanner)

Goal: Coordinate the flow.

Flow: 1. Get Input -> 2. Clean Target -> 3. Load Wordlist -> 4. Run Wildcard Check -> 5. Loop & Print Results.

[ ] Task 6: The "Entry Point" (if __name__ == "__main__":)

Logic: This ensures the code only runs if the file is executed directly, not imported.

 Phase 5: Future Expansion (What's coming later)
Once the foundation is rock solid, we will add these "Senior" features.

[ ] Concurrency: Use threading to check 50 domains at once (Speed boost 100x).

[ ] HTTP Probing: Don't just find IPs—check for web servers and read their titles/status codes.

[ ] Exporting: Automatically save "Hits" into a results.txt file.

[ ] CLI Arguments: Use argparse so you can run it like a pro: python scanner.py -t google.com -w mylist.txt.
