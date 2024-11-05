import camelot
import os

def extract_tables_from_pdf(pdf_path, output_csv_path):
    # Read the PDF
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

    # Check if any tables were found
    if not tables:
        print("No tables found in the PDF.")
        return

    # Export each table to a separate CSV file
    for i, table in enumerate(tables):
        table.to_csv(f"{output_csv_path}_table_{i + 1}.csv")
        print(f"Table {i + 1} saved to {output_csv_path}_table_{i + 1}.csv")

# def main():
# Use an absolute path to the PDF file
pdf_path = os.path.abspath("portfolio_holdings.pdf")
output_csv_path = os.path.abspath("portfolio_holdings")
extract_tables_from_pdf(pdf_path, output_csv_path)


# if __name__ == "__main__":
#     main()