import boto3


def get_phone_numbers(recipients):
    phone_numbers = []
    for name in recipients.keys():
        phone_numbers.append(recipients[name]['sms'])

    return phone_numbers


def send_sms(recipients, message):
    recipient_phone_numbers = get_phone_numbers(recipients)
    sns_client = boto3.client('sns')
    for phone_number in recipient_phone_numbers:
        sns_client.publish(
            PhoneNumber=phone_number,
            Message=message
        )


def main():
    recipients = {'jake': {'sms': '+1234567890'}}
    send_sms(recipients, 'go to sleep')


if __name__ == '__main__':
    main()
