import sys
import requests
import xlsxwriter


def export_results(emails):
    """
    Exports the results into a XLSX file
    """
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    count = 0
    try:
        print("Exporting the results in an excel")
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('hunter.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, "email")
        row += 1

        # Iterate over the data and write it out row by row.
        for email in emails:
            col = 0
            worksheet.write(row, col, email)
            row += 1
            count += 1

        # Close the excel
        workbook.close()

    except Exception as excp:
        print("Error in export_results" + str(excp))


def manage_response(data):
    """
    Treats the response obtained from the API
    """
    emails = []
    try:
        for email in data['data']['emails']:
            print("\n[*]Email: " + str(email['value']))
            emails.append(str(email['value']))
    except Exception:
        print("Could not find any information about that")
        emails = "-"
    return emails


def send_request(url):
    """
    Sends custom request to the API
    """
    response = None
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
    except Exception as excp:
        print(excp)
    return response.json()

def main():
    """
    Main function of this tool
    """
    banner()
    target = str(sys.argv)
    api = "21210edcfd10f0bda04920bbb45cdae7012d3cf6"
    response = None
    emails = []
    limit = 10000  # by default limit=10
    try:
        url = "https://api.hunter.io/v2/domain-search?domain=latrobe.edu.au&api_key=21210edcfd10f0bda04920bbb45cdae7012d3cf6" + \
            target+"&api_key="+api+"&limit="+str(limit)
        # Sent request
        response = send_request(url)
        # Manage the response
        emails = manage_response(response)
        # Export results
        if emails != "-":
            export_results(emails)
    except Exception as exception:
        print("Error in main function" + str(exception))


if __name__ == "__main__":
    main()
