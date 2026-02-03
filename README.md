🛡️ Subdomain Discovery Tool
A modular reconnaissance scanner for DNS enumeration and security auditing.

🎯 Project Goals
Modular Design: Separate I/O, Logic, and Orchestration.

Resilience: Handle DNS Wildcards and invalid user inputs.

Clean Code: Industry-standard Python structure (PEP 8).

🛠️ Development Phases
Phase 1: Ingestion & Sanitization
[ ] clean_url(input): Strip protocols (http/https), www, and paths to extract the raw FQDN.

[ ] load_wordlist(path): Securely read and sanitize wordlist entries (remove whitespace/newlines).

Phase 2: Core DNS Logic (The MVP)
[ ] dns_check(domain): Implement socket.gethostbyname.

[ ] Error Handling: Gracefully handle socket.gaierror (return None on failure).

Phase 3: Advanced Detection
[ ] wildcard_check(target): Detect "Catch-all" DNS records via random sub-domain probing.

[ ] False-Positive Filtering: Compare scan results against the Wildcard IP.

Phase 4: Orchestration
[ ] main(): Coordinate the data flow (Input -> Clean -> Pre-check -> Scan).

[ ] CLI Interaction: Implement user-driven target selection.

Phase 5: Future Scope (Scaling)
[ ] Concurrency: Implement threading or asyncio for high-speed scanning.

[ ] HTTP Probing: Verify active web services (Status Codes 200, 403, etc.).

[ ] Data Export: Support for JSON/TXT output formats.
