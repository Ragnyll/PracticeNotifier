import boto3
import requests


def get_phone_numbers(recipients):
    """Gets a list of phone numbers from a recipients dictionary

    Args:
        recipients(dict): a dictionary of recipients

    Returns:
        list: a list of phone_numbers
    """
    phone_numbers = []
    for name in recipients.keys():
        phone_numbers.append(recipients[name]['sms'])

    return phone_numbers


def send_sms(recipients, subject, message):
    """Sends a message to each phone numbers using aws SNS

    Args:
        recipients(dict): a dicitionary of recipients
        subject(str): the subject of the message
        message(str): the body of the message
    """
    recipient_phone_numbers = get_phone_numbers(recipients)
    sns_client = boto3.client('sns')
    for phone_number in recipient_phone_numbers:
        sns_client.publish(
            PhoneNumber=phone_number,
            Subject=subject,
            Message=message
        )


def send_facebook_messenger_message(recipients, message):
    """Sends a message to each person on facebook with messenger

    Args:
        recipients(dict): a dictionary of recipients
    """
    pass


def main():
    recipients = {'jake': {'sms': '+1234567890'}}
    send_sms(recipients, 'practice', 'go to sleep')
    send_facebook_messenger_message(recipients, 'message')


if __name__ == '__main__':
    main()
