import smtplib
from email.mime.text import MIMEText
import socket
import json

SMTP_HOST = "10.212.10.35"
SMTP_PORT = 25

def lambda_handler(event, context):
    for record in event.get("Records", []):
        try:
            # 1. SQS 바디 파싱
            body = json.loads(record["body"])
            raw_message = body.get("Message", "No Message")
            subject = body.get("Subject", "CloudWatch Alarm")

            # 2. 메시지 포맷 정리
            try:
                message_dict = json.loads(raw_message)
                formatted_message = "\n".join([f"{k}: {v}" for k, v in message_dict.items()])
            except json.JSONDecodeError:
                formatted_message = raw_message

            # 3. 이메일 구성
            msg = MIMEText(formatted_message, _charset="utf-8")
            msg["Subject"] = subject
            msg["From"] = "cloudwatch@hcs.com"
            msg["To"] = "aaa@hcs.com"

            # 4. SMTP 전송만 별도로 try 처리
            try:
                with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
                    server.sendmail(msg["From"], [msg["To"]], msg.as_string())
                    print("✅ 메일 전송 성공")
            except Exception as smtp_err:
                print(f"⛔ 메일 전송 실패: {smtp_err}")

        except Exception as e:
            print(f"⛔ 레코드 처리 중 예외 발생: {e}")

