# Access Key Rotation Script

This script is designed to manage AWS IAM access keys by rotating them if they are older than 30 days. It uses the `boto3` library to interact with AWS services and checks the age of the access keys for a specified user. If the key is older than 30 days, it creates a new access key and deletes the old one.

It is based on Medium article [Automating AWS IAM Key Rotation with Python using Gitlab Pipeline](https://medium.com/@premjith.rk/automating-aws-iam-key-rotation-with-python-using-gitlab-pipeline-e5108bbb230c).

## Prerequisites

- Python 3.x
- AWS credentials configured (e.g., via `aws configure`)
- `boto3` library installed

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required Python packages:**

   ```bash
   pip install boto3
   ```

## Usage

To run the script, use the following command:

```bash
python rotate_access_keys.py <username>
```

Replace `<username>` with the actual IAM username whose access keys you want to rotate.

## How It Works

1. **List Access Keys:** The script lists all access keys for the specified user.
2. **Check Key Age:** It calculates the age of the first access key.
3. **Rotate Key:** If the key is older than 30 days:
   - A new access key is created.
   - The old access key is deleted.
4. **Output:** The script outputs the new access key ID and secret key if a new key is created.

## Logging

The script uses Python's `logging` module to log information at the `WARNING` level. You can adjust the logging level as needed.

## Example

```bash
python rotate_access_keys.py johndoe
```

If the access key for `johndoe` is older than 30 days, the script will output:

```
New Access Key ID: <new-access-key-id>
New Secret Key: <new-secret-key>
```

Otherwise, it will inform you that no new access key was created.

## Important Notes

- Ensure your AWS credentials have sufficient permissions to list, create, and delete access keys.
- Handle the new secret key securely; it will not be retrievable after the initial creation.
- Consider implementing additional security measures, such as notifying users when their keys are rotated.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.