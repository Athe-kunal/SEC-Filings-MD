import subprocess
import os

SAVE_DIR = "output/SEC_EDGAR_FILINGS_MD"
def run_marker(input_ticker_year_path:str,ticker:str,year:str,workers:int=4,max_workers:int=8,num_chunks:int=1):
    # subprocess.run(["ls", "-l"]) 
    path_to_metadata = os.path.join(input_ticker_year_path,"metadata.json")
    output_ticker_year_path = os.path.join(SAVE_DIR,f"{ticker}-{year}")
    os.makedirs(SAVE_DIR,exist_ok=True)
    
    subprocess.run(["marker", input_ticker_year_path,output_ticker_year_path,  "--workers", str(workers), "--num_chunks",str(num_chunks),"--max", str(max_workers) ,"--metadata_file", path_to_metadata])