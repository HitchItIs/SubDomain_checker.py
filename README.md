# SUB-RECON 🔍
**Targeted Attack Surface Mapping & DNS Enumeration**

## I. Architecture & Philosophy
Built on a **decoupled functional approach**. By isolating data ingestion from the resolution logic, the tool ensures reliability and provides a foundation for future asynchronous scaling (AsyncIO).

Roadmap & Future Development#
----
1. Stability & Bugfixing (Highest Priority)
[ ] Logic Refactoring: Change dns_check to return None instead of error strings to prevent false-positive "Found" results.

[ ] Robust Error Handling: Implement a custom Exception-System instead of simple print statements in the data ingestion layer.

[ ] Input Sanitization: Add more rigorous checks for malformed wordlists and edge-case URLs.

2. Architecture & Clean Code
[ ] Type Hinting: Add Python Type Hints to all functions to improve maintainability and IDE support.

[ ] Decoupling: Separate the Core Logic (DNS resolution) from the CLI/Interface (Argparse/Print) to make the engine reusable as a library.

[ ] Logging: Replace standard print calls with the Python logging module for better debugging and audit trails.

3. Security Features (Recon Intelligence)
[ ] Wildcard Detection: Implement a pre-scan check to identify "catch-all" DNS records, preventing thousands of false-positive results.

[ ] Custom Timeouts: Add an option to set socket timeouts to prevent the scanner from hanging on unresponsive DNS servers.

[ ] Multi-DNS Support: Allow the user to specify custom DNS resolvers (e.g., 8.8.8.8) to bypass local DNS caching.

4. Performance & Scaling
[ ] Concurrency: Migration from synchronous execution to Threading or AsyncIO for high-speed scanning.

[ ] Export Engine: Add support for structured data export in JSON and CSV formats for integration into security pipelines.

## II. Core Features
* **Input Normalization:** Extraction and sanitization of FQDNs from raw datasets.
* **Resilient DNS Resolution:** Socket-based lookups with granular exception handling to manage network-level timeouts.
* **Wildcard Mitigation:** Pre-scan detection of catch-all records to minimize false positives.

## III. Installation & Quick Start
```bash
git clone [https://github.com/HitchItIs/Subdomain-Scanner](https://github.com/HitchItIs/Subdomain-Scanner)
cd Subdomain-Scanner
python subrecon.py --domain example.com

##  Legal Disclaimer & Operational Safety
----------
**For Educational and Authorized Testing Purposes Only.**

The use of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws. 

**Safe Use Guidelines:**
* **Test Environments:** This tool is architected strictly for authorized security auditing and educational research in controlled environments.
* **Rate Limiting:** Users should be aware that aggressive DNS enumeration can be interpreted as a Denial of Service (DoS) attempt or unauthorized scanning by ISP/Network security systems.
* **No Liability:** The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

**"Think before you scan."**
