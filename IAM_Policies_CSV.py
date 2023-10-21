try:
  import boto3
except ImportError:
    print("boto3 module is not installed. Please install it using 'pip install boto3'.")
    exit(1)
import csv

def create_iam_policies_csv(output_Policy_csv):
    # Initialize the IAM client
    iam = boto3.client('iam')

    try:
        # List all policies in your AWS account
        policies = iam.list_policies(Scope='All')['Policies']

        # Create CSV file
        with open(output_Policy_csv, 'w', newline='') as csvfile:
            fieldnames = ['Policy Name', 'PolicyId', 'Arn']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row to the CSV file
            writer.writeheader()

            # Iterate through the policies in your AWS account
            for policy in policies:
                policy_name = policy['PolicyName']
                policy_id = policy['PolicyId']
                arn = policy['Arn']

                # Write the policy details to the CSV file
                writer.writerow({
                    'Policy Name': policy_name,
                    'PolicyId': policy_id,
                    'Arn': arn
                })

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    output_Policy_csv = 'iam_policies.csv'
    
    create_iam_policies_csv(output_Policy_csv)
