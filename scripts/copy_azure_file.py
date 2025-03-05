import argparse
import os
from azure.storage.fileshare import ShareFileClient


def copy_azure_file(
        connection_string: str,
        share_name: str,
        file_path: str,
        output_path: str
):
    """Copy a single file from Azure File Share to local path.

    Args:
        connection_string: Azure storage connection string
        share_name: Name of the file share
        file_path: Path to file within the share
        output_path: Local path where file should be copied
    """
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Initialize the file client
    file_client = ShareFileClient.from_connection_string(
        connection_string,
        share_name=share_name,
        file_path=file_path
    )

    # Download the file
    print(f"Copying {file_path} to {output_path}")
    with open(output_path, "wb") as file_handle:
        data = file_client.download_file()
        data.readinto(file_handle)


def main():
    parser = argparse.ArgumentParser(
        description="Copy a file from Azure File Share"
    )
    parser.add_argument(
        "--share-name", required=True, help="Name of the file share"
    )
    parser.add_argument(
        "--file-path", required=True, help="Path to file within the share"
    )
    parser.add_argument(
        "--output-path",
        required=True,
        help="Local path where file should be copied"
    )
    args = parser.parse_args()

    # Get connection string from environment variables
    account_name = os.environ.get('AZURE_STORAGE_ACCOUNT')
    account_key = os.environ.get('AZURE_STORAGE_KEY')

    connection_string = (
        f"DefaultEndpointsProtocol=https;"
        f"AccountName={account_name};"
        f"AccountKey={account_key};"
        f"EndpointSuffix=core.windows.net"
    )

    copy_azure_file(
        connection_string, args.share_name, args.file_path, args.output_path
    )


if __name__ == '__main__':
    main()
