# SEC-Filings-MD

Build docker image

```bash
docker build -t sec-filings-pdf-md .
```

Run the docker image

```bash
docker run --mount source=output,target=/output sec-filings-pdf-md --ticker AAPL --year 2024 --include_amends true --filing_types 10-Q -bm 2
```