# SEC-Filings-MD

Build docker image

```bash
docker build -t sec-filings-pdf-md .
```

Run the docker image

```bash
docker run -v output:/output sec-filings-pdf-md --ticker AAPL --year 2023 --include_amends true --filing_types 10-K --num_chunks 1 --max 8 --workers 2
```