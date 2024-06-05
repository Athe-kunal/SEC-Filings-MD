# SEC-Filings-MD

Build docker image

```bash
docker build -t sec-filings-pdf-md .
```

Run the docker image

```bash
docker run --mount source=output,target=/output sec-filings-pdf-md --ticker AAPL --year 2024 --include_amends true --filing_types 10-Q -bm 2
```

Alternatively, you can run locally by first building a virtual environment

```bash
python -m venv marker-sec-env
```

Activate the virtual environment

```bash
source marker-sec-env/bin/activate
```

Install the packages

```bash
pip install -r requirements.txt
```
You also need to install the pdfkit requirements

For linux platforms, you can directly install

```bash
sudo apt-get install wkhtmltopdf
```

Refer [here](https://pypi.org/project/pdfkit/) for installation instructions

Run the `main.py` file to get the pdfs and convert it into markdowns

```bash
python main.py --ticker AAPL --year 2023 --include_amends true --filing_types 10-K,10-Q -bm 3
```